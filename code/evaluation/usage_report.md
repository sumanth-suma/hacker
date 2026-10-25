# Usage report

## Final full-dataset generation

Run on 2026-10-24 with `python code/main.py`. The run produced the repository-root `output.csv` with 518 rows.

| Provider / model | Calls | Input tokens | Output tokens | Estimated cost |
| --- | ---: | ---: | ---: | ---: |
| None — deterministic local Python parser | 0 | 0 | 0 | $0.00 |
| Overall | 0 | 0 | 0 | $0.00 |

Average model tokens per request: 0 input and 0 output. Average model cost per request: $0.00.

The agent is evidence-driven: it resolves current and historical identifiers, reads timestamped participant-facing JSON, SQL, and log evidence, and applies `deletion_rules.csv`. No API credentials, hosted-model calls, or hidden data were used in the generation run.

## 2026-10-25 final generation update

Executed `python code/main.py` after the structured SQL evidence upgrade. The run produced `output.csv` with 518 rows and valid JSON arrays. It used no hosted-model calls: 0 input tokens, 0 output tokens, and estimated cost $0.00.

The final 2026-10-25 regeneration used the bundled local Python runtime with `pypdf` for PDF evidence extraction. It made no hosted-model calls and incurred no token or API cost.
