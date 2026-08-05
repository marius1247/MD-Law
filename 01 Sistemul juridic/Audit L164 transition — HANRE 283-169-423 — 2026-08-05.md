---
title: "Audit L164 transition — HANRE 283-169-423"
type: reference
domeniu: [energetică, meta]
tags: [reference, meta, audit, L164, ANRE]
created: 2026-08-05
updated: 2026-08-05
status: reviewed
---

# L164 transition audit — HANRE 283/2020, 169/2019, 423/2019

**Question:** Are the three pre-L164 electricity HANRE acts still operative under [[Legea 164-2025 — energia electrica (text)|L164/2025]], or are they transitional / abrogated / needing re-adoption?

**Related:** [[Audit currency — Phase A — 2026-08-05]] · [[Status ingestie — Energetica]] · [[Energetică — sector electricitate ANRE (notă)]]

---

## Transition map (electricity)

| Layer | Old anchor | Current anchor | Vault status |
|---|---|---|---|
| Primary law | [[Legea 107-2016 — energia electrica (text)|L107/2016]] **abrogated** 19.08.2025 | [[Legea 164-2025 — energia electrica (text)|L164/2025]] | ✅ complete |
| Connection | [[HANRE 168-2019 — racordarea la retelele electrice (text)|HANRE 168/2019]] **abrogated** | [[HANRE 311-2026 — racordarea la retelele electrice (text)|HANRE 311/2026]] | ✅ L164-based |
| Market rules | HANRE 283/2020 under L107 art. 7(3)(a) | L164 market-design articles + HANRE 383/2026 amend | ⚠️ see below |
| Supply | HANRE 169/2019 under L107 arts. 63(7), 96(23) | L164 retail / universal service articles | ❌ truncated + L107 refs |
| Network code | HANRE 423/2019 under L107 arts. 53(4), 96(8) | L164 multiple network-code hooks | ⚠️ partial annex |

---

## HANRE 283/2020 — Regulile pieței energiei electrice

| Field | Finding |
|---|---|
| **Vault text** | ✅ Complete annex (`legis_id` 155187, `text_complet: true`) |
| **Enabling citation in text** | art. 7(3)(a) **L107/2016** — repealed |
| **Latest amendment in vault** | HANRE **383/2026** — in force **01.07.2026** (terminology + market rules) |
| **L164 relationship** | L164 restructures market design (REMIT, CACM, active consumers). HANRE 283 remains the **operative market rulebook** in practice until ANRE issues a full L164-native replacement. |
| **Re-adoption check** | No vault evidence of wholesale repeal. ANRE site / legis.md should be checked for a new "Regulile pieței" issued expressly under L164. **383/2026** is an amendment, not a re-base. |
| **Operational verdict** | **Cite with L164 hierarchy** — treat as **transitional operative** under amended text. Update [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]] client checklists when L164-native market rules appear. |
| **Cross-links** | [[HANRE 383-2026 — modificare Regulile pietei energiei electrice (text)]] · [[Energetică — licențiere cross-border și REMIT (notă)]] |

---

## HANRE 169/2019 — Regulament privind furnizarea energiei electrice

| Field | Finding |
|---|---|
| **Vault text** | ❌ **Truncated** mid-sentence at pct. 146 (`legis_id` 114962, `text_complet: false`) |
| **Enabling citation** | arts. **63(7), 96(23) L107/2016** — repealed |
| **Body references** | Repeated citations to **L107/2016**, [[Legea 174-2017 — energetica (text)|L174/2017]], and **HANRE 168/2019** connection rules (superseded by HANRE 311/2026) |
| **L164 relationship** | L164 separates universal service / last-resort supplier / retail supply (see [[Legea 164-2025 — energia electrica (notă)]] §4). No L164-era replacement supply regulation ingested. |
| **Re-adoption check** | **Not found in vault.** HANRE 169/2025 in vault is a **different act** (water/sewerage investments — `doc_id` 148195). |
| **Operational verdict** | **Do not cite** from vault text beyond truncated portion. **Priority download:** complete HANRE 169/2019 annex from legis.md, then assess whether ANRE has issued L164-aligned supply rules. |
| **QoS companion** | HANRE 537/2020 (electricity QoS) — not ingested; pairs with supply regulation |

---

## HANRE 423/2019 — Codul rețelelor electrice

| Field | Finding |
|---|---|
| **Vault text (before Phase A)** | Decision only (`continut: doar-dispozitiv`) |
| **Vault text (after Phase A)** | Decision + **partial annex** from HANRE **656/2021** amendment insert (~2 800 lines) — see [[HANRE 423-2019 — Codul retelelor electrice (text)]] |
| **Enabling citation** | arts. **53(4), 96(8) L107/2016** — repealed |
| **Post-2025 amendment** | Header records HANRE **646/2025** (in force 09.12.2025) — "modul generator" substitutions; **not fully merged** into ingested annex body |
| **L164 relationship** | L164 references multiple network codes (connection, emergency/restoration, demand response). ANRE 2025 package may have **split** codes beyond single HANRE 423 annex. |
| **Operational verdict** | **Partially unblocked** for operational security / balancing chapters (PARTEA II–V from 656 insert). **Connection-code technical parameters** (PARTEA ÎNTÂI body) may still be incomplete vs official consolidare. Re-download **full consolidated annex** from legis.md when Cloudflare/manual access available. |
| **Cross-links** | [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] · [[Concept — Racordare la rețea]] |

---

## ANRE re-adoption checklist (manual — legis.md / anre.md)

For each act, confirm on primary source:

- [ ] **HANRE 283/2020** — still in force as amended by 383/2026; no separate L164 re-issue
- [ ] **HANRE 169/2019** — still in force or replaced; if replaced, ingest successor
- [ ] **HANRE 423/2019** — consolidated text includes 646/2025; check for **new** network codes under L164 package (emergency, connection sub-codes)
- [ ] **HANRE 422/2019** QoS — not in vault; ingest if 169 remains operative

---

## Vault actions taken (2026-08-05)

1. **HANRE 423** — merged partial annex from `supplement-hanre-656-2021-cod-retele-electric.md`; updated `continut`, `status_ingestie`, danger/warning callouts.
2. **This audit** — linked from [[Status ingestie — Energetica]] and [[MOC — Energetică]].
3. **HANRE 169** — remains flagged `text_complet: false`; no false progress.

---

## See also

[[Legea 164-2025 — energia electrica (notă)]] · [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] · [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)]] · [[HANRE 423-2019 — Codul retelelor electrice (notă)]]
