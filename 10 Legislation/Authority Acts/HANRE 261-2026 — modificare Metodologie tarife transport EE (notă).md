---
title: "HANRE 261-2026 — modificare Metodologie tarife transport EE (notă)"
type: act-note
act: "[[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]]"
domeniu: [energetică, tarife]
enabling_act: "[[Legea 164-2025 — energia electrica (text)]]"
eu_directives: ""
analysis_tier: law-house
status: reviewed
depth: expert
tags: [act-note, analysis, energetică, tarife, ANRE, modificator]
created: 2026-08-06
updated: 2026-08-06
domain: tarife_metodologii
issuer: ANRE
legal_status: in_vigoare
---

# HANRE nr. 261/2026 — amending transmission tariff methodology — Analysis

**Raw text:** [[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]] ✅ · **Parent:** [[HANRE 626-2023 — Metodologie tarife transport EE (text)]] · [[HANRE 626-2023 — Metodologie tarife transport EE (notă)|parent notă]] · **Concepts:** [[Concept — Tarif de transport]] · [[Concept — Baza activelor reglementate]] · [[Concept — Devieri financiare]] · **Hub:** [[MOC — Energetică]]

> [!abstract] Executive summary & commercial impact
> **Core purpose:** Post-L164 parameter update to the **current** transmission methodology (626/2023). IF **23.05.2026**. Reworks technological-loss / imbalance cost recovery, softens working-capital clawback to **50%**, updates CAPM/WACC inputs, and recognises certain national-interest network project costs from financing disbursement.
> **Primary business risk:** Modelling tariffs off pre-261 parameters (old 3% imbalance proxy, full WC clawback, old beta/rm). Exact **RFD** algebraic line is OCR-weak — use definitions + 10% CTE cap until consolidated formula verified.

---

## 1. Foundation

* Amends methodology approved by HANRE **626/2023** (which abrogated 486/2017).
* Decision 16.04.2026; MO 176–179 art. 316 / 23.04.2026; IF **one month after publication** = **23.05.2026** (legis_id `154024`).

---

## 2. Material changes

| Area | Change |
|---|---|
| **Losses / imbalances (pt. 22)** | `CEj = CTEj × PEj + RFDj`. Old Wdez/PEdez (3% prior-year losses) removed. New **RFD** = TSO imbalance costs; cap logic with **Υ = 0.1** of CTEj for deficit/excess quantities |
| **Working capital (pt. 23)** | Unused/misused WC allowance reduces next-year revenue by **50%** (was 100%) |
| **Asset entry (pt. 8)** | ANRE may consider project value of transmission works declared **public utility of national interest** from financing disbursement; old revaluation depreciation clamp deleted |
| **Personnel (pt. 16)** | Adds **sector complexity coefficient** |
| **Accounting (pt. 10)** | References **SNC and/or IFRS** |
| **WACC / CAPM (pt. 25)** | rf = avg 10y MD state-bond fixed rates to end-2025; unlevered β = **0.4** (CEER 2024); rm = **5.48** (Damodaran Jan 2026); notional **50/50** D/E; Rd = 2025 BNM FX corporate >12m average |

---

## 3. Risk matrix

| Issue | Risk | Strategy |
|---|---|---|
| RFD formula OCR gap | Wrong imbalance pass-through model | Verify on legis.pdf / consolidated 626 |
| National-interest early recognition | Tension with “used & useful” entry-into-service rules | Track which projects ANRE treats under the exception |
| Parameter freeze dates (2025 rf/Rd) | Stale inputs in later years | Check whether ANRE refreshes series annually |

---

## 4. Client checklist

- [ ] Rebuild TSO tariff models with new WACC stack and RFD cap.
- [ ] For CAPEX disputes: identify national-interest designation + disbursement evidence.
- [ ] Challenge/defend WC clawbacks using the **50%** rule for post-IF periods.
- [ ] Keep [[HANRE 486-2017 — Metodologie tarife transport EE (notă)|486/2017]] only for historic periods.

---

## Sources

[[HANRE 261-2026 — modificare Metodologie tarife transport EE (text)]] — legis.md `154024`.
