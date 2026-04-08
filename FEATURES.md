# Feature Engineering (BRES Manuscript Classifier)

This document explains every feature the classifier extracts from a manuscript sequence and why it matters.

---

## Structural features

These are computed directly from the symbol sequence string.

| Feature | Formula | What it captures |
|---|---|---|
| `total_symbol_count` | `len(symbols)` | Total length of the sequence |
| `unique_symbol_count` | `len(set(symbols))` | Number of distinct symbols |
| `repeated_symbol_ratio` | `(total - unique) / total` | How much repetition exists |
| `unique_symbol_ratio` | `unique / total` | Inverse of repeated symbol ratio |
| `symbol_entropy_score` | Shannon entropy of symbol frequencies | Measures randomness; all-unique approaches max entropy |
| `phase_gap_std` | Standard deviation of positional gaps between repeat occurrences | Regularity of symbol recurrence |
| `dominant_cycle_length` | Derived from repeating positional patterns in the sequence | Estimated period of the dominant cycle |

---

## GCD alignment features

For each known calendar number `n` in `{12, 13, 18, 20, 28, 29, 30, 36, 260}`, a binary flag is set:

```text
gcd_match_n = 1  if  unique == n  OR  unique % n == 0  OR  n % unique == 0
```

This captures both exact matches and harmonic relationships between symbol counts and known calendrical cycles.

For example:
- 36 decans → `gcd_match_36 = 1`
- 12 zodiac signs → `gcd_match_12 = 1`, and also `gcd_match_36 = 1` because 36 % 12 = 0

---

## Herbal keyword feature

```text
herbal_score = count(symbols containing herbal keywords) / total_symbols
```

The keyword list includes words such as: rose, lily, sage, mint, thyme, basil, lavender, oak, ash, elder, mugwort, wormwood, hyssop, valerian, and mandrake.

Scores above `0.1` are treated as a strong botanical signal.

---

## Context features (binary flags)

These are derived from optional metadata passed alongside the sequence.

| Feature | Set to 1 when |
|---|---|
| `ctx_circular` | layout contains `circular` or `zodiac` |
| `ctx_linear` | layout contains `linear` |
| `ctx_grid` | layout contains `grid` |
| `ctx_egyptian` | origin contains `egyptian` or `hellenistic` |
| `ctx_mesoamerican` | origin contains `mayan`, `aztec`, or `mesoamerican` |
| `ctx_lunar_origin` | origin contains `chinese`, `arabic`, `vedic`, `indian`, `islamic`, or `hebrew` |
| `ctx_celtic` | origin contains `celtic` |
| `ctx_herbal_type` | symbol_type contains `plant`, `herb`, `flower`, or `botanical` |
| `ctx_star_type` | symbol_type contains `star`, `decan`, `constellation`, or `sign` |

---

## Classification scoring

The rule engine scores each calendar type against the features using a weighted sum:

| Signal | Weight |
|---|---|
| Unique symbol count in expected range | 0.45 |
| Origin context match | 0.15 |
| GCD alignment | 0.20 |
| Layout context match | 0.10 |
| Symbol type context match | 0.10 |
| Herbal keyword density (botanical only) | +0.30 |

Scores are capped at `1.0`. Only types scoring `>= 0.20` appear in results.

---

## Known limitations

**Astronomical feature**  
The original `calc_astronomical_alignment()` function computes sun altitude variation over `N` days from a fixed anchor date. That makes it mostly a function of sequence length rather than manuscript content. It is kept for backward compatibility, but it should be tied to an artifact's actual astronomical period in a future version.

**Small dataset**  
With fewer than 50 labeled samples, the ML layer (Random Forest) is not trained. The rule-based engine runs exclusively until the dataset grows.

**Single-sequence assumption**  
Each manuscript is represented as a single flat sequence. Manuscripts with multiple columns, hierarchical structure, or 2D layouts such as grids and spirals may require preprocessing before classification.
