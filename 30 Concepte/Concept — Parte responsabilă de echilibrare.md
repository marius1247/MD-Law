---
title: "Concept — Parte responsabilă de echilibrare"
type: concept
domeniu: [energetică]
tags: [concept, energetică, piață]
status: draft
created: 2026-07-23
---

# Concept — Parte responsabilă de echilibrare

**RO:** parte responsabilă de echilibrare (PRE) · **EN:** balance responsible party (BRP)

> [!danger] Base act replaced — 19 August 2025
> References below to **Legea 107/2016** are to a **repealed** statute. It was abrogated in full by [[Legea 164-2025 — energia electrica (notă)|Legea nr. 164/2025]], which transposes the EU **fourth package** (Dir. 2019/944, Reg. 2019/943), **REMIT** and **CACM**. Article numbering is entirely different, and new regulated activities — **storage, aggregation, trading** — were added. Verify every L107 citation against L164/2025 before use.

## Definition
The market participant that assumes **financial responsibility for the imbalance** between the volumes it has scheduled (nominated) and the volumes actually injected into or withdrawn from the system within its balancing perimeter.

## Why the role exists — the physics forces it
Electricity cannot be meaningfully stored at system scale: generation must equal consumption **instant by instant**. Someone must correct every deviation in real time, and correcting it costs money. Two design questions follow:

1. **Who physically corrects it?** The system operator, by activating balancing reserves.
2. **Who pays?** If the answer were "everyone, socialised", no participant would have any reason to forecast accurately. So the cost is **assigned to whoever caused the deviation**.

The BRP is the legal device that makes (2) work. Every unit — every generator, every supplier's portfolio — must sit inside some BRP's perimeter. Nothing is unallocated.

## Mechanics
- **Registration** with the system operator and accession to a balancing agreement
- **Nomination** of a schedule for each settlement period
- **Metering** of actual flows
- **Imbalance settlement** — the difference is priced at an imbalance price derived from the cost of the balancing energy the operator actually had to activate
- **Collateral** — BRPs post security, because imbalance exposure is an unsecured credit risk to the whole market

Imbalance pricing is deliberately unattractive relative to contracting in advance. That is not a penalty regime; it is the incentive that makes the schedules meaningful.

## Why it matters more for renewables
Wind and solar output is forecast, not chosen. An intermittent generator carries structural imbalance exposure that a thermal plant does not, and in a small system with thin balancing reserves the imbalance price can be volatile. Two consequences follow, and both are commercial:

- BRPs **aggregate** portfolios so that individual errors net off — larger perimeter, smaller relative imbalance. This is why third-party BRP services exist as a business.
- The allocation of imbalance risk is a **negotiated term** in every renewable PPA. Who is the BRP, and who wears the imbalance cost, is often worth more than a point of tariff.

→ [[Concept — Producător eligibil]]

## Governing provisions
- [[HANRE 283-2020 — Regulile pietei energiei electrice (text)]] — electricity market rules: BRP registration, nomination, imbalance settlement *(annex missing — the operative rules are not in the vault)*
- [[HANRE 534-2019 — Regulile pietei gazelor naturale (text)]] — gas market rules, **complete text**; the gas balancing regime is the best worked example available in this vault
- [[Legea 107-2016 — energia electrica (text)|L107/2016]] — market organisation *(beyond truncation)*

## Related
[[Concept — Producător eligibil]] · [[Concept — Tarif reglementat]] · [[Energetică — sinteza sectorului]] · [[ANRE]]

## Notes / conclusions
> The BRP concept is where market design stops being law and starts being engineering economics. Cross-reference [[FP — Marginal Pricing in Electricity Markets]] (GeoMacro vault) before drafting or reviewing any PPA imbalance clause.
