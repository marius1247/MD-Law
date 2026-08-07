---
title: "Status ingestie — PDF batch 2026-08-07 (4)"
type: reference
domeniu: [meta, energetică]
tags: [reference, meta, ingestion, pdf]
created: 2026-08-07
updated: 2026-08-07
---

# PDF batch 2026-08-07 (4) — ingestion status

User-uploaded legis.md PDFs (`147685`, `147714`, `147716`, `147843`, `148066`). Script: `scripts/ingest_energy_pdf_batch_2026_08_07e.py`.

| doc_id | Act | Status |
|---|---|---|
| `147685` | [[HG 86-2025 — Plan national integrat energie clima 2025-2030 (text)\|HG 86/2025]] | ✅ text + note · ⚠️ **PNIEC annex missing** |
| `147714` | [[HG 156-2025 — modificare HG 1059-2023 PSO securitate EE (text)\|HG 156/2025]] | ✅ text + note · parent HG 1059/2023 ❌ |
| `147716` | [[HG 158-2025 — modificare norme cheltuieli institutii sociale (text)\|HG 158/2025]] | ✅ text + stub note · ⚠️ annex missing · **peripheral (social)** |
| `147843` | [[Legea 45-2025 — garantiile avizelor de racordare si tolerante dezechilibre (text)\|LP45/2025]] | ✅ text + note · concepts wired |
| `148066` | [[HG 197-2025 — metodologie cogenerare inalta eficienta garantii origine (text)\|HG 197/2025]] | ✅ text + note · ⚠️ **methodology annex missing** · HG 297 tables present |

## Concepts added / updated

- **New:** [[Concept — Garanție de bună execuție a avizului de racordare]] · [[Concept — Garanții de origine (cogenerare HE)]]
- **Updated:** [[Concept — Aviz de racordare]] · [[Concept — Producător eligibil]] · [[Concept — Garanție de bună execuție]] (cross-link)

## Priority follow-up

1. Fetch **PNIEC 2025–2030** full annex (HG 86)
2. Fetch **HE-CHP GO methodology** annex (HG 197)
3. Ingest parent **HG 1059/2023** (security PSO)
4. Optional: HG 297/2016 consolidated parent; social HG 520/2006 only if practice needs it
