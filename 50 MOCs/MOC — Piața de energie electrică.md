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

Architecture spine: [[Energetică — architecture map]] · Master inventory: [[MOC — Energetică]] · Narrative: [[Energetică — synthesis]] · Sector dossier: [[Energetică — sector electricitate ANRE (notă)]]

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
| Long-term bilaterals | Piața contractelor bilaterale (OTC) | Parties + OPEE registration | HANRE 283 Titlul II | Concept seed: civil contract + market registration |
| Organised bilaterals | **POCB** | OPEE | HANRE 283 · [[Concept — Piața organizată a contractelor bilaterale]] | Concept ✅ |
| Day-ahead | **PZU** | OPEE → **OPEED** under L164 coupling path | HANRE 283 Titlul III · L164 CACM | Brief ⏳ Step 2 |
| Intraday | **PI** | OPEE / OPEED | HANRE 283 Titlul IV (383: PPZ→PI) | Brief ⏳ Step 2 |
| Balancing | Piața de echilibrare | **OST** (Moldelectrica) | HANRE 283 Titlul VI · HANRE 853 | [[Concept — Parte responsabilă de echilibrare]] · [[Concept — Furnizor de servicii de echilibrare]] |
| System services | Servicii de sistem | OST | HANRE 283 Titlul VII | Brief ⏳ Step 2 |
| Capacity / adequacy | Adequacy / capacity mechanisms | Policy + ANRE / OST (L164 defs) | L164 vocabulary; operational depth TBD | Stub — confirm whether a live MD capacity market exists beyond adequacy planning |
| Regulated central offtake | **FCEE** purchases (RES + urban CHP) | Designated central supplier | L164 · L10 · HANRE 283 special lane | Bridge to [[Concept — Producător eligibil]] |
| Universal / last-resort supply | Serviciu universal · **FUO** | Designated suppliers | L164 arts. 17, 114–115 · HANRE 169 | [[Concept — Furnizor de ultimă opțiune]] |
| Flexibility / aggregation / storage | New L164 activities | Licensed aggregators, storage operators, active consumers | L164 primary; HANRE lag | Concepts ⏳ Step 2 |

Economic spine: nominate a schedule → deviate → pay imbalance. BRP is the hinge ([[Concept — Parte responsabilă de echilibrare]]). Cross-vault economics: [[FP — Marginal Pricing in Electricity Markets]] (GeoMacro).

---

## 3. Actors

| Actor | Role | Primary source |
|---|---|---|
| **OPEE / OPEED** | Organised markets (PZU, PI, POCB); coupling designation under L164 | L164 · HANRE 283 |
| **OST** (Î.S. Moldelectrica) | Transmission, balancing market, system services, physical notifications interface | L164 · HANRE 283 · 316 · 853 |
| **OSD** | Distribution; market participant mainly for losses / technological consumption | L164 · HANRE 64 · 94 · 537 |
| **Producers** | Injection; may need eligible-producer status for support | L164 · L10 |
| **Suppliers** | Wholesale + retail; often BRP for customers / prosumers | L164 · HANRE 169 |
| **Traders** | Licensed trading (L164 new catalogue) | L164 |
| **FCEE** | Central offtake of eligible RES / urban CHP at regulated prices | L164 · L10 |
| **FUO / universal service supplier** | PSO retail | L164 · [[Concept — Furnizor de ultimă opțiune]] |
| **PRE / BRP** | Financial responsibility for imbalances | HANRE 283 · 853 · [[Concept — Parte responsabilă de echilibrare]] |
| **FSE** | Balancing energy / capacity provider | HANRE 853 · [[Concept — Furnizor de servicii de echilibrare]] |
| **Agregator independent** | Aggregation not affiliated to customer’s supplier | L164 def. — concept ⏳ |
| **Consumator activ / CEC** | Self-consume, store, share, sell, flexibility — not main business | L164 — concept ⏳ |
| **Storage operator** | Regulated activity under L164 | L164 — concept ⏳ |
| **ANRE** | Licensing, market rules approval, REMIT monitoring, tariffs | [[ANRE]] · L174 · L164 |
| Final customers | Retail choice, dynamic-price contracts (L164), protection rules | L164 · HANRE 169 |

---

## 4. Regulated activities (licensing catalogue — L164 era)

L164 expands the catalogue beyond the old L107 set. Working list for analysis (verify article numbers against current consolidation before advising):

| Activity | Notes |
|---|---|
| Generation | Still core |
| Transmission / distribution | Natural monopoly + unbundling |
| Supply | Incl. universal / FUO designations |
| **Trading** | Explicit L164 addition |
| **Aggregation** | Incl. independent aggregator |
| **Storage** | Explicit L164 addition |
| Market operation (OPEE/OPEED) | Designation / licence path under L164 |
| Cross-border related roles | See [[Energetică — licențiere cross-border și REMIT (notă)]] |

Operational licence procedure still largely rides on [[HANRE 286-2018 — licentiere energie (notă)|HANRE 286/2018]] — **re-check enabling articles** against L164. Concept: [[Concept — Licență în energetică]].

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

**Live:** [[Concept — Parte responsabilă de echilibrare]] · [[Concept — Furnizor de servicii de echilibrare]] · [[Concept — Piața organizată a contractelor bilaterale]] · [[Concept — Furnizor de ultimă opțiune]] · [[Concept — Producător eligibil]] · [[Concept — Facturare netă]] · [[Concept — Licență în energetică]] · [[Concept — Unbundling]] · [[Concept — Racordare la rețea]] · [[Concept — Situație excepțională electroenergetică]]

**Queued (Step 2):** OPEED · consumator activ · comunitate de energie cetățenească · agregator independent · stocare a energiei · contracte la prețuri dinamice

---

## 8. Open threads for this hub

1. Segment briefs for PZU / PI / system services / capacity (Step 2)
2. Currency: HANRE 283 *temei* still L107; track ANRE re-adoption
3. Confirm live MD **capacity market** vs adequacy planning language only
4. Align HANRE 286 licensing list with L164 catalogue
5. Prosumer vs active-consumer boundary note (feeds Step 7)

## Related
[[Energetică — architecture map]] · [[Roadmap — Energy analysis architecture]] · [[MOC — Energetică]] · [[MOC — Racordare și acces la rețele]] · [[MOC — Tarife și metodologii ANRE]] · [[Energetică — sector electricitate ANRE (notă)]] · [[ANRE]]
