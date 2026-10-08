# Contributing

Contributions are welcome when they preserve the project's evidence discipline.

## Requirements

- Add or update tests for behavioral changes.
- Use synthetic or independently redistributable fixtures.
- Classify material claims as PROVEN, STRONGLY SUPPORTED, HYPOTHESIS, or INCONCLUSIVE.
- State scope and limitations for every PROVEN claim.
- Keep physical encoding separate from semantic regeneration.
- Fail closed for unsupported mappings and ambiguous inputs.

## Do not submit

- proprietary binaries or executable images;
- raw memory dumps or runtime captures;
- customer designs or private datasets;
- credentials, tokens, or private keys;
- local absolute paths;
- target-derived lookup tables presented as native semantics;
- unsupported claims that native serialization is complete or production-ready.

## Development

```bash
python -m pip install -e ".[dev]"
python -m pytest -q
python -m ruff check .
```

## Pull requests

Explain the evidence source, expected failure mode, tests, limitations, and whether the change affects only physical encoding, a synthetic model, or a source-derived semantic claim.
