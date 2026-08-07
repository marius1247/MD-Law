---
title: "Energetică — metodologii tarifare"
type: domain-note
domeniu: [energetică, tarife]
tags: [domain, analysis, energetică, tarife, law-house]
analysis_tier: law-house
status: draft
created: 2026-07-28
updated: 2026-07-28
---

# Energy — tariff methodologies & pricing (Batch 3 dossier)

Cross-act synthesis of ANRE rate-making in Moldova. Individual methodology companions: [[HANRE 626-2023 — Metodologie tarife transport EE (notă)]] · [[HANRE 64-2018 — Metodologie tarife distributie EE (text)]] · [[HANRE 375-2017 — Metodologie tarife regenerabile (text)]]. Hub: [[MOC — Energetică]] · Concept: [[Concept — Tarif reglementat]]

> [!abstract] Executive summary
> ANRE exercises exclusive tariff authority under [[Legea 174-2017 — energetica (notă)]], [[Legea 164-2025 — energia electrica (notă)]] and [[Legea 108-2016 — gazele naturale (notă)]]. Tariffs must be cost-reflective, non-discriminatory, and stable across multi-year regulatory periods — with the **financial deviation (FD)** mechanism as the primary shock absorber for commodity and FX volatility.

---

## 1. Statutory authority & core rate-making principles

| Principle | Legal basis | Practical effect |
|---|---|---|
| **Cost-reflectivity** | L174 art. 3; L164/L108 tariff chapters | Tariffs cover justified OPEX, depreciation, and fair return on capital |
| **Non-discrimination** | L174 art. 2; EU third/fourth package | No cross-subsidy between consumer categories or activities |
| **Incentive regulation** | ANRE methodologies | Multi-year revenue caps, X-factor efficiency targets, benchmarked OPEX |
| **Regulatory stability** | 5-year methodology periods | Annual indexation + extraordinary adjustments on trigger events |

---

## 2. Electricity sector tariff architecture

```
                    ELECTRICITY TARIFF METHODOLOGY
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
  TRANSMISSION           DISTRIBUTION         REGULATED SUPPLY
  HANRE 626/2023         HANRE 64/2018*       (ANRE Dec. 2025)*
  (replaces 486/2017)    binomial reform 2025  FSU vs. FUO
        │                     │                     │
   RAB × WACC            capacity + kWh        WAPP + margin
   allowed losses        voltage stratification balancing pass-through
```

*Distribution methodology updated May 2025 (binomial structure); regulated supply methodology Dec 2025 — verify current ANRE decisions at source.

### 2.1 Transmission (TSO: Î.S. Moldelectrica)

**Legal basis:** [[HANRE 626-2023 — Metodologie tarife transport EE (notă)]]

Revenue requirement:

$$\text{RR}_{\text{TSO}} = \text{OPEX}_{\text{reg}} + \text{DEP} + (\text{RAB} \times \text{WACC}) + \text{NL}_{\text{cost}} + \text{AS}_{\text{cost}} \pm \text{FD}$$

| Component | Meaning |
|---|---|
| OPEX_reg | Controllable/non-controllable operating expenses with efficiency indexation |
| DEP | Linear depreciation of regulated assets |
| RAB × WACC | Return on regulated asset base (real WACC, pre-tax) |
| NL_cost | Grid loss costs, capped at normative percentages |
| AS_cost | Ancillary services and balancing procurement |
| FD | Financial deviations from prior regulatory years |

### 2.2 Distribution (DSOs: Premier Energy Distribution, RED Nord)

**2025 reform — binomial tariff structure:**

- **Fixed component:** capacity reservation fee (MDL/kW/month)
- **Volumetric component:** energy transportation fee (MDL/kWh)
- **Voltage stratification:** HV (35–110 kV) · MV (6–10 kV) · LV (0.4 kV)
- **Investment incentives:** accelerated return above capex thresholds; OPEX subject to X-factor benchmarking

### 2.3 Regulated supply (FSU / FUO)

End-user regulated price:

$$P_{\text{reg}} = \text{WAPP}_{\text{el}} + T_{\text{trans}} + T_{\text{dist}} + M_{\text{supp}} + C_{\text{bal}} \pm \text{FD}$$

- **FSU** (universal service): households + micro/small enterprises
- **FUO** (supplier of last resort): emergency supply when primary supplier fails → [[Concept — Furnizor de ultimă opțiune]]

---

## 3. Natural gas sector tariff architecture

### 3.1 Transmission — harmonised entry/exit model

**Legal basis:** ANRE Decision of 27.06.2023 (amending transmission tariff methodology)

Milestone: transformation from distance-volumetric model (MDL/1000 m³/100 km) to **EU-compliant harmonised entry/exit system**.

| Tariff | Application |
|---|---|
| T_entry | Border interconnection points (Grebenyky, Căușeni, Iași-Ungheni) — firm/interruptible capacity |
| T_exit | Distribution off-takes, large industrial connections |
| ITC | Inter-TSO compensation between Vestmoldtransgaz and Moldovatransgaz |

### 3.2 Regulated gas supply

$$P_{\text{gas}} = \text{WAPP}_{\text{gas}} + T_{\text{trans}} + T_{\text{dist}} + M_{\text{gas\_supp}} \pm \text{FD}$$

**Legal basis:** HANRE 355/2021 (as amended by 540/2024). Gas TSO transport methodology HANRE **535/2019** parent still missing — amending [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)|HANRE 329/2025]] ingested (conditional-capacity tariffs). HANRE 443/2020 still not ingested.

### 3.3 Uniform distribution tariff

Under [[Legea 108-2016 — gazele naturale (notă)]] art. 2: single uniform gas distribution tariff across all DSOs, with reconciliation entity for equalisation payments.

---

## 4. Financial deviation (FD) mechanism

```
  Actual commodity/FX  vs.  Tariff forecast assumptions
              \                    /
               v                  v
         [ Deviation = Actual − Forecast ]
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
  Variance ≥ threshold            Variance < threshold
  (1–5% trigger)                  (normal band)
         │                             │
  Extraordinary tariff revision   Annual true-up cycle
  (clawback / pass-through)       (amortised 1–3 years)
```

**Formula:**

$$\text{FD}_n = \sum_{t=1}^{12} \left[ V_t \times (P_t^{\text{act}} - P_t^{\text{reg}}) \right] \times (1 + i_t)$$

| Trigger | Examples |
|---|---|
| Annual adjustment | Q4/Q1 alignment with audited costs and efficiency benchmarks |
| Extraordinary | Import price volatility >1–5%; MDL/USD or MDL/EUR shifts; volume variance >5% |

**Litigation angle:** CSJ practice holds ANRE cannot arbitrarily defer validly documented FD — see [[Energetică — contencios administrativ și precedente (notă)]] §2.1.

---

## 5. Master tariff comparison matrix

| Sector & activity | Governing decision | Asset model | Primary driver | Special features |
|---|---|---|---|---|
| EE transmission | HANRE 626/2023 | RAB / cost-plus | Depreciation & system services | ENTSO-E sync; cross-border allocation |
| EE distribution | May 2025 methodology | Incentive revenue cap | Voltage & capacity | Binomial tariffs |
| EE supply | Dec 2025 methodology | Pass-through + margin | WAPP & balancing | FSU vs. FUO separation |
| Gas transmission | 27.06.2023 | RAB entry/exit | Booked capacity (MW/day) | EU harmonised entry/exit |
| Gas supply | HANRE 355/2021 (mod. 540/2024) | Cost-plus / pass-through | Import WAPP | Multi-year FD smoothing |
| Renewables | HANRE 375/2017 | Fixed tariff | Technology quota | 15-year PPA with Energocom |

---

## 6. Risk matrix (cross-cutting)

| Risk | Impact | Mitigation |
|---|---|---|
| ANRE delays annual recalculation despite >5% cost shift | Cash-flow crisis for regulated operators | Administrative action in obligation under [[Codul administrativ 116-2018 (notă)]]; CSJ cost-reflectivity precedent |
| FD haircut in subsequent tariff period | Unrecovered FX/commodity losses | Document deviations with audited accounts; judicial review |
| Binomial distribution tariff reform (2025) | Consumer bill structure change; industrial capacity charges | Model new tariff components before contract pricing |
| Missing gas methodology parents in vault | Incomplete advice on gas DSO/supply / full TSO BAR | Ingest HANRE 535/2019 (329 amend ✅), 443/2020 |

---

## 7. Client action checklist

- [ ] Identify whether the tariff is normative (methodology) or individual (specific tariff decision) — different challenge routes.
- [ ] Audit FD accumulation against ANRE-approved forecast assumptions quarterly.
- [ ] For regulated operators: file extraordinary adjustment petitions when macro triggers are met.
- [ ] For large consumers: review impact of binomial distribution tariffs on capacity reservation costs.
- [ ] Cross-check gas uniform tariff reconciliation statements from DSO.

---

## Sources

Synthesised from vault companions and Law House Batch 3 dossier. Verify all methodology decision numbers and dates at [ANRE](https://anre.md) before client advice.
