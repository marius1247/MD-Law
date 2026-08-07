---
title: "MOC — Piața de energie electrică"
type: moc
domeniu: [energetică, energie-electrică, piață]
tags: [moc, index, energetică, piață]
status: draft
created: 2026-07-28
updated: 2026-08-07
---

# MOC — Piața de energie electrică

Regulation-oriented map of Moldova’s **electricity markets**: segments, actors, regulated activities, and the acts that bind them.

Architecture spine: [[Energetică — architecture map]] · **Segment briefs:** [[Energetică — segmente piață electricitate (notă)]] · Master inventory: [[MOC — Energetică]] · Narrative: [[Energetică — synthesis]] · Sector dossier: [[Energetică — sector electricitate ANRE (notă)]]

> [!danger] Frame law is L164/2025 — not L107/2016
> [[Legea 164-2025 — energia electrica (text)|L164/2025]] repealed L107/2016 on 19.08.2025. Market rules [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)|HANRE 283/2020]] (as amended by [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (notă)|383/2026]]) still cite L107 enabling articles — **currency risk** until full re-adoption under L164.

---

## 1. Governing stack (how the acts talk)

| Tier | Act | Role for the market |
|---|---|---|
| Treaty | [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)\|L117/2009]] | EnC acquis obligation (Dir. 2019/944, Reg. 2019/943, REMIT, CACM — adapted) |
| Framework | [[Legea 174-2017 — energetica (notă)\|L174/2017]] | ANRE independence; who may regulate |
| Sectoral market | **[[Legea 164-2025 — energia electrica (notă)\|L164/2025]]** | Actors, licensing catalogue, market principles, PSO, coupling, REMIT |
| Support bridge | [[Legea 10-2016 — surse regenerabile (notă)\|L10/2016]] | Eligible producers, net billing — revenue side; trading still under L164/HANRE 283 |
| Efficiency bridge | [[Legea 139-2018 — eficienta energetica (notă)\|L139/2018]] | Demand-response / obligated parties — route flexibility through L164 |
| Market rules | [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)\|HANRE 283/2020]] + [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (notă)\|383/2026]] | Operational segments, scheduling, settlement |
| Balancing T&Cs | [[HANRE 853-2025 — clauze echilibrare FSE si PRE (notă)\|HANRE 853/2025]] | FSE + PRE contract terms (**IF 1 Jul 2026**) |
| Network / connection | [[HANRE 423-2019 — Codul retelelor electrice (notă)\|423]] · [[HANRE 656-2021 — modificare Codul retelelor electrice (notă)\|656]] · [[HANRE 311-2026 — racordarea la retelele electrice (notă)\|311]] | Physical access that makes market participation possible |
| Supply retail | [[HANRE 169-2019 — furnizarea energiei electrice (notă)\|HANRE 169/2019]] | Retail / FUO / prosumer annex (currency flags) |
| Tariffs | [[MOC — Tarife și metodologii ANRE]] | T/D regulated prices — monopoly layer, not wholesale trading |
| Procurement bridge | [[Legea 74-2020 — achizitii sectoriale (notă)\|L74/2020]] | Market-based procurement incl. losses (HANRE 24 abrogated) |

Horizontal logic: **L164 creates the market; HANRE 283 runs it; L10 changes who gets paid a support price; network codes decide who can inject/withdraw; L74 decides how licensed utilities buy.** Full bridge table: [[Energetică — architecture map]] §1.2.

---

## 2. Market segments (regulatory view)

| Segment | MD name | Who operates / clears | Governing ops rules | Status in analysis |
|---|---|---|---|---|
| Long-term bilaterals | Piața contractelor bilaterale (OTC) | Parties + OPEE registration | HANRE 283 Titlul II | Brief ✅ [[Energetică — segmente piață electricitate (notă)\|segments §1]] |
| Organised bilaterals | **POCB** | OPEE | HANRE 283 · [[Concept — Piața organizată a contractelor bilaterale]] | Brief ✅ · Concept ✅ |
| Day-ahead | **PZU** | OPEE → **[[Concept — OPEED\|OPEED]]** | HANRE 283 Titlul III · L164 CACM | Brief ✅ |
| Intraday | **PI** | OPEE / OPEED | HANRE 283 Titlul IV (383: PPZ→PI) | Brief ✅ |
| Balancing | Piața de echilibrare | **OST** (Moldelectrica) | HANRE 283 Titlul VI · HANRE 853 | Brief ✅ · [[Concept — Parte responsabilă de echilibrare]] · [[Concept — Furnizor de servicii de echilibrare]] |
| System services | Servicii de sistem | OST | HANRE 283 Titlul VII | Brief ✅ |
| Capacity / adequacy | Adequacy / capacity mechanisms | Policy + ANRE / OST (L164 arts. 49–51) | Legal toolbox only — no live capacity market | Brief ✅ *(stub verdict)* |
| Regulated central offtake | **[[Concept — Furnizor central de energie electrică\|FCEE]]** purchases (RES + urban CHP) | Designated central supplier | L164 · L10 · HANRE 283 special lane | Brief ✅ · Concept ✅ · [[Concept — Producător eligibil]] |
| Universal / last-resort supply | Serviciu universal · **FUO** | Designated suppliers | L164 arts. 17, 114–115 · HANRE 169 | Brief ✅ · [[Concept — Furnizor de ultimă opțiune]] |
| Flexibility / aggregation / storage | New L164 activities | Licensed aggregators, storage operators, active consumers, CECs | L164 primary; HANRE lag | Brief ✅ · concepts ✅ · boundary [[Energetică — prosumer vs consumator activ (notă)]] |

Economic spine: nominate a schedule → deviate → pay imbalance. BRP is the hinge ([[Concept — Parte responsabilă de echilibrare]]). Cross-vault economics: [[FP — Marginal Pricing in Electricity Markets]] (GeoMacro).

---

## 3. Actors

| Actor | Role | Primary source |
|---|---|---|
| **OPEE / [[Concept — OPEED\|OPEED]]** | Organised markets (PZU, PI, POCB); coupling designation under L164 | L164 · HANRE 283 |
| **OST** (Î.S. Moldelectrica) | Transmission, balancing market, system services, physical notifications interface | L164 · HANRE 283 · 316 · 853 |
| **OSD** | Distribution; market participant mainly for losses / technological consumption | L164 · HANRE 64 · 94 · 537 |
| **Producers** | Injection; may need eligible-producer status for support | L164 · L10 |
| **Suppliers** | Wholesale + retail; often BRP for customers / prosumers | L164 · HANRE 169 |
| **Traders** | Licensed trading (L164 new catalogue) | L164 |
| **FCEE** | Central offtake of eligible RES / urban CHP at regulated prices | L164 · L10 · [[Concept — Furnizor central de energie electrică]] |
| **FUO / universal service supplier** | PSO retail | L164 · [[Concept — Furnizor de ultimă opțiune]] |
| **PRE / BRP** | Financial responsibility for imbalances | HANRE 283 · 853 · [[Concept — Parte responsabilă de echilibrare]] |
| **FSE** | Balancing energy / capacity provider | HANRE 853 · [[Concept — Furnizor de servicii de echilibrare]] |
| **[[Concept — Agregator independent\|Agregator independent]]** | Aggregation not affiliated to customer’s supplier | L164 · [[Concept — Agregator independent]] |
| **[[Concept — Consumator activ\|Consumator activ]] / [[Concept — Comunitate de energie a cetățenilor\|CEC]]** | Self-consume, store, share, sell, flexibility — not main business | L164 arts. 122–126 |
| **[[Concept — Stocare a energiei\|Storage operator]]** | Regulated activity under L164 (≥ 1 MW gate) | L164 arts. 16–18, 34, 63 |
| **ANRE** | Licensing, market rules approval, REMIT monitoring, tariffs | [[ANRE]] · L174 · L164 |
| Final customers | Retail choice, dynamic-price contracts (L164), protection rules | L164 · HANRE 169 |

---

## 4. Regulated activities (licensing catalogue — L164 era)

Full inventory + thresholds: **[[Energetică — segmente piață electricitate (notă)]] §B**.

L164 arts. 16–18 catalogue: production · **storage** · market operation · transmission · centralised dispatch · distribution · **trading** · supply · **aggregation**.

| Activity | Notes |
|---|---|
| Generation | ≥ 5 MW licence gate (art. 18(2)) |
| Transmission / distribution | Natural monopoly + unbundling |
| Supply | Incl. universal / FUO designations; EV charging ≠ supply |
| **Trading** | Wholesale-only licence (10y) |
| **Aggregation** | Incl. [[Concept — Agregator independent\|independent aggregator]] status |
| **Storage** | ≥ 1 MW autonomous injection → [[Concept — Stocare a energiei]] |
| Market operation (OPEE/[[Concept — OPEED\|OPEED]]) | Single national licence + ANRE designation for coupling |

> [!danger] HANRE 286 is not the licensing regulation
> [[HANRE 286-2018 — licentiere energie (notă)|HANRE 286/2018]] is the **tariff application procedure**. Licensing doctrine: [[Concept — Licență în energetică]] + L164 arts. 18–23. Dedicated L164 licensing secondary act still a **gap to watch**.

Separate gate from licensing: **connection** ([[Concept — Racordare la rețea]] · [[MOC — Racordare și acces la rețele]] · HANRE 311/2026).

---

## 5. Monopoly layer (feeds the market but is not a “segment”)

- Connection & access — [[MOC — Racordare și acces la rețele]]
- Network code — HANRE 423 / 656
- Dispatch — [[HANRE 316-2018 — dirijare dispecerat sistem electroenergetic (notă)|HANRE 316/2018]] *(L107 currency)*
- QoS — [[HANRE 537-2020 — calitate servicii transport distributie EE (notă)|HANRE 537]] · [[Concept — Indicatori de calitate SAIDI SAIFI]]
- Tariffs — [[MOC — Tarife și metodologii ANRE]] · [[Concept — Tarif de transport]] · [[Concept — Tarif de distribuție]] · [[Concept — Unbundling]]

---

## 6. Support, prosumers, crisis (bridges out of pure wholesale)

| Theme | Acts / concepts | Hub later |
|---|---|---|
| Eligible producers / fixed tariff / auctions | L10 · HANRE 375 · HG 26 · HG 599 | Incentives layer (Step 7) |
| Prosumers / net billing | L10 · HANRE 833 Anexa 5 · HANRE 169 · [[Concept — Facturare netă]] | Prosumer layer (Step 7) |
| Active consumers / CEC | L164 | Same |
| Vulnerability / social | [[Legea 241-2022 — Fond reducere vulnerabilitate energetica (notă)\|L241]] | Incentives / social |
| Electroenergetic emergency | [[HG 820-2024 — situatii exceptionale electroenergetic (notă)\|HG 820]] · [[Concept — Situație excepțională electroenergetică]] | Crisis — do not mix with petroleum L101 |
| Climate / ESG frame | [[HG 10-2024 — guvernanta energetica si actiuni climatice (notă)\|HG 10]] · [[HG 86-2025 — PNIEC 2025-2030 (notă)\|PNIEC]] | ESG layer (Step 7) |

---

## 7. Concepts (electricity market)

**Live:** [[Concept — Parte responsabilă de echilibrare]] · [[Concept — Furnizor de servicii de echilibrare]] · [[Concept — Piața organizată a contractelor bilaterale]] · [[Concept — OPEED]] · [[Concept — Consumator activ]] · [[Concept — Agregator independent]] · [[Concept — Stocare a energiei]] · [[Concept — Comunitate de energie a cetățenilor]] · [[Concept — Contract la prețuri dinamice]] · [[Concept — Furnizor central de energie electrică]] · [[Concept — Furnizor de ultimă opțiune]] · [[Concept — Producător eligibil]] · [[Concept — Facturare netă]] · [[Concept — Licență în energetică]] · [[Concept — Unbundling]] · [[Concept — Racordare la rețea]] · [[Concept — Situație excepțională electroenergetică]]

**Boundary note:** [[Energetică — prosumer vs consumator activ (notă)]]

---

## 8. Professional legal analysis (risk matrix)

Lifted from [[Legea 164-2025 — energia electrica (notă)|L164 act-note]] §8 and hardened against operative text. Full segment-level advice: [[Energetică — segmente piață electricitate (notă)]] §E. Cross-vector rules: [[Energetică — architecture map]] §1.3.

| Issue | Flaw / ambiguity | Practical risk | Advice rule |
|---|---|---|---|
| **FUO duration** | L164 art. **115(1)** — consumers entitled to last-resort supply for **≥ 6 months**; HANRE 169 pts. 7/67/71 still say **≤ 90 days** (cites repealed L107 art. 73) | Wrong consumer-exit / supplier takeover advice | **Apply L164**; treat 169 timings as stale until supply regulation re-adopted |
| **US vs FUO** | Cleanly separated on L164 face (arts. 114–115): US = standing entitlement for households + micro/small; FUO = supplier-failure contingency | Conflating portfolios → wrong designation / procurement | Re-screen customer books against art. 114(1) perimeter; FUO is not a permanent industrial fallback |
| **REMIT** | Outages / capacity / inside information; registration before wholesale trading; ANRE portal + investigation powers | Manipulation / failure-to-publish liability | REMIT SOP + registration **before** first trade — parallel to art. 18 licence ([[Energetică — licențiere cross-border și REMIT (notă)]]) |
| **Flexible connection** | Art. 2 pt. 2 — limitation/control of injection built into connection | Bankability fights; curtailment unpriced | Price curtailment in PPA; operationalise via [[HANRE 311-2026 — racordarea la retelele electrice (notă)\|311]] · [[Concept — Racordare la rețea]] |
| **FCEE sunset** | Art. **150(3)** RES→CfD ends FCEE buy/resell + supplier purchase; art. **150(4)** ANRE calendar for **urban CHP** exit (duty by 1 Jan 2026) | Stranded offtake assumptions | Cite art. 87(2) + 150(3)–(4); calendar ≠ automatic cut-off — [[Concept — Furnizor central de energie electrică]] |
| **Tier-3 under L107** | 283 / 169 / 316 still L107-origin *temei* | Ultra vires / transitional uncertainty | Prefer post-L164 acts; where conflict, **statute wins** |
| **L107 legacy projects** | Non-retroactivity + pre-19.08.2025 design rule | Wrong connection/plant law applied | Ask: admitted under L107? designed before cutover? |
| **Capacity mechanism** | Arts. 49–51 toolbox only | Fake “capacity revenue” opinions | No live capacity market until HG + EnC opinion path |
| **HANRE still expected** | Aggregation reg (120(9)), CEC register (125), energy sharing (123), supply-reg update (119) | Advising from silence | Statute-first; legacy HANRE only where non-conflicting |
| **Procurement** | Market-based purchase incl. losses restored; HANRE 24 abrogated | Citing repealed procurement HANRE | Use [[Legea 74-2020 — achizitii sectoriale (notă)\|L74]] / market rules |

**Four gates (never collapse):** licence (arts. 16–18) · connection (311) · support/eligibility (L10 / FCEE) · REMIT registration.

---

## 9. Open threads for this hub

1. ✅ Segment briefs + licensing inventory — [[Energetică — segmente piață electricitate (notă)]]
2. ✅ Dynamic-price / FCEE concepts + prosumer↔active-consumer boundary
3. ✅ Professional risk matrix (§8) — FUO conflict, REMIT, flexible connection, FCEE art. 150 hardened
4. Currency: HANRE 283 *temei* still L107; track ANRE re-adoption
5. ✅ Capacity: legal toolbox (arts. 49–51), **no live capacity market** until HG
6. Watch for dedicated L164 licensing secondary act (do not use HANRE 286)
7. ANRE regulations still expected: aggregation (art. 120(9)), CEC register (art. 125), energy sharing (art. 123), supply-reg update for art. 119
8. Step 7: expand prosumer/active-consumer layer from the boundary note
9. Incomplete sources: HANRE 169 truncates past ~pt. 146; 423 parent annex incomplete (656 supplies Parts I–V); HG 820 annexes 1–2 missing

## Related
[[Energetică — segmente piață electricitate (notă)]] · [[Energetică — prosumer vs consumator activ (notă)]] · [[Energetică — architecture map]] · [[Roadmap — Energy analysis architecture]] · [[MOC — Energetică]] · [[MOC — Racordare și acces la rețele]] · [[MOC — Tarife și metodologii ANRE]] · [[Energetică — sector electricitate ANRE (notă)]] · [[Energetică — licențiere cross-border și REMIT (notă)]] · [[ANRE]]
