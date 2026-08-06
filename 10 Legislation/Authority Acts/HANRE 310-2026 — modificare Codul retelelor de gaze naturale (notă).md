---
title: "HANRE 310-2026 — modificare Codul retelelor de gaze naturale (notă)"
type: act-note
act: "[[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]]"
domeniu: [energetică, gaze-naturale]
enabling_act: "[[Legea 108-2016 — gazele naturale (text)]]"
eu_directives: "Regs (EU) 2017/459 CAM; 2015/703 interoperability; 2017/460 TAR; 312/2014 balancing — EnC-adapted"
analysis_tier: law-house
status: reviewed
depth: expert
tags: [act-note, analysis, energetică, gaze, ANRE, modificator]
created: 2026-08-06
updated: 2026-08-06
domain: gaze_naturale
issuer: ANRE
legal_status: in_vigoare
---

# HANRE nr. 310/2026 — recasting conditional capacity in Gas Network Code — Analysis

**Raw text:** [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]] ✅ · **Parent:** [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)]] · **Prior amend:** [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (notă)]] · **Concept:** [[Concept — Capacitate condiționată]] · **Hub:** [[MOC — Energetică]]

> [!abstract] Executive summary & commercial impact
> **Core purpose:** Recasts Chapter VI¹ **capacitate condiționată** and expands the Code’s EU-gas network code harmonisation clause. This is the **current** product architecture for Trans-Balkan corridor transit through Moldova.
> **Primary business risk:** Booking “ordinary” cross-border capacity mental models — conditional capacity is route-locked, may be without PVT access, sits outside balancing portfolios, and is interruptible behind firm/interruptible products.

---

## 1. Foundation

* Enabling: L108 arts. 7(1)(k), 7(1)(q¹), 72(3).
* Harmonisation clause updated to CAM, interoperability, TAR, balancing regulations (EnC-adapted versions).
* Abrogates some 328-era point references while rewriting the dedicated chapter.

---

## 2. Conditional capacity — current rules

→ [[Concept — Capacitate condiționată]]

* Supports use of MD transmission as part of the **Trans-Balkan corridor**.
* Products: day-ahead, monthly, quarterly, annual — only at IPs with ANRE-approved tariffs; OST publishes eligible points/tariffs (methodology HANRE **535/2019**).
* Quantities **excluded** from balancing portfolio / daily imbalance calculation.
* Cumulative use conditions (reconstructed from text):
  * Căușeni entry UA→MD for capacity without PVT access;
  * PVT access via Căușeni operationally limited to **6 million m³/day**;
  * above that limit, capacity without PVT only if equal capacity reserved at Grebenyky exit MD→UA;
  * no use for other IPs, distribution exits, or direct TSO-connected consumers;
  * equal injection at Căușeni and offtake at Grebenyky;
  * customs transit under Customs Code.
* OST may cut mismatched nominations to the lower confirmed quantity and interrupt for breach.
* Priority: firm > interruptible > conditional.

---

## 3. Risk matrix

| Issue | Risk | Strategy |
|---|---|---|
| PVT vs no-PVT split | Wrong commercial product booked | Explicitly state PVT access in nomination/contract |
| 6 mcm/day PVT cap | Corridor congestion / forced no-PVT path | Reserve matched Grebenyky exit early |
| Outside balancing portfolio | Imbalance accounting surprises | Align BRP systems to exclude conditional quantities |
| Tariff source 535/2019 absent | Incomplete price advice | Pull HANRE 535 before pricing |

---

## 4. Client checklist

- [ ] Confirm path Căușeni UA→MD / Grebenyky MD→UA.
- [ ] Choose with/without PVT; respect 6 mcm/day PVT ceiling.
- [ ] Match entry/exit reserved quantities; nominate as conditional capacity.
- [ ] Verify ANRE tariff + OST publication for the IP/product.
- [ ] Model interruption priority explicitly in transit contracts.

## Sources
[[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (text)]] — legis.md `154280`.
