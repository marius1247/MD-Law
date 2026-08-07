---
title: "Energetică — segmente piață gaze (notă)"
type: domain-note
domeniu: [energetică, gaze-naturale, piață]
tags: [domain, analysis, energetică, gaze, piață, law-house]
analysis_tier: law-house
status: draft
created: 2026-08-07
updated: 2026-08-07
---

# Natural gas market segments — regulatory briefs

Step 3 deep fill for [[MOC — Piața gazelor naturale]]. Spine: [[Energetică — architecture map]]. Ops rulebook: [[HANRE 534-2019 — Regulile pietei gazelor naturale (notă)|HANRE 534/2019]]. Network: [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)|HANRE 420]] (+ 328/310). Frame law: [[Legea 108-2016 — gazele naturale (notă)|L108/2016]] (**third package**).

> [!warning] Not electricity
> No PZU/PI/OPEED stack. The commercial hinge is **entry-exit capacity + [[Concept — Punct virtual de tranzacționare|PVT]] title transfer + daily imbalance**. Electricity PRE / storage concepts are analogues only — do not cite them as gas law.

---

## A. Segment briefs

### 1. Wholesale bilaterals (delivery at PVT)

| | |
|---|---|
| **What** | OTC purchase/sale of gas with delivery at the virtual trading point |
| **Who trades** | Licensed suppliers, traders, producers; SOs only for operational volumes |
| **Operator** | Parties contract; TSO/balancing entity processes notifications |
| **Settlement logic** | Contract price private; notified quantities enter PRE portfolios → daily imbalance if inputs ≠ outputs |
| **Key sources** | HANRE 534 (PVT = wholesale delivery point) · L108 · civil contracts [[Codul civil 1107-2002 (notă)]] |
| **Practice** | A bilateral without PVT/PRE machinery is not a wholesale market position. |

### 2. Virtual Trading Point (PVT)

| | |
|---|---|
| **What** | National virtual hub — title transfer without internal physical capacity booking |
| **Who** | Registered system users / PREs |
| **Operator** | TSO + balancing entity (EE) |
| **Settlement logic** | Matched commercial notifications; feeds daily imbalance calculation |
| **Key sources** | [[Concept — Punct virtual de tranzacționare]] · HANRE 534 · 420 |
| **Practice** | First onboarding step for any wholesale participant: PVT agreement + guarantees + PRE contract. |

### 3. Entry-exit capacity (firm / interruptible / secondary)

| | |
|---|---|
| **What** | Bookable capacity at entry IPs and exit points (DSO offtakes, industrial, export) |
| **Who books** | Shippers / suppliers / traders with credit support |
| **Operator** | TSO (Vestmoldtransgaz); secondary trading via market rules |
| **Settlement logic** | Capacity tariffs (535) + nomination/renomination; unused capacity penalty / UIOLI-type pressure |
| **Key sources** | HANRE 534 · 420 · [[HANRE 535-2019 — Metodologie tarife transport gaze (notă)\|535]] (+ [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)\|329]]) · [[Concept — Tarif de transport]] |
| **Practice** | Book interruptible or use secondary market when flows uncertain; overbooking penalties are a margin killer. Main IPs in analysis: Grebenyky, Căușeni, Ungheni, Isaccea corridor points. |

### 4. Conditional / Trans-Balkan capacity

| | |
|---|---|
| **What** | Special corridor capacity product — not ordinary firm IP capacity |
| **Who** | Shippers meeting route/matching/customs/(PVT) conditions |
| **Operator** | TSO |
| **Settlement logic** | Outside ordinary balancing portfolio; priority firm > interruptible > conditional |
| **Key sources** | [[Concept — Capacitate condiționată]] · HANRE 328/310 · 535 §7² |
| **Practice** | Treat as transit/corridor tool; do not assume it covers domestic imbalance hedging. |

### 5. Balancing (gas day)

| | |
|---|---|
| **What** | Daily cash-out of PRE portfolio imbalance (entries − exits) |
| **Who** | Every PRE; EE calculates and settles |
| **Operator** | Balancing entity (EE) cooperating with OST/OSD |
| **Settlement logic** | **Asymmetric:** short → Marginal Buy = WAPP × **1.10**; long → Marginal Sell = WAPP × **0.90**; tolerances before full cash-out; **10-day** invoice challenge window |
| **Key sources** | HANRE 534 · 420 nominations |
| **Practice** | Structural cost for volatile load — telemetry + renomination matter more than the bilateral price. Electricity PRE note is conceptual cousin only. |

### 6. Storage (commercial) and SoS storage overlays

| | |
|---|---|
| **What** | (a) Licensed commercial storage access; (b) Government storage **obligation** / security stocks |
| **Who** | Storage operator (commercial) · **Energocom** (obligation holder under HG 365) |
| **Settlement logic** | Commercial: storage tariffs + injection/withdrawal as adjacent balancing zone. SoS: cost recovery via regulated mechanism; crisis-use rules |
| **Key sources** | L108 arts. 51, 56, 108²–108³ · [[HG 365-2024 — obligatie stocare gaze naturale (notă)\|HG 365]] · [[HG 364-2024 — modificare stocuri securitate gaze (notă)\|364]] · [[HG 677-2024 — plan sezon incalzire 2024-2025 (notă)\|677]] |
| **Practice** | **Three instruments, three questions** — commercial access ≠ 15% obligation ≠ 47.1 mcm security stocks. Moldova has no domestic storage at scale; EU/EnC facilities matter operationally. |

### 7. Retail supply & switching

| | |
|---|---|
| **What** | Final-customer supply contracts; free supplier switching |
| **Who** | Licensed suppliers · DSO meter/data transfer |
| **Key sources** | [[HANRE 113-2019 — furnizarea gazelor naturale (notă)\|HANRE 113]] · [[HANRE 363-2020 — schimbarea furnizorului de gaze (notă)\|363]] · [[HANRE 177-2026 — modificarea unor hotarari ANRE (notă)\|177/2026]] (fixed-price ≥12 months, comparison tool, >50 MWh/day imbalance hooks) · L108 art. 88 |
| **Practice** | Switching ≤ **21 calendar days**; anti-termination penalty clauses **void** (L108 art. 61 path). Disconnection notice rules in 113. |

### 8. PSO / regulated supply & FUO

| | |
|---|---|
| **What** | Public-service supply to protected categories + last-resort takeover on supplier failure |
| **Who** | Designated suppliers · ANRE regulated prices (355/540) |
| **Key sources** | L108 arts. 11, 89–90 · [[Concept — Furnizor de ultimă opțiune]] · HANRE 113 · [[HANRE 355-2021 — preturi reglementate furnizare gaze (notă)\|355]] / [[HANRE 540-2024 — modificare Metodologie preturi furnizare gaze (notă)\|540]] |
| **Practice** | **Live cliff:** large industrial PSO withdrawal targeted **1 Apr 2026**. Re-paper industrial contracts; do not assume regulated fallback survives. FUO remains the contingency for supplier failure (HANRE 113: limited takeover window — verify current months against 177 patches). |

---

## B. Licensing inventory (L108 arts. 10–12)

| Activity | Licence | Comment |
|---|---|---|
| Production | Yes | Domestic production thin |
| Transmission | Yes | Unbundling / certification precondition |
| Distribution | Yes | Exclusive territory |
| Storage | Yes | Commercial — not HG obligation designation |
| Trading | Yes (d¹) | Wholesale |
| Supply | Yes | Incl. PSO/FUO designations |
| CNG vehicle sales | Yes | Distinct type |
| Network ownership (ISO case) | Ownership right | Art. 10(1)(g) |

HANRE 286 remains **tariff application procedure**, not gas licensing either → [[Concept — Licență în energetică]].

---

## C. Package asymmetry & forecast

| | Electricity | Gas |
|---|---|---|
| Frame law | L164/2025 **fourth** package | L108/2016 **third** package |
| Organised short-term markets | PZU / PI / coupling path | Thin — PVT + bilaterals |
| Storage in market design | Licensed BESS activity | Commercial storage + SoS overlays |
| Live political risk | L164 HANRE re-adoption | **Unbundling + industrial PSO exit** |

Expect a gas rewrite mirroring L164. Until then, do not import electricity fourth-package actors (OPEED, aggregators, active consumers) into gas opinions.

---

## D. Fill status (Step 3)

| Deliverable | Status |
|---|---|
| [[MOC — Piața gazelor naturale]] | ✅ |
| Segment briefs 1–8 | ✅ this note |
| [[Concept — Punct virtual de tranzacționare]] | ✅ |
| Licensing inventory | ✅ |
| Gas-specific PRE deep concept | ⏳ optional if mechanics need split from electricity PRE |
| Fourth-package gas rewrite watch | Ongoing |

## Related
[[MOC — Piața gazelor naturale]] · [[Energetică — sector gaze ANRE (notă)]] · [[Energetică — architecture map]] · [[Roadmap — Energy analysis architecture]] · [[MOC — Piața de energie electrică]] · [[Legea 108-2016 — gazele naturale (notă)]] · [[HANRE 534-2019 — Regulile pietei gazelor naturale (notă)]] · [[ANRE]]
