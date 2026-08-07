---
title: "Status ingestie — HTML batch 2026-08-07"
type: status
tags: [status, ingestie, meta]
created: 2026-08-07
updated: 2026-08-07
---

# Status ingestie — HTML batch 2026-08-07

Five legis.md HTML dumps dropped into the agent upload zone. Mapping and disposition:

| doc_id | Act | Disposition |
|---|---|---|
| `152955` | **Legea nr. 1593/2002** — AOAM premiums | ✅ `(text)` + `(notă)` · [[Concept — Prima AOAM]] · [[CNAM]] stub · wired into [[MOC — Fiscalitate & Contabilitate]] |
| `153011` | **Legea nr. 271/2017** — statutory audit | ✅ `(text)` + `(notă)` · [[Concept — Audit statutar]] · closes horizon P2 primary gap |
| `153667` | **Legea nr. 41/2026** — business-support omnibus | ✅ `(text)` + `(notă)` · concepts [[Concept — Retragere asociat SRL]] · [[Concept — Garanție de bună execuție]] · wired into fiscal / companies / procurement MOCs |
| `152862` | **Codul fiscal nr. 1163/1997** | ♻️ source refresh only — Titluri I–X already in vault under same doc_id |
| `152737` | **Legea nr. 489/1999** | 📦 archived as older consolidation — working text stays `155453` |

## Analysis layer produced
- 3 Law House `(notă)` companions
- 4 concepts
- 1 authority stub ([[CNAM]])
- Updates: [[SOURCE INDEX]] · [[Fiscalitate — synthesis]] · [[Contabilitate & raportare financiară — synthesis]] · [[Fiscalitate & Contabilitate — horizon and gaps]] · Home

## Still open after this batch
- Law **1585/1998** (AOAM parent) + annual AOAM funds laws
- L131/2015 full text (Art. 68 already patched via L41)
- CSPA authority profile + secondary audit acts
- CNAS authority profile

## Script
`scripts/ingest_legis_batch_2026_08_07.py`
