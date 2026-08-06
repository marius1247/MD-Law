---
title: "Analysis backlog — texts without notes"
type: project
tags: [project, backlog, analysis]
created: 2026-08-06
updated: 2026-08-06
status: active
---

# Analysis backlog — `(text)` without `(notă)` / concepts

Audit of standalone working texts under `10 Legislation/` that lacked a companion `(notă)`. Non-standard: [[Legea 244-2024 — revizuirea Constituției (UE)]] (treaty/revision note — not a classic act pair).

**Starting set (2026-08-06):** 14 acts. **All four batches now have Law House notes.** Remaining work is annex completion / parent ingestion, not missing companions.

## Batch 1 — primary / crisis / security ✅

| Act | Note |
|---|---|
| [[Legea 139-2018 — eficienta energetica (text)]] | [[Legea 139-2018 — eficienta energetica (notă)]] |
| [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (text)]] | [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (notă)]] |
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)]] | [[HG 820-2024 — situatii exceptionale electroenergetic (notă)]] ⚠️ annex missing |

## Batch 2 — electricity market & supply ✅

| Act | Note |
|---|---|
| [[HANRE 169-2019 — furnizarea energiei electrice (text)]] | [[HANRE 169-2019 — furnizarea energiei electrice (notă)]] ⚠️ truncates pt. 146; L164 currency conflicts |
| [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (text)]] | [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (notă)]] · [[Concept — Piața organizată a contractelor bilaterale]] |
| [[HANRE 177-2026 — modificarea unor hotarari ANRE (text)]] | [[HANRE 177-2026 — modificarea unor hotarari ANRE (notă)]] *(gas 113/2019 + 363/2020)* |

## Batch 3 — tariff methodologies ✅

| Act | Note |
|---|---|
| [[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]] | [[HANRE 261-2026 — modificare Metodologie tarife transport EE (notă)]] |
| [[HANRE 64-2018 — Metodologie tarife distributie EE (text)]] | [[HANRE 64-2018 — Metodologie tarife distributie EE (notă)]] ⚠️ annex missing |
| [[HANRE 375-2017 — Metodologie tarife regenerabile (text)]] | [[HANRE 375-2017 — Metodologie tarife regenerabile (notă)]] ⚠️ annex missing |
| [[HANRE 486-2017 — Metodologie tarife transport EE (text)]] | [[HANRE 486-2017 — Metodologie tarife transport EE (notă)]] *(abrogated — historic)* |

## Batch 4 — gas corridor, water, rectificare ✅

| Act | Note |
|---|---|
| [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (text)]] | [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (notă)]] |
| [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]] | [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (notă)]] · [[Concept — Capacitate condiționată]] |
| [[HANRE 169-2025 — investitii apa si canalizare (text)]] | [[HANRE 169-2025 — investitii apa si canalizare (notă)]] |
| [[Rectificare ANRE 05-03-5694-2025 (text)]] | [[Rectificare ANRE 05-03-5694-2025 (notă)]] |

## Batch 5 — parent ingest + stub deepen (2026-08-06) 🟡

| Item | Status |
|---|---|
| [[HANRE 363-2020 — schimbarea furnizorului de gaze (text)]] / [[HANRE 363-2020 — schimbarea furnizorului de gaze (notă)]] | ✅ ingested from mirror PDF (transautogaz / weblex tipar); 177/2026 amendments reflected |
| Finance/transport Law House deepen (L202, L548, L171, L92, L1194, HG 854, Cod aerian, Cod feroviar) | ✅ notes deepened from existing vault texts |
| HANRE **853/2025** balancing T&Cs (PRE/BSP) | ❌ blocked — legis.md Cloudflare; moldelectrica 403 from this environment |
| HANRE **535/2019** gas transmission tariff methodology | ❌ no usable mirror yet |
| Law **461/2001** petroleum products market | ❌ legis.md blocked |
| Law **248/2025** crisis management | ❌ legis.md blocked |

## Follow-ups — annex gaps (need manual browser download)

> [!warning] Fetch ceiling / Cloudflare (reconfirmed 2026-08-06)
> Automated and headless browser fetches of legis.md hit Cloudflare; ANRE’s 2019 annex files are not exposed as stable direct storage URLs from this environment. Complete these via local browser download into `uploads/` or `99 Attachments/source-legis/`, then re-ingest.

| Act | legis doc_id | Problem |
|---|---|---|
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)]] | `146237` | Annexes 1–2 missing |
| [[HANRE 64-2018 — Metodologie tarife distributie EE (text)]] | `103739` | Methodology annex missing |
| [[HANRE 375-2017 — Metodologie tarife regenerabile (text)]] | `103972` | Methodology annex missing |
| [[HANRE 169-2019 — furnizarea energiei electrice (text)]] | `114962` | Truncates mid-pt. 146 |
| [[HANRE 423-2019 — Codul retelelor electrice (text)]] | `151929` | Network-code annex missing |

Optional next: water/utilities MOC if the water corpus grows.
