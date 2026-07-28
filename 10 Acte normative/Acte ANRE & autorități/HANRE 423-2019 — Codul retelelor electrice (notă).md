---
title: HANRE 423-2019 — Codul retelelor electrice (notă)
type: act-note
act: '[[HANRE 423-2019 — Codul retelelor electrice (text)]]'
domeniu:
- energetică
- energie-electrică
- rețele
enabling_act: '[[Legea 164-2025 — energia electrica (text)]]'
eu_directives: ENTSO-E grid code principles; Regulation (EU) 2019/943
analysis_tier: law-house
tags:
- act-note
- analysis
- energetică
- rețele
- ANRE
- acte_normative
status: draft
created: 2026-07-28
updated: 2026-07-28
domain: energie_electrica
issuer: ANRE
legal_status: in_vigoare
last_amended: '2026-07-28'
---

# HANRE nr. 423/2019 — Codul rețelelor electrice — Analysis

**Raw text:** [[HANRE 423-2019 — Codul retelelor electrice (text)]] ⚠️ *decision only — annex missing* · **Electricity law:** [[Legea 164-2025 — energia electrica (notă)]] · **Connection:** [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] · **Hub:** [[MOC — Energetică]]

> [!danger] Annex not in vault
> Only the approving decision is ingested. The substantive **Codul rețelelor electrice** (network code annex) must be downloaded separately from [legis.md](https://www.legis.md/cautare/getResults?lang=ro&doc_id=151929). Analysis below is based on the decision text, cross-references in other acts, and the Batch 2 Law House dossier. **Do not cite specific technical parameters without verifying the annex.**

> [!abstract] Executive summary & commercial impact
> **Core purpose:** Mandatory technical operational requirements for system security — grid frequency, voltage stability, dispatch protocols, fault ride-through, and technical connection parameters across HV/MV/LV networks.
> **Primary business risk:** Curtailment or immediate disconnection of generation facilities (especially renewables) for technical non-compliance; uncompensated emergency curtailment under broad TSO discretion.

---

## 1. Statutory hierarchy & legal foundation

* **Primary legal basis:** Originally issued under [[Legea 107-2016 — energia electrica (text)|L107/2016]] arts. 53(4) and 96(8); enabling basis now under [[Legea 164-2025 — energia electrica (text)|L164/2025]] network-code provisions.
* **Procedural subordination:** Technical admission disputes → ANRE under [[Legea 174-2017 — energetica (notă)]] art. 18; judicial review → [[Codul administrativ 116-2018 (notă)]].
* **EU acquis alignment:** Aligned with ENTSO-E grid code parameters and Regulation (EU) 2019/943 system-operation requirements.
* **Inter-relation:** Works in tandem with [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] for technical admission into operation after connection.

---

## 2. Practical legal mechanics & key provisions

*Based on decision text and operational cross-references — verify against annex when available.*

### A. Grid connection technical requirements

* **Frequency & voltage tolerances:** Power plants must retain active power output during specified frequency variations.
* **Fault ride-through (FRT):** Wind and solar facilities must withstand temporary voltage dips without disconnecting.
* **Inverter compliance:** Solar inverters must meet certification standards referenced in the network code — international test certificates may be rejected if not explicitly aligned with ENTSO-E parameters.

### B. Dispatching & operational management

* **TSO dispatch instructions:** Î.S. Moldelectrica holds ultimate operational control for balancing and system restoration.
* **Plants >1 MW:** Must follow TSO dispatch orders; non-compliance triggers disconnection.
* **SCADA/telemetry:** Mandatory data links to TSO/DSO control centres before energisation.

### C. Amendments

* HANRE 646/2025 (in force 09.12.2025) amends the code — check current consolidation before relying on pre-2025 technical parameters.

---

## 3. Legal ambiguities, vulnerabilities & risk matrix

| Provision | Identified flaw / ambiguity | Practical risk | Recommended strategy |
| :--- | :--- | :--- | :--- |
| **Emergency curtailment** | Broad TSO discretion under "system emergency" declarations without clear compensation | Revenue loss for renewable operators without compensation mechanism | Log all TSO dispatch orders; verify against [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]] market rules; challenge non-discriminatory curtailment via ANRE |
| **Inverter certification** | Evolving compliance requirements during commissioning | Operational delay from rejection of international testing certificates | Pre-audit inverter documentation against ENTSO-E parameters referenced in code |
| **Annex availability** | Network code annex not publicly ingested in vault | Advice based on incomplete technical parameters | Download annex from legis.md; flag `text_complet: false` until ingested |
| **L107 → L164 transition** | Code adopted under repealed electricity law | Currency risk for new market entrants post-August 2025 | Cross-check L164 network-code enabling articles; monitor ANRE re-adoption |

---

## 4. Relevant jurisprudence & ANRE practice

* **ANRE technical commission:** Oversees disputes regarding emergency curtailments; TSOs must provide SCADA log evidence justifying emergency disconnections.
* **Grid connection practice:** ANRE holds that DSOs cannot impose off-site network reinforcement costs on single applicants unless under approved co-financing — technical standards in the network code must not be used to shift capital expenditure.

---

## 5. Client action checklist / compliance roadmap

- [ ] Download and ingest the network code annex from legis.md doc_id `151929`.
- [ ] Audit inverter and protection relay settings against ENTSO-E grid code parameters before commissioning tests.
- [ ] Establish telemetry and SCADA data links with TSO/DSO control centre before requesting energisation.
- [ ] Log all TSO dispatch/curtailment orders with timestamps for potential imbalance or compensation disputes.
- [ ] Pair technical compliance review with connection permit under [[HANRE 311-2026 — racordarea la retelele electrice (notă)]].

---

## 6. Connections in the vault

* **Electricity law:** [[Legea 164-2025 — energia electrica (notă)]]
* **Connection regulation:** [[HANRE 311-2026 — racordarea la retelele electrice (notă)]]
* **Market rules:** [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]]
* **Gas equivalent:** [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)]]
* **Ingestion status:** [[Status ingestie — Energetica]]

---

## Sources

[[HANRE 423-2019 — Codul retelelor electrice (text)]] — legis.md doc_id `151929`, decision only (`continut: doar-dispozitiv`, `text_complet: false`). Annex ingestion pending.
