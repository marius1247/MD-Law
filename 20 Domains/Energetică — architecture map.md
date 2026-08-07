---
title: "Energetică — architecture map"
type: domain-note
domeniu: [energetică]
tags: [domain, analysis, energetică, architecture, inter-law, market-segmentation]
status: draft
created: 2026-08-07
updated: 2026-08-07
---

# Energy — architecture map

How Moldovan energy acts **communicate**, and how the analysis layer should be **segmented by market** from a regulatory perspective.

Hub inventory: [[MOC — Energetică]] · Practitioner narrative: [[Energetică — synthesis]] · Build plan: [[Roadmap — Energy analysis architecture]]

> [!abstract] Use this note as the spine
> For “which law speaks to which?” → §1–3. For “how do we cut the markets?” → §4–5. For “what is filled vs stubbed?” → §6.

---

## 1. Two kinds of communication between acts

### 1.1 Vertical cascade (delegation)

Already the mental model of the domain — restated here because every horizontal bridge still rides on it:

```
Energy Community Treaty  ←── L117/2009 ratification
        ↓ (adapted acquis decisions: …/MC-EnC)
Parliament — organic / ordinary law
        ↓  temei legal (enabling article)
Government — HG (strategy, SoS, quotas, methodologies of policy)
        ↓
ANRE — HANRE (market rules, network codes, connection/supply, tariff methodologies)
        ↓
ANRE — individual decisions (licences, specific tariffs)  ← not ingested
```

**Reading rule:** an operational obligation is almost always in a HANRE. The law supplies objectives, actor definitions, licensing catalogue, and the *power* to regulate. Challenging a HANRE starts with the enabling article (`temei legal`) — *ultra vires* is the standard attack line. See [[Energetică — synthesis]] §1–2 · [[Energetică — contencios administrativ și precedente (notă)]].

### 1.2 Horizontal bridges (same-tier talk)

Sectoral laws do not sit in silos. They **call**, **defer**, **amend**, or **override** each other. The important bridges in the current corpus:

| From | To | How they communicate | Practical effect |
|---|---|---|---|
| [[Legea 174-2017 — energetica (notă)\|L174/2017]] | L164 · L108 · L92 · L10 · L461 | Framework: who may regulate; ANRE independence; energy/climate governance | Sectoral laws assume L174's institutional answers |
| [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)\|L117/2009]] | All energy acquis | Treaty obligation → EnC-adapted EU text is the transposition target | Always check `…/MC-EnC`, not only CELEX |
| [[Legea 164-2025 — energia electrica (notă)\|L164/2025]] | [[Legea 10-2016 — surse regenerabile (notă)\|L10/2016]] | RES electricity is sold / balanced / connected under electricity market + network rules; support stays in L10 | Legal work on RES is usually connection + BRP + FCEE, not only the support tariff |
| L164 | [[Legea 139-2018 — eficienta energetica (notă)\|L139/2018]] | Flexibility / demand response: L139 hooks that still cite L107 must be re-routed through L164 | Do not advise DR from L139 alone |
| L164 | [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)\|HANRE 283]] · [[HANRE 311-2026 — racordarea la retelele electrice (notă)\|311]] · tariffs | Law creates market/actors; HANRE operationalises | Currency: many HANRE still on L107 *temei* |
| [[Legea 108-2016 — gazele naturale (notă)\|L108/2016]] | [[HANRE 534-2019 — Regulile pietei gazelor naturale (notă)\|534]] · network code · gas tariffs | Same pattern as electricity, **one package behind** | Expect a gas L164-equivalent |
| [[Legea 92-2014 — energia termica si cogenerarea (notă)\|L92/2014]] | L164 (electricity from CHP) · L10 (if RES heat) · FCEE | CHP straddles heat regulation and electricity market | Urban CHP → FCEE lane under L164 vocabulary |
| [[Legea 461-2001 — piata produselor petroliere (notă)\|L461/2001]] | [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (notă)\|L101/2026]] · [[Legea 248-2025 — managementul situatiilor de criza (notă)\|L248]] | Petroleum market + crisis price / procurement tools | Do not conflate petroleum crisis with electricity risk-preparedness ([[HG 820-2024 — situatii exceptionale electroenergetic (notă)\|HG 820]]) |
| L10 | [[HG 599-2025 — limite capacitate regenerabile 2030 (notă)\|HG 599]] · [[HG 26-2025 — PSO acces retea producatori regenerabile pret fix (notă)\|HG 26]] · [[HANRE 375-2017 — Metodologie tarife regenerabile (notă)\|375]] | Quotas / PSO / fixed-tariff methodology | Support is a three-tier stack |
| L139 | [[CNED]] · [[HG 829-2024 — audit energetic intreprinderi mari (notă)\|HG 829/2024]] · FEE | Obligation scheme, audits, EPC finance | Efficiency is compliance, not soft policy |
| Climate governance | [[HG 10-2024 — guvernanta energetica si actiuni climatice (notă)\|HG 10/2024]] · [[HG 86-2025 — PNIEC 2025-2030 (notă)\|PNIEC]] | Planning / reporting layer above markets | ESG narrative anchors here + accounting non-financial statements |
| Sectoral procurement | [[Legea 74-2020 — achizitii sectoriale (notă)\|L74/2020]] | Utilities buy energy / works under sectoral procurement after HANRE 24 repeal | Market-based procurement of losses intersects here |
| Company law | L164 / L108 unbundling | Structural unbundling executed via SA/SRL reorganisation | [[Societăți & guvernanță — synthesis]] |

**Reading rule for bridges:** when two laws both seem to answer the question, ask which one is *institutional* (L174), which is *sectoral market* (L164/L108/L92/L461), which is *support / climate / crisis*, and which is *operational HANRE*. Cite the lowest tier that actually binds, and the enabling article that authorised it.

---

## 2. Package asymmetry (the legislative forecast)

| Vector | Domestic frame | EU / EnC package | Signal |
|---|---|---|---|
| Electricity | **L164/2025** | Fourth (+ REMIT, CACM; 2024 amends) | Current |
| Gas | L108/2016 | Third | **Next major rewrite expected** |
| Heat / CHP | L92/2014 | Older / partial | Local monopoly + CHP bridges |
| RES support | L10/2016 | RED lineage (EnC-adapted) | Live: net billing, quotas to 2030 |
| Efficiency | L139/2018 | EED lineage | Hardened by LP111/2025 |
| Petroleum | L461/2001 | Sectoral / SoS | Crisis tools via L101/L248 |
| Hydrogen / coal / geothermal as standalone markets | — | Acquis pressure uneven | **Stubs** — see §6 |

Electricity being a package ahead of gas is the best predictor of what changes next ([[Energetică — synthesis]] §6).

---

## 3. Inter-law map (compact diagram)

```
                    ┌─────────────────────────────────────┐
                    │  L117/2009  Energy Community Treaty │
                    └──────────────────┬──────────────────┘
                                       │ adapted acquis
                    ┌──────────────────▼──────────────────┐
                    │  L174/2017  Framework (ANRE, policy) │
                    └──────────────────┬──────────────────┘
           ┌───────────┬───────────────┼───────────────┬───────────┐
           ▼           ▼               ▼               ▼           ▼
        L164/2025   L108/2016       L92/2014        L10/2016    L461/2001
        electricity   gas            heat/CHP         RES         petroleum
           │           │               │               │           │
           ▼           ▼               ▼               ▼           ▼
        HANRE 283    HANRE 534      HANRE 23        HG quotas   ANRE max
        311, codes   420, tariffs   supply          375, 311    prices
        tariffs      112/113                        net billing  L101 crisis
           │           │               │               │
           └───────────┴───────┬───────┴───────────────┘
                               ▼
                    L139 efficiency · HG 10 / PNIEC · L248/L101 crisis
                               │
                               ▼
                    Cross-cutting: prosumers · incentives · ESG
```

---

## 4. Market segmentation taxonomy (regulation lens)

Every energy vector is analysed with the **same columns**. Cells may be empty — that is information.

### 4.1 Columns (apply to each vector)

| Column | Meaning |
|---|---|
| **Market segments** | Where title to energy / capacity / flexibility is traded or allocated (incl. regulated supply) |
| **Actors** | Who the law names (licensed or designated) |
| **Regulated activities** | Activities that require a licence / authorisation / designation |
| **Network / monopoly layer** | TSO/DSO duties, network codes, connection, QoS, regulated tariffs |
| **Support & PSO** | Subsidies, quotas, FUO/universal service, vulnerability |
| **Crisis & SoS** | Emergency instruments that override ordinary market operation |
| **ESG / climate hooks** | Governance, GHG, disclosure, efficiency obligations that touch the vector |

### 4.2 Standard electricity segment list (filled in [[MOC — Piața de energie electrică]])

| Segment | MD label / home | Regulatory character |
|---|---|---|
| Long-term / bilaterals | Contracte bilaterale · POCB | Private contract + registration / scheduling duties |
| Day-ahead | PZU | Organised short-term; CACM / coupling trajectory |
| Intraday | PI | Organised; post-383 terminology aligned |
| Balancing | Piața de echilibrare | TSO-run; BRP / FSE; [[HANRE 853-2025 — clauze echilibrare FSE si PRE (notă)\|853/2025]] |
| System / ancillary services | Servicii de sistem | TSO procurement of reserves / services |
| Capacity / adequacy | Adequacy / capacity mechanisms | L164 vocabulary present; operational depth TBD in analysis |
| Regulated / central offtake | FCEE · universal service · FUO | Not “free market”; still a market *structure* segment |
| Flexibility / aggregation / storage | New L164 activities | Partially ahead of HANRE re-adoption |

### 4.3 Vectors to mirror (later steps)

| Vector | Hub status | Primary acts |
|---|---|---|
| **Electricity** | ✅ Steps 1–2 | L164 · HANRE 283/383 · 853 · 311 · 423/656 · tariffs |
| **Gas** | ✅ Step 3 | L108 · HANRE 534 · 420/328/310 · 112/113/177 · 535/443/355 · HG 365 |
| **Petroleum** | ✅ Step 4 | L461 · L101 · L248/CNMC |
| **Coal** | ✅ Step 4 stub | [[Energetică — cărbune gap stub (notă)]] — no dedicated market law |
| **Thermal / CHP** | ✅ Step 5 | L92 · HANRE 23 · HG 197 · [[MOC — Piața energiei termice]] |
| **Geothermal** | ✅ Step 5 stub | [[Energetică — geotermal gap stub (notă)]] — L10 RES / L92 if SACET / PM_DC25 |
| **Biofuels** | ⏳ Step 6 | HG 53 · L10 bridges |
| **Hydrogen** | ⏳ Step 6 stub | Watch EnC / EU; MD primary silence |


### 4.4 Cross-cutting layers (Step 7)

| Layer | Why separate | Seed material already in vault |
|---|---|---|
| **Prosumers / active consumers** | Spans L10 support + L164 consumer rights + connection/supply HANRE | [[Concept — Facturare netă]] · HANRE 833 Anexa 5 · L164 *consumator activ* |
| **Incentives** | Support schemes change revenue stacks without changing market segments | Eligible producer · HG 26 PSO · HG 599 quotas · L241 vulnerability fund · CNED/FEE |
| **ESG / climate** | Governance and disclosure sit above trading rules | HG 10 · PNIEC · L139 · biofuel GHG · accounting non-financial statements |

---

## 5. Where existing notes sit in the new spine

| Existing note | Role under new architecture |
|---|---|
| [[Energetică — synthesis]] | Practitioner narrative (problems, risk, package story) — keep short |
| [[MOC — Energetică]] | Master act inventory by tier |
| [[MOC — Piața de energie electrică]] | **Axis B hub — electricity** (segments, actors, activities) |
| [[MOC — Piața gazelor naturale]] | **Axis B hub — gas** (PVT, entry-exit, balancing, PSO exit) |
| [[MOC — Piața produselor petroliere]] | **Axis B hub — petroleum** (price-cap retail, licensing, crisis) |
| [[MOC — Piața energiei termice]] | **Axis B hub — heat / CHP** (public-service tariffs, licences, HE CHP → EE) |
| [[Energetică — segmente piață electricitate (notă)]] | Electricity segment briefs |
| [[Energetică — segmente piață gaze (notă)]] | Gas segment briefs |
| [[Energetică — segmente piață petrol (notă)]] | Petroleum segment briefs |
| [[Energetică — segmente piață termică (notă)]] | Thermal / CHP segment briefs |
| [[Energetică — cărbune gap stub (notă)]] | Coal — no dedicated ANRE market |
| [[Energetică — geotermal gap stub (notă)]] | Geothermal — RES / SACET / no dedicated market |

| [[Energetică — prosumer vs consumator activ (notă)]] | Electricity prosumer boundary |
| [[MOC — Racordare și acces la rețele]] | Monopoly / connection slice (cross-vector) |
| [[MOC — Tarife și metodologii ANRE]] | Monopoly / tariff slice |
| [[Energetică — sector electricitate ANRE (notă)]] | Operational dossier — feeds the electricity hub |
| [[Energetică — sector gaze ANRE (notă)]] | Operational dossier — feeds the gas hub |
| [[Energetică — metodologii tarifare (notă)]] | Tariff deep dive |
| [[Energetică — licențiere cross-border și REMIT (notă)]] | Licensing + wholesale integrity slice |
| `30 Concepts/*` | Atomic doctrines cited from hubs — do not duplicate into MOCs |

---

## 6. Fill status & next action

| Step | Deliverable | Status |
|---|---|---|
| 1 | This map + electricity market MOC rewrite | **Done (2026-08-07)** |
| 2 | Electricity deep fill (segment briefs + missing concepts) | **Done (2026-08-07)** — [[Energetică — segmente piață electricitate (notă)]] · actor/retail/FCEE concepts · [[Energetică — prosumer vs consumator activ (notă)]] |
| 3 | Gas market hub | **Done (2026-08-07)** — [[MOC — Piața gazelor naturale]] · [[Energetică — segmente piață gaze (notă)]] · [[Concept — Punct virtual de tranzacționare]] |
| 4 | Petroleum + coal gap | **Done (2026-08-07)** — [[MOC — Piața produselor petroliere]] · [[Energetică — segmente piață petrol (notă)]] · [[Concept — Preț maxim ANRE produse petroliere]] · [[Energetică — cărbune gap stub (notă)]] |
| 5 | Thermal / CHP + geothermal stub | **Done (2026-08-07)** — [[MOC — Piața energiei termice]] · [[Energetică — segmente piață termică (notă)]] · [[Concept — Cogenerare de înaltă eficiență]] · [[Energetică — geotermal gap stub (notă)]] |
| 6 | Biofuels / hydrogen | **Next: Step 6** |
| 7 | Prosumers · incentives · ESG notes | Queued |
| 8 | Synthesis retune to this spine | After Step 6–7 have substance |

**Immediate next work (Step 6):** biofuels hub from [[HG 53-2025 — durabilitate biocarburanti emisii GES (notă)|HG 53]] + hydrogen watch-list stub.


## Related
[[Roadmap — Energy analysis architecture]] · [[MOC — Piața de energie electrică]] · [[MOC — Piața gazelor naturale]] · [[MOC — Piața produselor petroliere]] · [[MOC — Piața energiei termice]] · [[Energetică — cărbune gap stub (notă)]] · [[Energetică — geotermal gap stub (notă)]] · [[Energetică — synthesis]] · [[MOC — Energetică]] · [[ANRE]] · [[Legea 164-2025 — energia electrica (notă)]] · [[Legea 174-2017 — energetica (notă)]] · [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)]]
