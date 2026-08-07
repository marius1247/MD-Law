---
title: "Energetică — segmente piață electricitate (notă)"
type: domain-note
domeniu: [energetică, energie-electrică, piață]
tags: [domain, analysis, energetică, piață, law-house]
analysis_tier: law-house
status: draft
created: 2026-08-07
updated: 2026-08-07
---

# Electricity market segments — regulatory briefs

Step 2 deep fill for [[MOC — Piața de energie electrică]]. Spine: [[Energetică — architecture map]]. Ops rulebook: [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)|HANRE 283/2020]] + [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (notă)|383/2026]]. Frame law: [[Legea 164-2025 — energia electrica (notă)|L164/2025]].

> [!warning] Currency
> HANRE 283 still rests on repealed L107 enabling articles. Prefer L164 definitions and post-2025/26 ANRE acts where they conflict; treat 283 as the operational specimen until re-adopted.

---

## A. Segment briefs

### 1. Negotiated bilaterals (OTC)

| | |
|---|---|
| **What** | Direct physical-delivery electricity contracts outside organised auctions |
| **Who trades** | Licensed producers, suppliers, traders, FCEE (special lane), other admitted participants |
| **Operator** | Parties negotiate; **OPEE registers** the contract |
| **Settlement logic** | Contract price private; volumes enter net contractual positions → physical notifications → imbalance if schedule ≠ meter |
| **Key sources** | L164 art. 2 (piața contractelor bilaterale) · HANRE 283 Titlul II · civil contract doctrine [[Codul civil 1107-2002 (notă)]] |
| **Practice** | Market validity ≠ private-law validity. Unregistered / un-notified deals do not protect against imbalance. Import/export/transit need OST coordination. |

### 2. Organised bilaterals (POCB)

| | |
|---|---|
| **What** | Transparent public-auction venue for physical bilaterals (≥ 1 month delivery) |
| **Who trades** | Voluntary; gated by balancing contract, OPEE registration, POCB framework contract. SOs only for losses/tech consumption |
| **Operator** | **OPEE** |
| **Settlement logic** | Auction → registered bilateral → schedules / PRE perimeter |
| **Key sources** | [[Concept — Piața organizată a contractelor bilaterale]] · HANRE 383 pts. 32¹–32⁴¹ (IF 01.07.2026) |
| **Practice** | Use for visible LT offtake when OTC opacity or credit concerns dominate; still BRP-backed. |

### 3. Day-ahead (PZU)

| | |
|---|---|
| **What** | Organised wholesale market for each dispatch interval of the **next** delivery day |
| **Who trades** | Admitted participants posting price/quantity offers |
| **Operator** | OPEE today → **[[Concept — OPEED\|OPEED]]** for single DA coupling |
| **Settlement logic** | Clearing (consolidation references **Euphemia**-compatible logic) → confirmed trades → nominations → delivery-day imbalance residual |
| **Key sources** | L164 art. 2 pt. 100 · arts. 94–96 (CACM / OPEED) · HANRE 283 Titlul III |
| **Practice** | Guarantees and contestation clocks are in the rules — miss them and the trade is not bankable. Coupling is the L164 end-state; do not assume it is live without the [[Concept — OPEED\|OPEED]] designation decision. **REMIT** applies to wholesale participants on this venue — registration + inside-information SOP before first trade ([[Energetică — licențiere cross-border și REMIT (notă)]]). |

### 4. Intraday (PI)

| | |
|---|---|
| **What** | Organised adjustment market **after** DA gate closure, before delivery |
| **Who trades** | Same admission universe as PZU, for residual forecast error |
| **Operator** | OPEE / OPEED |
| **Settlement logic** | Continuous (and/or auction) trades update positions closer to real time → lower expected imbalance |
| **Key sources** | L164 art. 2 pt. 98 · HANRE 283 Titlul IV · 383 terminology **PPZ → PI** |
| **Practice** | Primary hedge for intermittent RES and load forecast updates. Product size rules under L164 push minimum offers toward ≤ 100 kW for small RES/storage/DR. |

### 5. Balancing

| | |
|---|---|
| **What** | TSO-run market for balancing energy / capacity so system frequency and schedules close |
| **Who trades** | **[[Concept — Furnizor de servicii de echilibrare\|FSE]]** bid products; **[[Concept — Parte responsabilă de echilibrare\|PRE]]** pay imbalances |
| **Operator** | **OST** (Moldelectrica) |
| **Settlement logic** | Activate balancing energy → price imbalances per ISP → collateralised invoices |
| **Key sources** | L164 arts. 90–91 · HANRE 283 Titlurile VI & VIII · **[[HANRE 853-2025 — clauze echilibrare FSE si PRE (notă)\|HANRE 853/2025]]** (IF **1 Jul 2026**) |
| **Practice** | From 1 Jul 2026 advise off HANRE 853 for qualification, guarantees and settlement — not from 283 alone. Suppliers typically BRP for their prosumer perimeter. |

### 6. System / ancillary services

| | |
|---|---|
| **What** | TSO procurement of services needed for secure operation (reserves, non-frequency services, etc.) beyond pure energy balancing |
| **Who provides** | Qualified FSEs, generators, storage, demand response / aggregators — technology-neutral duty under L164 |
| **Operator** | OST (procurement) · ANRE (rules / methodologies) |
| **Settlement logic** | Capacity and/or activation payments under service contracts; distinct from PRE imbalance |
| **Key sources** | HANRE 283 Titlul VII · L164 arts. 35 (OST duties), 49(4) (market-based procurement of balancing/system services) · priority dispatch Titlul XI (sensitive under fourth package) |
| **Practice** | Priority dispatch for eligible RES / CHP still interacts with FCEE and heat constraints — do not assume unlimited privilege. |

### 7. Capacity / adequacy *(not a live MD capacity market yet)*

| | |
|---|---|
| **What** | Statutory **adequacy assessment** + optional **capacity mechanism** if a resource-adequacy problem remains after market reforms |
| **Who decides** | TSO annual national adequacy assessment (by **30 Nov**) · ministry implementation plan · Government HG to introduce a capacity mechanism · ANRE monitors |
| **Operator** | N/A as organised segment until HG introduces one |
| **Settlement logic** | If introduced: capacity payments under the HG design — **subject to EnC Secretariat opinion**, state-aid check ([[Concept — Ajutor de stat]]), and prohibition on introducing a mechanism when no adequacy problem is identified |
| **Key sources** | [[Legea 164-2025 — energia electrica (text)#Articolul 49. Adecvanța resurselor pe piața|L164 arts. 49–51]] |
| **Practice** | **Verdict:** Moldova has the **legal toolbox**, not an operating capacity market. Advise “capacity revenue” only if a specific HG exists; otherwise treat as adequacy planning + reform plan risk. |

### 8. FCEE / regulated central offtake

| | |
|---|---|
| **What** | Government-designated **central electricity supplier** buys from eligible RES (and, for a defined period, urban CHP) at regulated prices and resells into the market |
| **Who trades** | [[Concept — Furnizor central de energie electrică\|FCEE]] ↔ eligible producers ([[Concept — Producător eligibil]]) ↔ organised / bilateral markets |
| **Operator** | Designated FCEE entity · ANRE price approval |
| **Settlement logic** | Support price in; market sale out; differences are a regulated / PSO economics problem, not free retail margin |
| **Key sources** | L164 art. 2 pt. 55 · [[Legea 10-2016 — surse regenerabile (notă)\|L10]] · HANRE 283 FCEE lane · [[HG 26-2025 — PSO acces retea producatori regenerabile pret fix (notă)\|HG 26/2025]] |
| **Practice** | Art. **87(2)** is a **mandatory couple**: FCEE buys; suppliers **must** buy ANRE-allocated shares at regulated prices. Bankability = FCEE credit + BRP + connection queue + supplier-purchase continuity — not the support tariff alone. **Sunset:** art. **150(3)** ends RES FCEE offtake on CfD migration; art. **150(4)** requires ANRE **calendar** for urban CHP exit (duty by 1 Jan 2026 — calendar ≠ automatic cut-off). → [[Concept — Furnizor central de energie electrică]] |

### 9. Universal service & last-resort (retail PSO lanes)

| | |
|---|---|
| **What** | Regulated retail continuity: **universal service** (standing) vs **FUO** (supplier failure contingency) — now separated on the face of L164 |
| **Who** | Designated suppliers · household + **micro/small company** perimeter for US (art. 114(1)) |
| **Key sources** | L164 arts. 17, **114–115** · [[Concept — Furnizor de ultimă opțiune]] · [[HANRE 169-2019 — furnizarea energiei electrice (notă)\|HANRE 169]] · [[Concept — Contract la prețuri dinamice]] |
| **Practice** | **Conflict:** art. 115(1) entitles consumers to FUO for **≥ 6 months**; HANRE 169 still caps at **90 days** under repealed L107 art. 73. **Apply L164.** US is not industrial PSO forever — re-screen portfolios. US/FUO must procure on bilaterals / organised markets at lowest cost (art. 109 path); market-based purchase of volumes/losses restored → [[Legea 74-2020 — achizitii sectoriale (notă)\|L74]]. |

### 10. Flexibility stack (aggregation / storage / active consumers / flexible connection)

Not a single organised venue — a **participation mode** across the segments above.

| Actor | Concept | Licence / gate |
|---|---|---|
| Active consumer | [[Concept — Consumator activ]] | Usually no supply licence; BRP duty; ANRE capacity cap by technology |
| Prosumer (net billing) | [[Concept — Facturare netă]] | L10 overlay — see boundary note |
| Independent aggregator | [[Concept — Agregator independent]] | Aggregation licence (10y); ANRE aggregation regulation still expected (art. 120(9)) |
| Storage operator | [[Concept — Stocare a energiei]] | Storage licence if ≥ 1 MW autonomous injection; SO ownership bans arts. 34/63 |
| CEC | [[Concept — Comunitate de energie a cetățenilor]] | ANRE register (art. 125) + licences when thresholds hit |
| Flexible connection | [[Concept — Racordare la rețea]] | L164 art. 2 pt. 2 — non-firm injection/withdrawal; price curtailment in PPA; HANRE 311 |

**Boundary:** [[Energetică — prosumer vs consumator activ (notă)]]

---

## B. Regulated-activity inventory (L164 catalogue)

### B.1 Activities & licence types (arts. 16–18)

| Activity (art. 16) | Licence type (art. 18) | Term | Key threshold / note |
|---|---|---|---|
| Production | Production | 25y | ≥ **5 MW** installed (single or cumulative) or integrated plant+storage ≥ 5 MW injection |
| **Storage** | Storage | 25y | Autonomous ≥ **1 MW** injection; final customers included; SO derogations excluded |
| Market operation | Market operation | 10y | **One** national licence; Government designates OPEE |
| Transmission | Transmission | 25y | Exclusive in licensed territory |
| Centralised system operation | Dispatch / SE conduction | 25y | Single TSO |
| Distribution | Distribution | 25y | Exclusive in licensed territory |
| **Trading** | Trading | 10y | Wholesale only; unlimited number |
| Supply | Supply | 10y | Wholesale + retail; EV charging points **not** supply (art. 18(9)) |
| **Aggregation** | Aggregation | 10y | Unlimited number; independent aggregator = non-affiliation status |

### B.2 Secondary-act currency (important correction)

| Act | Role | Currency for licensing advice |
|---|---|---|
| ~~[[HANRE 286-2018 — licentiere energie (notă)\|HANRE 286/2018]]~~ | **Misleading filename** — it is the **tariff/price application procedure**, not licence grant | **Do not cite for licensing** → [[Concept — Licență în energetică]] |
| L164 arts. 18–23 | Primary licensing catalogue, grant/amend/suspend/withdraw | **Authoritative** for activity → licence mapping |
| [[Legea 160-2011 — reglementarea prin autorizare (notă)\|L160/2011]] | General authorisation law | Background for renewal / reperfectare |
| Dedicated ANRE licensing regulation under L164 | Procedure / forms / dossier | **Gap to watch** — until re-adopted, argue from L164 + L160 + legacy practice carefully |
| [[Energetică — licențiere cross-border și REMIT (notă)]] | REMIT registration / wholesale integrity | Parallel compliance layer — not a substitute for art. 18 licence |

### B.3 Practitioner mapping checklist

- [ ] Name the physical/commercial activity in art. 16 vocabulary
- [ ] Map to art. 18 licence type + threshold
- [ ] Check SO ownership bans (storage arts. 34/63) before “TSO/DSO will build the BESS”
- [ ] Separate **licence** from **connection** ([[Concept — Racordare la rețea]]) and from **REMIT** registration
- [ ] For CEC / active consumer / prosumer: apply the correct status filter before assuming licence exemption

---

## C. Fill status (Step 2)

| Deliverable | Status |
|---|---|
| Segment briefs 1–10 | ✅ |
| Concepts: OPEED, consumator activ, agregator independent, stocare, CEC | ✅ |
| Licensing inventory vs true secondary acts | ✅ (286 trap documented) |
| [[Concept — Contract la prețuri dinamice]] | ✅ |
| [[Concept — Furnizor central de energie electrică]] | ✅ |
| [[Energetică — prosumer vs consumator activ (notă)\|Prosumer ↔ active-consumer boundary]] | ✅ |
| Per-segment deep annexes (offer types, guarantee formulas) | Deferred — only if client work demands |

**Step 2 closed.** Professional deepening: §E below. Next structuring work was Step 3 gas hub (done).

---

## E. Legal conflicts & advice rules (professional deepening)

| Conflict / doctrine | Binding answer | Do not |
|---|---|---|
| FUO duration | L164 art. **115(1) ≥ 6 months** | Advise from HANRE 169 **90-day** cap |
| US perimeter | Households + micro/small (art. 114(1)); designation arts. 114(2)–(3) | Assume all non-households remain on regulated US |
| FCEE RES exit | Art. **150(3)** — ends on CfD migration under L10 | Assume perpetual central offtake |
| FCEE urban CHP | Art. **150(4)** — ANRE must set **exit calendar** (duty ≤ 1 Jan 2026) | Invent a hard cut-off date the statute does not fix |
| Supplier purchase of FCEE volumes | Art. **87(2)** mandatory by retail share | Treat as optional wholesale product |
| Flexible vs firm connection | Art. 2 pt. 2 + HANRE 311 | Equate flexible *acord* with firm injection rights |
| REMIT vs licence | Parallel gates | Trade on licence alone without REMIT registration |
| Capacity revenue | Arts. 49–51 toolbox only | Sell “capacity market income” without HG |
| L107-era HANRE | Operational until conflict; then statute wins | Cite 169/283 *temei* as if still L107 primary law |
| Legacy plants | Non-retroactivity + pre-19.08.2025 design rule (L164 transitional) | Apply L164 blindly to every pre-cutover installation |

Incomplete sources that block further depth: HANRE 169 truncation; HANRE 423 parent annex; HG 820 annexes 1–2.

## Related
[[MOC — Piața de energie electrică]] · [[Energetică — prosumer vs consumator activ (notă)]] · [[Energetică — architecture map]] · [[Roadmap — Energy analysis architecture]] · [[Energetică — sector electricitate ANRE (notă)]] · [[Energetică — licențiere cross-border și REMIT (notă)]] · [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]] · [[Legea 164-2025 — energia electrica (notă)]] · [[ANRE]]
