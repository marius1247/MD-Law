---
title: "Status ingestie — Energetica"
type: reference
domeniu: [energetică, meta]
tags: [reference, meta, ingestion, data-quality]
created: 2026-07-22
updated: 2026-08-06
---

# Ingestion status — Energy corpus

**Read this before citing any energy text in this vault.** The core energy corpus has moved from "mostly partial" to **mostly complete** after manual browser downloads on 2026-07-23 and 2026-07-26. The remaining high-value hole is **HANRE 423/2019 electricity network code**, whose annex is still missing.

> [!danger] Legal-currency warning, not just a completeness warning
> [[Legea 107-2016 — energia electrica (text)|L107/2016]] was **repealed** on 19 August 2025 by [[Legea 164-2025 — energia electrica (text)|L164/2025]]. Many pre-2025 electricity HANRE acts were issued under L107 and now need currency checking against L164. Completeness is the *second* thing to check; **currency is the first**.

## ✅ Resolved by manual download — core laws

Manual browser downloads from legis.md bypassed the ~96 KB automated-fetch ceiling. These acts are now **complete** in the vault and no longer subject to the truncation caveat:

| Act | Source doc_id | Consolidation | Articles |
|---|---|---|---|
| [[Legea 164-2025 — energia electrica (text)]] | 152515 | incl. LP101/2026 | 151 |
| [[Legea 108-2016 — gazele naturale (text)]] | 151419 | incl. LP227/2025 (30.12.25) | 114 (+bis) |
| [[Legea 10-2016 — surse regenerabile (text)]] | 151418 | incl. LP227/2025 (30.12.25) | 45 (+bis) |
| [[Legea 139-2018 — eficienta energetica (text)]] | 148767 | incl. LP111/2025 (03.06.25) | 30 (+bis) |
| [[Legea 174-2017 — energetica (text)]] | 150492 | incl. LP236/2025 (12.09.25) | 42 numbered articles |
| [[Legea 92-2014 — energia termica si cogenerarea (text)]] | 151415 | incl. LP227/2025 (30.12.25) | 61 numbered articles |
| [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (text)]] | 3445 | — | short act, full |
| [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (text)]] | 155085 | new amending law | Art. I–V |

Also complete, because it is frequently needed for energy-law hierarchy/procedure work:

| Act | Source doc_id | Consolidation | Articles |
|---|---|---|---|
| [[Legea 100-2017 — actele normative (text)]] | 153007 | incl. LP327/2025 (31.12.25) | 79 + transitional art. 80 in text |

The manual browser-download route worked exactly as predicted: PDFs bypass the ~96 KB fetch ceiling. **Superscript "bis" articles** (e.g. art. 36¹) that pdftotext flattens to "361" were reconstructed during ingestion.

> [!note] Diacritics
> These files use the correct comma-below **ș/ț**; older vault files use cedilla ş/ţ. Cross-note article links may need the matching form.

## ✅ Resolved by manual download — ANRE regulations

These ANRE acts now have full text/annexes in the vault:

| Act | Status | Notes |
|---|---|---|
| [[HANRE 283-2020 — Regulile pietei energiei electrice (text)]] | ✅ complete annex | Amended by [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (text)]], in force 01.07.2026. Still issued originally under L107/2016 → currency check under L164/2025 |
| [[HANRE 420-2019 — Codul retelelor de gaze naturale (text)]] | ✅ complete annex | Amended by [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (text)]] and [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]] |
| [[HANRE 112-2019 — racordarea la retelele de gaze (text)]] | ✅ complete | Manual download complete |
| [[HANRE 113-2019 — furnizarea gazelor naturale (text)]] | ✅ complete | Manual download complete |
| [[HANRE 168-2019 — racordarea la retelele electrice (text)]] | ✅ complete but historical/superseded | Abrogated by [[HANRE 311-2026 — racordarea la retelele electrice (text)]] |
| [[HANRE 311-2026 — racordarea la retelele electrice (text)]] | ✅ complete | New L164-based connection regulation; flexible connection and capacity auction concepts |
| [[HANRE 626-2023 — Metodologie tarife transport EE (text)]] | ✅ complete | Replaces/abrogates [[HANRE 486-2017 — Metodologie tarife transport EE (text)|HANRE 486/2017]]; amended by [[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]] |

Other newly relevant amendment/transition acts now present:

- [[HANRE 177-2026 — modificarea unor hotarari ANRE (text)]] — omnibus ANRE amendment package; check for knock-on amendments before citing affected acts.

## ❌ Still incomplete / decision-only

| Act | Problem | Priority |
|---|---|---|
| [[HANRE 423-2019 — Codul retelelor electrice (text)]] | **decision-only; annex missing** | High. Still needed by [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] and technical connection/network-code analysis |
| [[HANRE 64-2018 — Metodologie tarife distributie EE (text)]] | likely annex/methodology completeness should be rechecked | Medium |
| [[HANRE 375-2017 — Metodologie tarife regenerabile (text)]] | likely annex/methodology completeness should be rechecked | Medium |
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)]] | earlier flagged as detached-annex risk | Medium |

## Electricity transition map — L107 to L164

| Old/current act | Current position |
|---|---|
| [[Legea 107-2016 — energia electrica (text)]] | **Abrogated** by [[Legea 164-2025 — energia electrica (text)]] on 19.08.2025; historical / legacy-project relevance only |
| [[HANRE 168-2019 — racordarea la retelele electrice (text)]] | **Abrogated** by [[HANRE 311-2026 — racordarea la retelele electrice (text)]] |
| [[HANRE 486-2017 — Metodologie tarife transport EE (text)]] | **Abrogated** by [[HANRE 626-2023 — Metodologie tarife transport EE (text)]] |
| [[HANRE 283-2020 — Regulile pietei energiei electrice (text)]] | Complete annex, amended 2026, but originally L107-based; check for L164 re-adoption/replacement |
| [[HANRE 423-2019 — Codul retelelor electrice (text)]] | Still decision-only; annex missing; originally L107-based |

## Limitation 1 — the ~96 KB fetch ceiling

> [!important] Diagnosed 2026-07-23 — this is a **hard tool ceiling, not a fixable bug**
> Automated retrieval of long legis.md PDFs stops around 96–105 KB. Re-fetching does not help; legis.md serves each act as one indivisible document and the HTML viewer is client-rendered. Manual browser download remains the reliable route.

This limitation has now been worked around for the highest-priority laws and several ANRE annexes. Keep using the manual download route for any remaining large acts.

## How to complete remaining annexes

1. Open the `legis_url` in the file's frontmatter in a normal browser.
2. Wait for the JS viewer to render, then use the site's own download control (PDF/DOC).
3. For ANRE annexes, also check [ANRE › Hotărâri](https://anre.md/acte-normative-3-18), which often hosts direct `.pdf`/`.doc` annexes.
4. Paste below frontmatter, keeping the header block.
5. Normalise headings enough for navigation; for ANRE point-numbered rules, preserve point numbering rather than forcing article anchors.
6. Set `text_complet: true`, update `continut`, `updated`, and add/update the companion `— notă`.

## Analysis layer status

New/updated analysis notes created on 2026-07-26:

- [[Legea 174-2017 — energetica (notă)]]
- [[Legea 92-2014 — energia termica si cogenerarea (notă)]]
- [[Legea 100-2017 — actele normative (notă)]]
- [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]]
- [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)]]
- [[HANRE 311-2026 — racordarea la retelele electrice (notă)]]
- [[HANRE 626-2023 — Metodologie tarife transport EE (notă)]]

**Batch 1 — deep Law House notes (2026-08-06)** — acts that had `(text)` but no `(notă)` / concepts:

- [[Legea 139-2018 — eficienta energetica (notă)]] ✅ complete text analysed
- [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (notă)]] ✅ amending package
- [[HG 820-2024 — situatii exceptionale electroenergetic (notă)]] ⚠️ dispositif-only (annex still missing)
- Concepts: [[Concept — Audit energetic]] · [[Concept — Contract de performanță energetică]] · [[Concept — Parte obligată (eficiență energetică)]] · [[Concept — Eficiența energetică înainte de toate]] · [[Concept — Situație de criză în domeniul petrolier]] · [[Concept — Situație excepțională electroenergetică]]
- Authority: [[CNED]]
- Remaining backlog: [[Analysis backlog — texts without notes]] (Batches 2–4)

Procedure/civil/procurement support notes also created because they are needed for energy disputes and contracts:

- [[Codul civil 1107-2002 (notă)]]
- [[Codul administrativ 116-2018 (notă)]]
- [[Legea 74-2020 — achizitii sectoriale (notă)]]

## Scope decision (deliberate)
Individual **tariff decisions and licences** were *not* ingested. ANRE issues these continuously; they date fast and would swamp the graph. Only structural acts — rules, codes, procedures, methodologies — are in scope. Current tariffs: [ANRE › Tarife în vigoare](https://anre.md/tarife-in-vigoare-3-204).

## Current priorities

1. Complete [[HANRE 423-2019 — Codul retelelor electrice (text)]] annex.
2. Re-check electricity HANRE acts for L164-based re-adoption/replacement.
3. Re-check distribution/renewables tariff methodology annex status.
4. Watch for a gas equivalent of [[Legea 164-2025 — energia electrica (text)|L164/2025]].
5. Keep amendment acts ([[HANRE 177-2026 — modificarea unor hotarari ANRE (text)]], [[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]], [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (text)]], [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (text)]], [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]]) linked from affected notes.

## See also
[[MOC — Energetică]] · [[Energetică — synthesis]] · [[Conventions]] · [[Roadmap]]
