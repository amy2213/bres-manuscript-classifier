# API Reference

The BRES Manuscript Classifier Flask API exposes four endpoints for classifying manuscript sequences programmatically.

## Base URL

```text
http://localhost:5000
```

Start the server with:

```bash
python api.py --host 0.0.0.0 --port 5000 --debug
```

---

## Endpoints

### GET /health

Returns service status. Use this to verify the API is running before sending classification requests.

**Response 200**

```json
{
  "ok": true,
  "status": "healthy",
  "version": "0.2.0",
  "calendar_types_supported": 8,
  "timestamp": "2025-07-13T20:00:00+00:00"
}
```

---

### GET /calendar-types

Returns the full list of calendar types the classifier can detect, including their expected symbol ranges, GCD targets, and context hints.

**Response 200**

```json
{
  "ok": true,
  "calendar_types": [
    {
      "id": "36_phase_decan",
      "description": "36-phase decan / star calendar (Egyptian-style)",
      "unique_symbol_range": [35, 38],
      "gcd_targets": [36],
      "layout_hints": ["circular", "zodiac"],
      "origin_hints": ["egyptian", "hellenistic", "greek"],
      "symbol_type_hints": ["gods", "stars", "decans"]
    }
  ]
}
```

---

### POST /classify

Classify a single manuscript sequence.

**Request body**

```json
{
  "sequence": "Decan01,Decan02,...,Decan36",
  "artifact_name": "Dendera Zodiac",
  "origin": "egyptian",
  "layout": "circular",
  "symbol_type": "decans"
}
```

| Field | Required | Description |
|---|---|---|
| `sequence` | Yes | Comma-separated symbol string |
| `artifact_name` | No | Human-readable name (default: `"Unknown Artifact"`) |
| `origin` | No | Cultural origin; improves accuracy |
| `layout` | No | Physical layout: `circular`, `linear`, `grid`, `zodiac`, `spiral` |
| `symbol_type` | No | Symbol type: `gods`, `decans`, `months`, `plants`, `signs`, etc. |

**Response 200**

```json
{
  "ok": true,
  "timestamp": "2025-07-13T20:00:00+00:00",
  "artifact_name": "Dendera Zodiac",
  "features": {
    "total_symbol_count": 36,
    "unique_symbol_count": 36,
    "repeated_symbol_ratio": 0.0,
    "unique_symbol_ratio": 1.0,
    "symbol_entropy_score": 5.169925,
    "phase_gap_std": 0.0,
    "dominant_cycle_length": 0,
    "herbal_score": 0.0,
    "gcd_match_12": 1,
    "gcd_match_36": 1,
    "ctx_egyptian": 1,
    "ctx_circular": 1
  },
  "classifications": [
    {
      "type": "36_phase_decan",
      "description": "36-phase decan / star calendar (Egyptian-style)",
      "confidence": 1.0,
      "reasons": [
        "36 unique symbols in expected range 35-38",
        "GCD alignment with 36",
        "Origin matches (egyptian)",
        "Layout matches (circular)",
        "Symbol type matches (decans)"
      ]
    }
  ]
}
```

**Response 400** — missing or empty sequence

```json
{
  "ok": false,
  "error": "'sequence' is required and must not be empty.",
  "timestamp": "2025-07-13T20:00:00+00:00"
}
```

**curl example**

```bash
curl -X POST http://localhost:5000/classify \
  -H "Content-Type: application/json" \
  -d '{
    "sequence": "Decan01,Decan02,Decan03,Decan04,Decan05,Decan06,Decan07,Decan08,Decan09,Decan10,Decan11,Decan12,Decan13,Decan14,Decan15,Decan16,Decan17,Decan18,Decan19,Decan20,Decan21,Decan22,Decan23,Decan24,Decan25,Decan26,Decan27,Decan28,Decan29,Decan30,Decan31,Decan32,Decan33,Decan34,Decan35,Decan36",
    "artifact_name": "Dendera Zodiac",
    "origin": "egyptian",
    "layout": "circular",
    "symbol_type": "decans"
  }'
```

---

### POST /classify/batch

Classify up to 50 sequences in a single request. Items that fail validation are recorded in `errors` without stopping the rest of the batch.

**Request body**

```json
{
  "manuscripts": [
    {
      "sequence": "Decan01,Decan02,...,Decan36",
      "artifact_name": "Dendera Zodiac",
      "origin": "egyptian",
      "layout": "circular",
      "symbol_type": "decans"
    },
    {
      "sequence": "Aries,Taurus,Gemini,...,Pisces",
      "artifact_name": "Hellenistic Zodiac",
      "origin": "hellenistic",
      "layout": "zodiac",
      "symbol_type": "signs"
    }
  ]
}
```

**Response 200**

```json
{
  "ok": true,
  "timestamp": "2025-07-13T20:00:00+00:00",
  "total": 2,
  "classified": 2,
  "failed": 0,
  "results": [{ "...classify result..." }, { "...classify result..." }],
  "errors": []
}
```

**Response when some items fail**

```json
{
  "ok": true,
  "total": 3,
  "classified": 2,
  "failed": 1,
  "results": ["...", "..."],
  "errors": [
    { "index": 2, "error": "'sequence' is required and must not be empty." }
  ]
}
```

**Limits**
- Maximum 50 manuscripts per request
- Requests exceeding this return HTTP 400

---

## Error responses

All error responses follow the same envelope:

```json
{
  "ok": false,
  "error": "Human-readable error message",
  "timestamp": "2025-07-13T20:00:00+00:00"
}
```

| Status | Meaning |
|---|---|
| 400 | Bad request; missing fields, invalid JSON, or exceeded batch limit |
| 404 | Endpoint not found |
| 405 | Method not allowed for this endpoint |
| 500 | Internal server error during classification |

---

## Python client example

```python
import requests

BASE = "http://localhost:5000"

resp = requests.post(f"{BASE}/classify", json={
    "sequence": "Decan01,Decan02,...,Decan36",
    "artifact_name": "Dendera Zodiac",
    "origin": "egyptian",
    "layout": "circular",
    "symbol_type": "decans",
})

data = resp.json()
for c in data["classifications"]:
    print(f"{c['type']}: {c['confidence'] * 100:.0f}%")
    for r in c["reasons"]:
        print(f"  • {r}")
```
