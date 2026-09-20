# Privy

Policy-driven PII/secrets scrubber that sits in front of every LLM call and every log write.

LLM applications have **two** data-governance surfaces: what goes *to* the model, and what gets
*written down about* the interaction (logs, traces, vector stores). Privy scans both directions,
applies a per-destination policy, and writes an audit trail that lets a reviewer answer
"why was this SSN allowed through?" from the log alone.

Privy does **not** reinvent detection. It wraps [Microsoft Presidio](https://github.com/microsoft/presidio)
(PII, NER via spaCy) and [detect-secrets](https://github.com/Yelp/detect-secrets) (credentials),
and adds the parts those tools don't provide: the policy engine, bidirectional middleware,
audit log, and an evaluation harness that proves the numbers.

## Quick start

```bash
uv sync --all-groups
uv run python -m spacy download en_core_web_lg   # NER model (~600 MB)
uv run pytest
```

```python
import privy

guard = privy.Guard.from_policy("policies/default.yaml")

with guard.inbound() as scrub:
    prompt = scrub("Call John Smith at 555-123-4567, SSN 123-45-6789")
    # -> "Call <PERSON> at <PHONE_NUMBER>, SSN <US_SSN>"  (or BlockedError, per policy)
```

## Project layout

```
src/privy/          library code
  detect/           detection layer (Presidio + detect-secrets wrappers, custom recognizers)
  policy/           policy schema, loader, decision engine
  middleware/       inbound / outbound / storage hooks, decorator + context manager
  audit/            structured audit log (SQLite)
policies/           shipped YAML policies
tests/              unit + integration tests
eval/               eval datasets, harness, reports (ship gate)
docs/               ADRs, architecture, eval reports  (not tracked in git — see important_notes.md)
```

## Documentation

See [docs/README.md](docs/README.md) for the documentation index, including
architecture decision records under `docs/adr/`.

## License

MIT
