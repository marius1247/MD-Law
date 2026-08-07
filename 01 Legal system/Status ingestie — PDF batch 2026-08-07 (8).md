---
title: "Status ingestie — PDF batch 2026-08-07 (8)"
type: reference
domeniu: [meta, energetică]
tags: [reference, meta, ingestion, pdf]
created: 2026-08-07
updated: 2026-08-07
---

# PDF batch 2026-08-07 (8) — ingestion status

Script: `scripts/ingest_energy_pdf_batch_2026_08_07i.py`.

| doc_id | Act | Status |
|---|---|---|
| `154839` | [[HG 668-2022 — stocuri securitate gaze naturale (text)\|HG 668/2022]] | ✅ consolidated · **56.3 mcm** (HG 299/2026) |
| `154418` | [[HG 852-2024 — zone protectie retele electrice (text)\|HG 852/2024]] | ✅ Regulament body · ⚠️ form annexes missing |
| `154133` | [[Legea 74-2024 — actiuni climatice (text)\|LP74/2024]] | ✅ + annexes · patched by LP53 |
| `155406` | [[Legea 75-2026 — cadru institutii publice (text)\|LP75/2026]] | ✅ peripheral · IF **1.01.2027** |
| `154422` | [[Legea 105-2024 — Retea date durabilitate agricola (text)\|LP105/2024]] | ✅ peripheral (agriculture) |
| `155290` | HG 346/2026 | **archived only** — duplicate of vault legis_id `155511` |

## Priority follow-up

1. Ingest **HG 299/2026** (stocks volume amend)
2. HG 852 form annexes; **HG 248/2026** (852 enabling remap)
3. Prior annex gaps (443 methodology, HG 599, PNIEC, QoS)
