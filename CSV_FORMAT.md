# CSV Data Format

This document defines the CSV format for manuscript artifact data files.

---

## Required columns

Every CSV in `artifact_data_files/` must contain these three columns:

| Column | Type | Description |
|---|---|---|
| `artifact_name` | string | Unique name for the artifact |
| `symbol_sequence` | string | Comma-separated list of symbol names |
| `has_36_phase_structure` | integer (`0` or `1`) | Whether the artifact encodes a 36-phase structure |

---

## Optional columns (improve classification accuracy)

| Column | Type | Example values |
|---|---|---|
| `origin` | string | `egyptian`, `celtic`, `mayan`, `chinese`, `hellenistic` |
| `layout` | string | `circular`, `linear`, `grid`, `zodiac`, `spiral` |
| `symbol_type` | string | `gods`, `decans`, `months`, `plants`, `signs`, `glyphs` |
| `date_range` | string | `c. 50 BCE`, `Medieval`, `Unknown` |
| `source` | string | Citation or URL |

---

## Minimal example

```csv
artifact_name,symbol_sequence,has_36_phase_structure
Dendera_Zodiac,"Decan01,Decan02,Decan03,...,Decan36",1
```

## Full example

```csv
artifact_name,symbol_sequence,has_36_phase_structure,origin,layout,symbol_type,date_range,source
Dendera_Zodiac,"Decan01,Decan02,Decan03,...,Decan36",1,egyptian,circular,decans,c. 50 BCE,Neugebauer & Parker 1960
```

---

## Symbol naming conventions

- Use consistent, descriptive names within a sequence: `Decan01`, not `D1`
- For repeated symbols, append a suffix such as `SAMONIOS_1`, `SAMONIOS_2`
- Avoid commas within symbol names, because commas are the delimiter
- Use ASCII characters only for maximum compatibility
- Gods and deity names should use the most common English transliteration

---

## Labeling `has_36_phase_structure`

Label `1` if the artifact:
- Encodes approximately 36 distinct astronomical or calendrical phases (±1 tolerance)
- Uses unique symbols for each phase, not a repeated smaller cycle

Label `0` if:
- The total symbol count is 36 but unique count is much lower, for example 12 months × 3 repeats
- The system encodes fewer than 35 or more than 38 distinct phases
- The sequence is random, control data, or from a non-calendrical system

**When in doubt**, open a GitHub issue using the **New Artifact** template.

---

## One artifact per file

Each CSV file should contain data for one artifact. Multi-row CSVs, one row per artifact, are also accepted, but one-per-file is preferred for clarity and git diff readability.

---

## File naming

Name files after the artifact using underscores:

```text
Dendera_Zodiac_36.csv
Coffin_A1C_Decans.csv
Chinese_28_Lunar_Mansions.csv
```
