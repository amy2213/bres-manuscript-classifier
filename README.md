# BRES Manuscript Classifier

A multi-label classification framework for detecting structural patterns in symbolic manuscripts.

Designed for researchers working across archaeoastronomy, digital humanities, manuscript analysis, and computational pattern recognition.

---

## What it does

Given a comma-separated sequence of symbols and optional manuscript metadata, the BRES Manuscript Classifier estimates which known structural system the sequence most closely matches.

It returns:
- Predicted structural classifications
- Confidence scores for each match
- Human-readable explanations describing why each classification was triggered

This system focuses on **structural pattern detection**, not linguistic translation.

---

## Supported classification types

| Type | Example Artifact | Key Signature |
|------|------------------|---------------|
| 36-phase decan | Dendera Zodiac, Coffin Texts | ~36 unique symbols |
| 12-month solar | Roman, Babylonian calendars | 12 unique symbols, cyclical |
| Lunar mansion (28) | Chinese XiÃ¹, Arabic ManÄzil | 28 unique symbols |
| Lunisolar 18-month | Coligny Calendar | 18 unique symbols |
| Zodiacal 12 | Hellenistic zodiac | 12 signs, circular layout |
| Ritual 260-day | Maya Tzolkin | 13Ã20 structure |
| Herbal / botanical | Medieval herbals, Voynich | Plant keyword density |
| Synodic lunar | Babylonian, Hebrew systems | 29â30 unit cycles |

---

## Quick start

### Clone the repository
```bash
git clone https://github.com/amy2213/bres-manuscript-classifier.git
cd bres-manuscript-classifier
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Classify a folder of CSV files
```bash
python classifier_multi_label.py folder \
  --input_folder ./artifact_data_files \
  --output_file results.csv
```

### Classify a single sequence
```bash
python classifier_multi_label.py single \
  --sequence "Decan01,Decan02,...,Decan36" \
  --name "Dendera Zodiac" \
  --origin egyptian \
  --layout circular \
  --symbol_type decans
```

### Optional CLI command
After installing the package, you can also run:

```bash
bres-classifier single \
  --sequence "Decan01,Decan02,...,Decan36" \
  --name "Dendera Zodiac" \
  --origin egyptian \
  --layout circular \
  --symbol_type decans
```

### Run the API
```bash
python api.py --host 0.0.0.0 --port 5000 --debug
```

---

## Example output

```json
{
  "artifact_name": "Dendera Zodiac",
  "predictions": [
    {
      "label": "36-phase decan",
      "confidence": 0.94,
      "explanation": "Sequence contains approximately 36 distinct recurring symbols and circular layout metadata consistent with decanal systems."
    },
    {
      "label": "zodiacal 12",
      "confidence": 0.41,
      "explanation": "Partial cyclical overlap with 12-sign systems, but weaker structural alignment."
    }
  ]
}
```

---

## Project structure

```text
bres-manuscript-classifier/
âââ classifier_multi_label.py
âââ api.py
âââ requirements.txt
âââ requirements-dev.txt
âââ setup.py
âââ .gitignore
âââ LICENSE
âââ CONTRIBUTING.md
âââ CHANGELOG.md
âââ artifact_data_files/
âââ docs/
â   âââ API.md
â   âââ CSV_FORMAT.md
â   âââ FEATURES.md
âââ .github/
    âââ ISSUE_TEMPLATE/
    â   âââ bug_report.md
    âââ workflows/
        âââ ci.yml
```

---

## CSV data format

Required columns:
```text
artifact_name, symbol_sequence, has_36_phase_structure
```

Optional columns:
```text
origin, layout, symbol_type
```

See `docs/CSV_FORMAT.md` for full specification.

---

## API

Start the server:
```bash
python api.py --host 0.0.0.0 --port 5000
```

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | /health | Service status |
| GET | /calendar-types | Available classification types |
| POST | /classify | Classify a sequence |
| POST | /classify/batch | Classify multiple sequences |

See `docs/API.md` for full details.

---

## Research use cases

- Compare unknown manuscripts against known structural systems
- Detect cyclical or phase-based symbolic patterns
- Screen datasets for astronomical or calendrical structures
- Support digital humanities workflows with reproducible classification

---

## Limitations

- Detects structural similarity, not confirmed meaning or translation
- Results depend on input quality and encoding
- Incomplete or ambiguous data may reduce confidence
- Some systems may overlap in classification

---

## Contributing

Contributions are welcome. See `CONTRIBUTING.md` for guidelines.

---

## License

MIT License â see `LICENSE`

---

## Contact

Amy Laird  
dataweaver22@gmail.com
