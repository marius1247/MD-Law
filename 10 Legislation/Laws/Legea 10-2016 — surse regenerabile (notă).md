---
title: Legea 10-2016 — surse regenerabile (notă)
type: act-note
act: '[[Legea 10-2016 — surse regenerabile (text)]]'
domeniu:
- energetică
- regenerabile
tags:
- act-note
- analysis
- energetică
- regenerabile
- acte_normative
enabling_act: '[[Legea 174-2017 — energetica (text)]]'
eu_directives: Directive (EU) 2018/2001 (RED); amended by Law 329/2023 (net billing)
analysis_tier: law-house
status: draft
created: 2026-07-23
updated: 2026-08-06
domain: energie_regenerabila
issuer: Parlament
legal_status: in_vigoare
last_amended: '2026-07-28'
---

# Legea nr. 10/2016 privind promovarea utilizării energiei din surse regenerabile — Analysis

**Raw text:** [[Legea 10-2016 — surse regenerabile (text)]] ✅ *complete (45 arts + bis; consolidated LP227/2025)* · **Hub:** [[MOC — Energetică]] · **Synthesis:** [[Energetică — synthesis]]

> [!success] Text status
> Full consolidated text is in the vault (manual ingest 2026-07-23). Older notes claiming truncation at Art. 34 are obsolete — see [[Status ingestie — Energetica]].

## What it is
The renewables support statute. It does four things: sets **targets**, defines who qualifies as an [[Concept — Producător eligibil|eligible producer]], establishes the **support scheme**, and creates the administrative apparatus (quotas, guarantees of origin, reporting).

## The support architecture

**Two tracks, split by capacity.**
- **Below the threshold** — administrative grant of eligible-producer status against a quota, with a **fixed tariff** set by ANRE under [[HANRE 375-2017 — Metodologie tarife regenerabile (text)|methodology 375/2017]].
- **Above the threshold** — **competitive tender**, bids capped by a **ceiling price**.

**The quota is the binding constraint.** Government sets a capacity quota per technology and category; support is available only within it. This converts renewable development into a race, and makes queue position and connection capacity the real currency of the sector. → [[Concept — Racordare la rețea]]

**Prosumers** are handled separately by **net metering / net billing** — surplus injected is set off against consumption over a settlement period. No quota competition, no tariff support, much lower administrative burden.

> The capacity threshold, quota volumes and ceiling prices are all set administratively and revised. **Never rely on a figure from a note** — check the current Government decision and the current ANRE decision.

## Why the support level is not the interesting question
Moldova's constraint on renewables is **system integration**, not incentive strength:

- A small system with limited flexible capacity and thin balancing reserves. Intermittent output is disproportionately expensive to accommodate.
- Post-2022 synchronisation with **ENTSO-E via Romania** reshaped both the interconnection profile and the balancing options — a structural improvement, but it changes the analysis rather than removing the constraint.
- Consequence: **curtailment risk and balancing exposure** are the material risks in a Moldovan renewable project, and neither is addressed by this statute. → [[Concept — Parte responsabilă de echilibrare]]

The 2025 connection-permit **financial guarantee for plants above 200 kW** is a direct response to the same underlying scarcity: capacity is the rationed good, and holding it was free.

## Practical sequence for a project
1. Confirm quota headroom for the technology and capacity band
2. Secure the **connection permit** — capacity, cost allocation, expiry, guarantee
3. Obtain **eligible-producer status** (administrative or through the auction)
4. Fix the **offtake** — guaranteed purchase or PPA
5. Allocate **imbalance risk** in the PPA — who is BRP, who wears the cost
6. Track **guarantees of origin** separately from the energy

Steps 2 and 5 are where projects fail. Step 3 is where clients think the risk is.

## How it connects
- Support price flows through the tariff system → [[Concept — Tarif reglementat]] · pricing algorithm layer [[HANRE 375-2017 — Metodologie tarife regenerabile (notă)]] ⚠️ annex missing
- Market participation, dispatch, priority, balancing and offtake sit in **[[Legea 164-2025 — energia electrica (notă)|L164/2025]]** (not repealed [[Legea 107-2016 — energia electrica (text)|L107/2016]]) and [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)|market rules]] / [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (notă)|383/2026 POCB]]
- Connection queue / >200 kW guarantee → [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] · [[Concept — Racordare la rețea]]
- The EU frame is the Renewable Energy Directive as applied through the **Energy Community**; expect movement toward the RED II/III architecture — auctions as default, self-consumption and renewable energy communities as new categories

## Net billing transition (Law 329/2023)

| Regime | Period | Mechanism |
|---|---|---|
| **Net metering** (*contorizare netă*) | Pre-2024 | Physical kWh-for-kWh netting monthly/annually |
| **Net billing** (*facturare netă*) | From 01.01.2024 | Monetary netting: injection valued at day-ahead/bilateral market average price |
| **Legacy rights** | Installations active before 31.12.2023 | Retain net metering until 31.12.2027 (art. 39¹ transitional clauses) |

Commercial prosumers: model self-consumption above 70%; deploy BESS to minimise grid injection during low-price hours.

## Legal ambiguities, vulnerabilities & risk matrix

| Provision | Identified flaw / ambiguity | Practical risk | Recommended strategy |
| :--- | :--- | :--- | :--- |
| **Art. 10, 35 (capacity quotas)** | Quota exhaustion without transparent public registry | Project stranded after land/grid investment | Pre-audit ANRE quota availability before eligible-producer application |
| **Art. 37² (commissioning deadline)** | 24-month deadline with DSO grid delays beyond developer control | Bank guarantee forfeiture | File extension request before expiry; invoke CA arts. 21–25 proportionality |
| **Art. 36¹ (bank guarantees)** | Strict 15-day deposit after ANRE decision | Automatic nullification of eligible status | Pre-clear SWIFT/LC formats with ANRE legal department |
| **Art. 39¹ (net billing price)** | Injection valued at volatile market prices | Revenue uncertainty for commercial prosumers | Optimise self-consumption; deploy storage |

## Client action checklist / compliance roadmap

- [ ] Confirm quota headroom for technology and capacity band before application.
- [ ] Secure connection permit — verify capacity, cost allocation, expiry, and >200 kW financial guarantee.
- [ ] Obtain eligible-producer status (administrative or auction) within available quotas.
- [ ] Execute 15-year PPA with S.A. Energocom; allocate BRP/imbalance risk explicitly.
- [ ] For prosumers: execute amended supply contract for monetary netting under net billing.
- [ ] Track guarantees of origin separately from energy offtake.

## Open questions
- Current quota and ceiling price — verify at [ANRE](https://anre.md) and Government decision.
- Whether the 200 kW guarantee reaches existing permit holders.
- Eligible-producer confirmation procedures — HANRE 251/2019 not yet ingested.

## Sources
[[Legea 10-2016 — surse regenerabile (text)]] — legis.md complete consolidation (LP227/2025).
