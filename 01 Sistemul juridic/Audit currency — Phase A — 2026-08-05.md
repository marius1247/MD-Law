---
title: "Audit currency — Phase A — 2026-08-05"
type: reference
domeniu: [meta]
tags: [reference, meta, audit, currency]
created: 2026-08-05
updated: 2026-08-05
status: reviewed
---

# Cross-domain currency audit — Phase A (non-energy MOCs)

**Scope:** Every act listed in [[MOC — Societăți & Guvernanță corporativă]], [[MOC — Fiscalitate & Contabilitate]], [[MOC — Drept comercial]], [[MOC — Drept civil]], [[MOC — Achiziții publice & Statul]], and [[MOC — Proceduri]] — plus keystone codes ingested outside those hubs.

**Method:** Vault text `MODIFICAT` / `ABROGAT` headers, frontmatter `legis_id`, cross-check against [[Roadmap]] watch list and EU-alignment projects. **legis.md live API was not reachable** from this environment (Cloudflare block on `downloadpdf` / `getResults`) — consolidation dates in vault must be re-verified manually on [legis.md](https://www.legis.md) before operational citation.

**Related:** [[Audit L164 transition — HANRE 283-169-423 — 2026-08-05]] · [[Status ingestie — Energetica]] · [[Roadmap]]

---

## Executive summary

| Verdict | Count | Meaning |
|---|---:|---|
| ✅ **Vault consolidation looks current** | 12 keystone acts | `MODIFICAT` header matches known 2025–26 amendments in text |
| ⚠️ **Current but forward-dated change** | 4 acts | Amendment in vault; entry into force still future |
| ⚠️ **Missing `legis_id` in frontmatter** | 28 upload-sourced acts | Text ingested; metadata not yet wired for Dataview |
| ❌ **Not in vault** | 2 critical | L131/2015 general procurement; L845/1992 entrepreneurship (legacy) |
| ❌ **Truncated text** | 0 in non-energy scope | Energy truncations tracked separately |

**Bottom line:** Non-energy hubs are **not silently repealed** like L107/2016 was — but several carry **EU-accession amendment layers** and **one keystone procurement act is still missing**. Treat every MOC inventory as **verified through headers, not through hub prose**.

---

## Per-hub findings

### [[MOC — Societăți & Guvernanță corporativă]]

| Act | Vault | `legis_id` | Currency signal | Status |
|---|---|---|---|---|
| [[Legea 135-2007 — SRL (text)]] | ✅ | 153674 | `LP41/2026` in header (27.03.26) | ✅ Current |
| [[Legea 1134-1997 — societati pe actiuni (text)]] | ✅ | 154811 | EU company-law amendments in header | ⚠️ Track SA remuneration file (Roadmap) |
| [[Legea 220-2007 — inregistrarea de stat (text)]] | ✅ | 155438 | `MODIFICAT` present | ✅ Verify on legis before cite |
| [[Legea 149-2012 — insolvabilitate (text)]] | ✅ | 152605 | `MODIFICAT` present | ✅ Verify on legis |
| [[Codul civil 1107-2002 — text — Cartea I]] | ✅ | 149719 | `LP76/2026` markers — **in force 01.01.2027** | ⚠️ Forward-dated reform in text |
| L845/1992 entrepreneurship | ❌ | — | Slated **full repeal** (project 345/MDED/2025) | ❌ Not ingested; still cited in L135/2007 art. 1(2) |

### [[MOC — Fiscalitate & Contabilitate]]

| Act | Vault | `legis_id` | Currency signal | Status |
|---|---|---|---|---|
| [[Codul fiscal 1163-1997 (text) — Index]] | ✅ | 152862 | Titluri I–X; annual fiscal-policy vehicle | ⚠️ Re-verify each January |
| [[Legea 287-2017 — contabilitate (text)]] | ✅ | 154725 | `MODIFICAT`; EU directive refs | ✅ |
| [[Legea 86-2026 — modificare Legea contabilitatii (text)]] | ✅ | 154710 | **In force 01.01.2027** — threshold reset | ⚠️ Forward-dated |
| [[Codul vamal 95-2021 (text)]] | ✅ | 149774 | `MODIFICAT`; EU customs code refs | ✅ |
| Fiscal Code rewrite (MF concept) | — | — | Roadmap watch item | 🔭 Monitor |

### [[MOC — Drept comercial]]

| Act | Vault | `legis_id` | Currency signal | Status |
|---|---|---|---|---|
| [[Legea 183-2012 — concurenta (text)]] | ✅ | 121240 | EU competition alignment in header | ✅ |
| [[Legea 235-2006 — principii reglementare intreprinzator (text)]] | ✅ | 142654 | `_MODIFICAT_` | ✅ |
| [[Legea 160-2011 — reglementarea prin autorizare (text)]] | ✅ | 154478 | `MODIFICAT` | ✅ |
| [[Codul civil 1107-2002 — text — Cartea III]] | ✅ | 149719 | Same consolidation as Cartea I | ⚠️ LP76/2027 |
| Upload batch (banking, trade, transport…) | ✅ | mostly **missing** | Ingested 2026-07-28 | ⚠️ Add `legis_id` |
| State aid law | ❌ | — | MOC says verify number on legis | ❌ Not ingested |

### [[MOC — Drept civil]]

| Act | Vault | `legis_id` | Currency signal | Status |
|---|---|---|---|---|
| [[Codul civil 1107-2002 (text) — Index]] | ✅ | 149719 | Republicat 2019; LP76/2026 + LP187/2025 noted | ⚠️ LP76 from 01.01.2027 |
| All Cărți I–V | ✅ | 149719 | `text_complet: true` on splits | ✅ Completeness OK |

### [[MOC — Achiziții publice & Statul]]

| Act | Vault | `legis_id` | Currency signal | Status |
|---|---|---|---|---|
| **Legea 131/2015** general procurement | ❌ | — | MOC still marks ❌ to download | ❌ **Critical gap** |
| [[Legea 74-2020 — achizitii sectoriale (text)]] | ✅ | 155279 | EU directive amendment refs in header | ✅ |
| [[Legea 179-2008 — parteneriat public-privat (text)]] | ✅ | — | Upload ingest | ⚠️ Add `legis_id` |
| [[HG 773-2016 — Regulament achizitii interne (text)]] | ✅ | — | Internal procurement rules | ⚠️ Add `legis_id` |
| Concessions / implementing HG | partial | — | MOC: verify on legis | ⚠️ |

### [[MOC — Proceduri]]

| Act | Vault | `legis_id` | Currency signal | Status |
|---|---|---|---|---|
| [[Codul administrativ 116-2018 (text)]] | ✅ | 149723 | `MODIFICAT` | ✅ |
| [[Codul de procedura civila 225-2003 (text)]] | ✅ | 150766 | Long amendment list in header | ✅ |
| [[Codul de executare 443-2004 (text)]] | ✅ | 149721 | `_MODIFICAT_` | ✅ |
| [[Legea 23-2008 — arbitraj (text)]] | ✅ | 95607 | No recent `MODIFICAT` in header slice | ✅ stable |
| Upload procedure acts (L74/2025, L436, L136, L797, L1234) | ✅ | mostly **missing** | Ingested 2026-07-28 | ⚠️ Add `legis_id` |

### Foundations (all hubs)

| Act | Vault | `legis_id` | Status |
|---|---|---|---|
| [[Constituția RM — text]] | ✅ | 136130 | ⚠️ Roadmap: swap post-2024 `doc_id` when legis publishes |
| [[Legea 100-2017 — actele normative (text)]] | ✅ | 153007 | `LP327/2025` in header — meta-layer OK |

---

## EU-alignment & legislative movement (watch list)

| Item | Vault impact | Action |
|---|---|---|
| **Entrepreneurship law** replacing L845/1992 | [[Drept comercial — sinteza]] §2 | Track project 345/MDED/2025 |
| **L86/2026** accounting thresholds | [[Contabilitate & raportare financiară — sinteza]] | Flag clients before 01.01.2027 |
| **LP76/2026** civil code | Cartea I art. 307 etc. | Already in text; effective 01.01.2027 |
| **LP41/2026** SRL | L135/2007 | In vault header |
| **Fiscal / Customs Code rewrite** | Cod fiscal Titlu map | Monitor MF concept |
| **L131/2015** procurement | Achiziții hub empty | **Ingest next** (Phase B) |
| **Ministerul Energiei legal framework page** | External only | Still lists **L107/2016** — do not use as currency source |

---

## Metadata hygiene (structure)

1. **28 upload-sourced `(text)` files** lack `legis_id` / `legis_url` — frontmatter not Dataview-ready. Extract from `Uploads/*.md` or legis.md search.
2. **[[Constituția RM — text]]** and keystone codes share consolidation discipline — run annual `MODIFICAT` header scan after each 1 January fiscal package.
3. **MOC currency banners** on Achiziții, Proceduri, Drept civil — replace with link to **this audit** and `currency_checked` date after each pass.

---

## Recommended next actions (Phase B)

1. Ingest **Legea 131/2015** (general public procurement).
2. Batch-add `legis_id` to upload-ingested acts from `Uploads/` sources.
3. Re-run this audit after **manual legis.md consolidation check** for acts flagged ⚠️.
4. Ingest or archive **L845/1992** with explicit **superseded** banner until replacement law passes.

---

## See also

[[Audit L164 transition — HANRE 283-169-423 — 2026-08-05]] · [[Audit ingestie — 2026-07-26]] · [[Audit vault — Law House Knowledge Engine — 2026-07-28]] · [[00 - Index general]]
