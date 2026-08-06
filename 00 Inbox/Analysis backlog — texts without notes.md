---
title: "Analysis backlog — texts without notes"
type: project
tags: [project, backlog, analysis]
created: 2026-08-06
updated: 2026-08-06
status: active
---

# Analysis backlog — `(text)` without `(notă)` / concepts

Audit of standalone working texts under `10 Legislation/` that lack a companion `(notă)`. Split-chapter code files and indexes excluded. Non-standard: [[Legea 244-2024 — revizuirea Constituției (UE)]] (treaty/revision note — not a classic act pair).

**14 acts** were missing notes as of 2026-08-06; Batch 1 (3 acts) now has Law House notes → **11 remaining**.

## Batch 1 — primary / crisis / security ✅ done (2026-08-06)

| Act | Note | Concepts / authority |
|---|---|---|
| [[Legea 139-2018 — eficienta energetica (text)]] | [[Legea 139-2018 — eficienta energetica (notă)]] | [[Concept — Audit energetic]] · [[Concept — Contract de performanță energetică]] · [[Concept — Parte obligată (eficiență energetică)]] · [[Concept — Eficiența energetică înainte de toate]] · [[CNED]] |
| [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (text)]] | [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (notă)]] | [[Concept — Situație de criză în domeniul petrolier]] |
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)]] | [[HG 820-2024 — situatii exceptionale electroenergetic (notă)]] ⚠️ annex missing | [[Concept — Situație excepțională electroenergetică]] *(stub)* |

## Batch 2 — electricity market & supply operations

| Act | Notes |
|---|---|
| [[HANRE 169-2019 — furnizarea energiei electrice (text)]] | Large supply regulation; `text_complet: false` — analyse from available text + flag gaps |
| [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (text)]] | Amends [[HANRE 283-2020 — Regulile pietei energiei electrice (text)]]; in force 01.07.2026 |
| [[HANRE 177-2026 — modificarea unor hotarari ANRE (text)]] | Omnibus ANRE amendment — map knock-ons before citing affected acts |

## Batch 3 — tariff methodologies

| Act | Notes |
|---|---|
| [[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]] | Amends current [[HANRE 626-2023 — Metodologie tarife transport EE (text)]] |
| [[HANRE 64-2018 — Metodologie tarife distributie EE (text)]] | Incomplete; re-check annex |
| [[HANRE 375-2017 — Metodologie tarife regenerabile (text)]] | Incomplete; links to [[Concept — Producător eligibil]] |
| [[HANRE 486-2017 — Metodologie tarife transport EE (text)]] | **Abrogated** — short historical note only |

## Batch 4 — gas network amendments & outliers

| Act | Notes |
|---|---|
| [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (text)]] | Amends [[HANRE 420-2019 — Codul retelelor de gaze naturale (text)]] |
| [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]] | Same parent |
| [[HANRE 169-2025 — investitii apa si canalizare (text)]] | Water/sewerage — outside energy MOC; new domain or defer |
| [[Rectificare ANRE 05-03-5694-2025 (text)]] | Minor corrigendum — thin note |

## Workflow per batch

1. Write Law House `(notă)` from [[Template — Act (notă)]]
2. Extract `Concept — …` notes where doctrine is new
3. Seed / update authority profiles if a new institution appears (e.g. CNED)
4. Wire into [[MOC — Energetică]] / relevant MOC + [[Energetică — synthesis]]
5. Update [[Status ingestie — Energetica]] analysis-layer list
