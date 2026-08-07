---
title: "Status ingestie — PDF batch 2026-08-07 (6)"
type: reference
domeniu: [meta, energetică]
tags: [reference, meta, ingestion, pdf]
created: 2026-08-07
updated: 2026-08-07
---

# PDF batch 2026-08-07 (6) — ingestion status

Script: `scripts/ingest_energy_pdf_batch_2026_08_07g.py`.

| doc_id | Act | Status |
|---|---|---|
| `152035` | [[HG 1060-2023 — organizare functionare CNED (text)\|HG 1060/2023]] | ✅ statute/structure · ⚠️ annex 4 may truncate |
| `152132` | [[HANRE 23-2017 — furnizarea energiei termice (text)\|HANRE 23/2017]] | ✅ body (~175 pts) · ⚠️ form annexes missing |
| `152152` | [[HANRE 785-2025 — modificare Metodologie tarife distributie gaze 443-2020 (text)\|HANRE 785/2025]] | ✅ complete · IF **1.01.2026** · parent decision now in [[Status ingestie — PDF batch 2026-08-07 (7)|(7)]] · annex still ❌ |
| `150832` | [[HG 599-2025 — limite cote capacitate regenerabile pana 2030 (text)\|HG 599/2025]] | ✅ dispositif · ⚠️ **annexes 1–2 missing** · abrogates HG 401 |
| `150858` | [[HG 517-2024 — Regulament constructie reconstructie centrale electrice (text)\|HG 517/2024]] | ✅ complete · patched by HG 596 |
| `150977` | [[HG 620-2025 — transmitere bunuri Fond eficienta energetica CNED (text)\|HG 620/2025]] | ✅ body · ⚠️ form annexes missing |

## Priority follow-up

1. **HG 599 annexes** (quota / net-billing numbers)
2. **HANRE 443 methodology annex** (decision ingested in batch 7)
3. Re-fetch HG 1060 annex 4; HANRE 23 form annexes
