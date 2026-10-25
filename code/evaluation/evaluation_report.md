# Evaluation report

## Executed public-sample evaluation

Run on 2026-10-24 with `python code/main.py --requests dataset/sample_deletion_requests.csv --output sample_predictions.csv`.

| Metric | Result |
| --- | ---: |
| Cases | 32 |
| Status accuracy | 21 / 32 (65.6%) |
| Exact row / sequence accuracy | 0 / 32 (0.0%) |
| JSON-array validity | 32 / 32 (100%) |

The exact-row score compares deletion status and the parsed `steps_json` array. It is deliberately reported as zero rather than presenting schema validity as correctness.

## Additional deterministic tests

`python code/test_main.py -v` passed 3/3 tests:

1. A historical request email resolves to the same stable subject.
2. An export-only request is not treated as deletion authorization.
3. A permanent deletion request is authorized.

## Failures found and improvements made

The first run revealed a Windows SQLite temporary-file error; SQL snapshots now execute in an in-memory database. It also revealed that repeated SQL parsing would be expensive, so the engine now requires a matched resolved identifier before parsing an artifact. Remaining sample misses are primarily artifacts in PNG/PDF evidence, richer policy context (retained security records and tombstones), and verification planning for records not directly observed. The current output is schema-valid but needs those extensions before it should be treated as a high-accuracy submission.

## 2026-10-25 SQL evidence candidate update

This executed evaluation supersedes the earlier metrics. The protected source scored 21/32 rather than the claimed 22/32; it is retained under `protected_baselines/current_21_32/`.

| Metric | Protected baseline | Current candidate |
| --- | ---: | ---: |
| Status accuracy | 21/32 | 25/32 |
| Exact rows / sequences | 0/32 | 1/32 |
| Step matches / predicted / expected | not measured | 23 / 179 / 193 |
| Step precision / recall | not measured | 12.8% / 11.9% |
| Position-aligned fields | not measured | 462 / 1,253 |

The candidate decodes SQL `record_json`, honors `origin_system`, recursively matches nested identity values, and caches parsed SQL snapshots. It fixed cases 16, 22, 24, and 26 without status regressions. Generalized tests cover `account_005`, `account_994`, `analytics_4440`, and `tombstone_3745`. Remaining status misses are 03, 07, 10, 13, 15, 28, and 31.

## 2026-10-25 trace and PDF evidence update

The current promoted candidate adds strict trace-scoped terminal-event reduction and cached PDF text extraction for support attachment evidence. It was evaluated with the bundled local runtime containing `pypdf`.

| Metric | Prior promoted candidate | Current candidate |
| --- | ---: | ---: |
| Status accuracy | 25/32 | 27/32 |
| Exact JSON rows | 1/32 | 1/32 |
| Exact step overlap | 23/193 | 25/193 |
| Unit tests | 3/3 | 3/3 |

The trace reducer fixed case 15 without regression, and generalized PDF support-record extraction fixed case 07 without regression. Remaining status misses are cases 03, 10, 13, 28, and 31.
