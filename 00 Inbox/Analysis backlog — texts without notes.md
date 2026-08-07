---
title: "Analysis backlog — texts without notes"
type: project
tags: [project, backlog, analysis]
created: 2026-08-06
updated: 2026-08-07
status: active
---

# Analysis backlog — `(text)` without `(notă)` / concepts

Audit of standalone working texts under `10 Legislation/` that lacked a companion `(notă)`. Non-standard: [[Legea 244-2024 — revizuirea Constituției (UE)]] (treaty/revision note — not a classic act pair).

**Starting set (2026-08-06):** 14 acts. **All four batches now have Law House notes.** **Batch 6 (2026-08-07)** ingested five user-uploaded ANRE PDFs with companions. Remaining work is annex completion / parent ingestion, not missing companions.

## Batch — tax/accounting uploads (2026-08-07) ✅

| Act | Status |
|---|---|
| [[Legea 77-2016 — parcuri tehnologia informatiei (text)]] / [[Legea 77-2016 — parcuri tehnologia informatiei (notă)\|notă]] | ✅ · [[Concept — Parc IT]] |
| [[Legea 125-2024 — modificare parc IT si tranzitii vamale (text)]] / [[Legea 125-2024 — modificare parc IT si tranzitii vamale (notă)\|notă]] | ✅ omnibus (IT Park / CA art. 214 / customs) |
| [[OMF 118-2013 — Standardele Nationale de Contabilitate (text)]] / [[OMF 118-2013 — Standardele Nationale de Contabilitate (notă)\|notă]] | ✅ approving order · individual SNC texts still ❌ |
| [[OMF 73-2022 — modificare indicatii metodice contabilitate (text)]] / [[OMF 73-2022 — modificare indicatii metodice contabilitate (notă)\|notă]] | ✅ |
| [[OMF 128-2024 — modificare formular IPC21 (text)]] / [[OMF 128-2024 — modificare formular IPC21 (notă)\|notă]] | ✅ · parent OMF 94/2020 still ❌ |

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
| HANRE **535/2019** gas transmission tariff methodology | 🟡 decision ✅ ([[HANRE 535-2019 — Metodologie tarife transport gaze (notă)\|notă]]) · **annex still ❌** — amending [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)\|329/2025]] ✅ |
| Law **461/2001** petroleum products market | ❌ legis.md blocked |
| Law **248/2025** crisis management | ❌ parent still missing · HG 346/2026 + L150/2026 ingested 2026-08-07 |

## Follow-ups — annex gaps (need manual browser download)

> [!warning] Fetch ceiling / Cloudflare (reconfirmed 2026-08-06)
> Automated and headless browser fetches of legis.md hit Cloudflare; ANRE’s 2019 annex files are not exposed as stable direct storage URLs from this environment. Complete these via local browser download into `uploads/` or `99 Attachments/source-legis/`, then re-ingest.

| Act | legis doc_id | Problem |
|---|---|---|
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)]] | `146237` | Annexes 1–2 missing |
| [[HANRE 64-2018 — Metodologie tarife distributie EE (text)]] | `103739` | Methodology annex missing |
| [[HANRE 375-2017 — Metodologie tarife regenerabile (text)]] | `103972` | Methodology annex missing |
| [[HANRE 169-2019 — furnizarea energiei electrice (text)]] | `114962` | Truncates mid-pt. 146 |
| [[HANRE 423-2019 — Codul retelelor electrice (text)]] | `151929` | Clean annex consolidation still missing — **partial substance** via [[HANRE 656-2021 — modificare Codul retelelor electrice (text)\|656/2021]] (`129504`) ✅ |
| [[HANRE 535-2019 — Metodologie tarife transport gaze (text)]] | `149131` | Approving decision ✅ · **methodology annex missing** · amend [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (text)\|329/2025]] ✅ |

## Batch 6 — user PDF upload (2026-08-07) ✅

| Act | Status |
|---|---|
| [[HANRE 24-2017 — achizitii titulari de licenta (abrogata) (text)]] / [[HANRE 24-2017 — achizitii titulari de licenta (abrogata) (notă)\|notă]] | ✅ historic (abrogated 06.08.2021) |
| [[HANRE 305-2021 — abrogare HANRE 24-2017 achizitii titulari (text)]] / [[HANRE 305-2021 — abrogare HANRE 24-2017 achizitii titulari (notă)\|notă]] | ✅ repeal → L74/2020 |
| [[HANRE 656-2021 — modificare Codul retelelor electrice (text)]] / [[HANRE 656-2021 — modificare Codul retelelor electrice (notă)\|notă]] | ✅ Parts I–V restructuring of 423 |
| [[HANRE 833-2023 — modificarea unor hotarari ANRE regenerabile (text)]] / [[HANRE 833-2023 — modificarea unor hotarari ANRE regenerabile (notă)\|notă]] | ✅ renewables omnibus (168/169/537) |
| [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (text)]] / [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)\|notă]] | ✅ conditional-capacity tariffs; parent [[HANRE 535-2019 — Metodologie tarife transport gaze (notă)\|535]] decision ✅ · annex ❌ |

## Batch 7 — energy PDF OCR (2026-08-07) ✅

| Act | Note |
|---|---|
| [[HANRE 94-2019 — dezvoltarea retelelor electrice de distributie (text)]] | [[HANRE 94-2019 — dezvoltarea retelelor electrice de distributie (notă)]] |
| [[HANRE 414-2020 — modificare HANRE 94-2019 dezvoltare retele distributie EE (text)]] | [[HANRE 414-2020 — modificare HANRE 94-2019 dezvoltare retele distributie EE (notă)]] |
| [[HANRE 316-2018 — dirijare dispecerat sistem electroenergetic (text)]] | [[HANRE 316-2018 — dirijare dispecerat sistem electroenergetic (notă)]] |
| [[HANRE 138-2018 — dezvoltarea retelelor de distributie gaze (text)]] | [[HANRE 138-2018 — dezvoltarea retelelor de distributie gaze (notă)]] |
| [[HANRE 8-2023 — modificare racordare gaze si masurare gaze (text)]] | [[HANRE 8-2023 — modificare racordare gaze si masurare gaze (notă)]] ⚠️ annex OCR |

Optional next: recover HANRE **535/2019 methodology annex** + **537/2020** QoS + **297/2022** metering parent; water/utilities MOC if the water corpus grows.
