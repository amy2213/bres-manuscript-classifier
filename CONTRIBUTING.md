# Contributing to BRES Manuscript Classifier

Thank you for your interest in contributing.

This project sits at the intersection of symbolic manuscript analysis, archaeoastronomy, and computational classification. Contributions are welcome from technical, historical, and interdisciplinary backgrounds.

---

## Ways to contribute

### 1. Add new artifact datasets

This is the highest-value contribution.

Before submitting:
- Review `docs/CSV_FORMAT.md`
- Ensure consistent symbol naming and formatting
- Open a **New Artifact** issue to discuss classification and labeling

Well-labeled datasets directly improve classifier accuracy and coverage.

---

### 2. Improve feature engineering

The classifier currently uses a rule-based scoring system.

Areas for improvement include:
- GCD alignment logic
- Entropy and recurrence metrics
- Positional and sequential pattern detection (for example, bigrams and n-grams)
- Cycle detection for irregular symbolic systems

---

### 3. Expand classification types

New structural systems can be added to `CALENDAR_SIGNATURES` in `classifier_multi_label.py`.

Each new type should include:
- Expected unique symbol range
- GCD alignment targets
- Optional context hints such as `origin`, `layout`, and `symbol_type`

---

### 4. Fix bugs

- Check existing issues labeled `bug`
- Include reproducible steps
- Add or update tests when fixing behavior

---

### 5. Improve test coverage

Tests are located in `tests/test_classifier.py`.

When adding:
- New artifact types, include integration tests
- New features, include unit tests
- API changes, include endpoint tests

---

## Development setup

```bash
git clone https://github.com/amy2213/bres-manuscript-classifier.git
cd bres-manuscript-classifier

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest tests/ -v
```

---

## Pull request checklist

Before submitting a pull request:

- [ ] Tests pass locally (`pytest tests/ -v`)
- [ ] New features include tests
- [ ] New datasets follow `docs/CSV_FORMAT.md`
- [ ] Code is formatted with `black` and `isort`
- [ ] The pull request clearly explains what changed and why

---

## Data labeling guidance

### `has_36_phase_structure`

Use `1` if:
- The system encodes approximately 36 distinct symbolic phases (±1 tolerance)
- Each phase is represented by a unique symbol

Use `0` if:
- The sequence repeats a smaller cycle such as 12 × 3 = 36 total but only 12 unique symbols
- The structure does not represent a true 36-phase system

If uncertain:
- Open a **New Artifact** issue before labeling

---

## Code standards

- Python 3.8+
- Format with `black`
- Sort imports with `isort`
- Use docstrings for public functions
- Avoid bare `except:` blocks

---

## Project philosophy

- This system detects **structural similarity**, not confirmed historical meaning
- Classification outputs are **research signals**, not final conclusions
- Reproducibility and clarity are prioritized over unnecessary complexity

---

## Questions

Open a GitHub Discussion or contact:

Amy Laird  
dataweaver22@gmail.com
