# Changelog

All notable changes to BRES Manuscript Classifier are documented here.

The format follows Keep a Changelog, and this project uses semantic versioning where practical.

---

## [0.2.0] — 2025-07-13

### Added
- Multi-label classifier replacing the original binary `has_36_phase_structure` output
- 8 detectable calendar types: 36-phase decan, 12-month solar, lunar mansion (28), lunisolar 18-month, zodiacal 12, ritual 260-day, herbal/botanical, synodic lunar
- Rule-based classification engine with transparent confidence scoring and human-readable reasons
- GCD alignment feature: checks symbol counts against 12, 13, 18, 20, 28, 29, 30, 36, 260
- Herbal keyword detection feature
- Context inputs: origin, layout, symbol_type now feed into scoring
- Flask REST API (`api.py`) with 4 endpoints: `/health`, `/calendar-types`, `/classify`, `/classify/batch`
- Batch classification endpoint supporting up to 50 manuscripts per request
- 84-test pytest suite covering unit, integration, and API layers
- 4 new artifact datasets: `Coffin_A1C_Decans.csv`, `Coffin_Star_Clock_Variation.csv`, `Maya_Tzolkin_260.csv`, `Chinese_28_Lunar_Mansions.csv`
- `flask-cors` support for cross-origin requests from the web UI
- `requirements-dev.txt` with testing and code quality tools

### Fixed
- `calc_additional_features()` unnamed Series columns causing wrong column names after concat
- `calc_astronomical_alignment()` called per-row; now uses `lru_cache` to avoid redundant computation
- Hardcoded `2025-01-01` anchor date in astronomical feature flagged for later replacement tied to artifact dates
- Empty input folder crash; now raises `ValueError` with a clear message
- Missing required column validation added for each CSV

### Changed
- Classifier now runs rule-based layer first; ML layer reserved for when dataset reaches 50+ samples
- CLI restructured into `folder` and `single` subcommands

---

## [0.1.0] — 2025-07-13

### Added
- Initial binary classifier detecting `has_36_phase_structure` in CSV symbol sequences
- Feature extraction: total/unique symbol counts, entropy, phase gap standard deviation, dominant cycle length
- Astronomical alignment scoring via Astropy (`get_sun`, `AltAz`)
- Random Forest classifier (scikit-learn)
- CLI via argparse using `--input_folder`, `--location`, and `--output_file`
- 6 initial artifact datasets: Dendera Zodiac, Egyptian Decans Extended, Book of Nut, Coligny Calendar, 18-Month Lunar Cycle, Random Symbol Text
