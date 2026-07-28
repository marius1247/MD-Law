---
title: "Energetică — sinteza sectorului"
type: domain-note
domeniu: [energetică]
tags: [domain, analysis, energetică]
status: draft
created: 2026-07-23
---

# Energy — sector synthesis

The reasoning layer for the energy corpus. Raw acts: [[MOC — Energetică]]. Text completeness caveats: [[Status ingestie — Energetica]].

> [!danger] Updated 2026-07-23 — the electricity law changed
> **[[Legea 164-2025 — energia electrica (notă)|Legea nr. 164/2025]] repealed [[Legea 107-2016 — energia electrica (text)|L107/2016]] in full**, in force 19 August 2025. Moldova moved from the EU **third package to the fourth**: Dir. (EU) 2019/944, Reg. (EU) 2019/943, **REMIT** and **CACM** are all now transposed. Storage, aggregation and trading became regulated activities; active consumers, citizen energy communities, demand response, flexible connection agreements and market coupling entered the law. Sections below have been updated; anything citing an L107 article number is historical.

---

## 1. The one thing to understand first

Moldovan energy law is **a delegation system, not a rulebook**. The organic laws ([[Legea 164-2025 — energia electrica (text)|L164/2025]] for electricity, [[Legea 108-2016 — gazele naturale (text)|L108/2016]] for gas) almost never answer an operational question. They set objectives, create [[ANRE]], and enumerate what ANRE *must* regulate. The binding answer — what tariff applies, who pays for a connection, what happens when a supplier fails — lives one or two tiers down, in a `HANRE`.

Practical consequence: **reading the law is step one of three.** Any real question needs (a) the enabling article in the law, (b) the ANRE act issued under it, (c) a check that the ANRE act is the current version. Advice built on the statute alone will be wrong more often than not.

## 2. The cascade

```
Parliament — organic law        framework, regulator, licensing, tariff principles
    ↓  (delegation article, cited as "temei legal")
Government — HG                 security of supply, strategy, construction, protection zones
    ↓
ANRE — HANRE                    market rules · network codes · connection & supply
                                regulations · tariff methodologies
    ↓
ANRE — individual decisions     licences, specific tariffs   (NOT ingested — see scope note)
```

Every tier-3 act in this vault names its parent article in `Temei legal`. That field is the navigation handle: it lets you walk *up* from an obligation to its statutory authority, which is what you need for any challenge to an ANRE act (*ultra vires* is the standard line of attack).

## 3. Four regulatory problems the sector is organised around

Everything in the corpus is an answer to one of these.

### 3.1 Natural monopoly → regulated tariffs
Transmission and distribution networks cannot be duplicated. The answer is **cost-plus-with-a-cap regulation**: ANRE publishes a *methodology* (the algorithm) with a multi-year application period, then applies it periodically to issue the actual tariff. Two acts, two different legal characters — the methodology is a normative act; the tariff is an individual administrative act. They are challenged in different ways and on different timelines.

Methodologies in the vault: [[HANRE 486-2017 — Metodologie tarife transport EE (text)|transmission]], [[HANRE 64-2018 — Metodologie tarife distributie EE (text)|distribution]], [[HANRE 375-2017 — Metodologie tarife regenerabile (text)|renewables]] (all *decision-only* — the annex holding the actual formula is not in the vault). → [[Concept — Tarif reglementat]]

### 3.2 Vertical integration → unbundling
A firm that both owns the wires and sells the electrons has every incentive to foreclose rivals. The EU third-package answer is structural: separate the network operator from supply and generation. L107/2016 and L108/2016 transpose this. → [[Concept — Unbundling]]

Moldova's gas sector is where this bites hardest — the historic Moldovagaz structure, Russian ownership, and the Vestmoldtransgaz/Moldovatransgaz split are the live application. Treat any pre-2023 commentary on gas unbundling as obsolete.

### 3.3 Entry into a network industry → licensing and connection
Two separate gates, often confused:
- **Licence** — permission to *carry on the activity* (generate, transmit, distribute, supply). Granted by ANRE. → [[Concept — Licență în energetică]]
- **Connection** — permission and physical works to *attach a specific installation* to a specific network. Granted by the network operator under ANRE's regulation. → [[Concept — Racordare la rețea]]

A developer needs both, in that logical order, and the connection process is where projects actually die — queue position, cost allocation, and the operator's capacity assessment.

> **2025 change worth knowing:** amendments to the electricity law introduced a **financial guarantee** for applicants and holders of connection permits for plants **above 200 kW**, with the amount set by ANRE. The point was to stop speculative queue-blocking by projects with no intention of building. If you hold a pre-2025 connection permit, check whether the guarantee applies retroactively to holders — the amendment was drafted to catch *holders*, not just new applicants. *(Verify against the current consolidation — this is beyond the truncation point in the vault text.)*

### 3.4 Universal service and the socially exposed consumer → public service obligations
A liberalised market will not, on its own, supply an unprofitable household. The mechanism is the **public service obligation** (`obligație de serviciu public`, [[Legea 107-2016 — energia electrica (text)#Articolul 11. Obligaţii de serviciu public|L107 art. 11]]), imposed on named participants and, where it imposes net cost, compensated. Its two operational children are the **supplier of last resort** ([[Concept — Furnizor de ultimă opțiune]]) and the regulated-tariff supply segment.

This is the pressure point in the current liberalisation programme: PSOs for large industrial gas consumers have been **progressively withdrawn**, a process run from October 2025 and targeted for completion by **1 April 2026**. The direction of travel is unambiguous — PSOs shrink toward households and small consumers only.

## 4. Market design

**Electricity.** The market rules ([[HANRE 283-2020 — Regulile pietei energiei electrice (text)|HANRE 283/2020]]) define the segments — bilateral contracts, balancing, and the machinery of imbalance settlement. The economic core is that every participant nominates a schedule and pays for deviating from it, which is what makes [[Concept — Parte responsabilă de echilibrare|the balance responsible party]] the pivotal role in the whole design. The annex containing the actual rules is missing from the vault (see the status note) — but the structure is standard Energy Community.

**A 2026 structural change:** suppliers and system operators are again required to procure electricity — **including for network losses** — through **market-based mechanisms**. During the crisis years this had been suspended in favour of directed/negotiated procurement. Its restoration is the single most consequential change to trading practice in the current period, and it interacts with [[MOC — Achiziții publice & Statul|procurement law]] via HANRE 24/2017 (procurement procedures for licence-holders — not yet ingested).

**Gas.** [[HANRE 534-2019 — Regulile pietei gazelor naturale (text)|HANRE 534/2019]] is the one tier-3 act in the vault with **complete text** — so it is the best available specimen for seeing how ANRE actually drafts market rules. Read it as the model even when the question is about electricity.

## 5. Renewables

[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] runs a two-track support scheme:
- **Fixed tariff** for smaller eligible producers, set by ANRE under [[HANRE 375-2017 — Metodologie tarife regenerabile (text)|methodology 375/2017]];
- **Auction / ceiling price** for larger capacity, allocated competitively against a quota set by Government.

The gatekeeping concept is **eligible producer** ([[Concept — Producător eligibil]]) — status confers the support, and the capacity quota is what makes it scarce. **Net metering / net billing** handles the prosumer case.

The binding constraint on Moldovan renewables is not the support level; it is **system integration** — a small, historically import-dependent system with limited flexibility and an interconnection profile reshaped by the post-2022 synchronisation with ENTSO-E via Romania. Legal work on renewables is in practice work on connection, curtailment and balancing exposure, not on tariff.

## 6. EU alignment — the engine of the whole corpus

Moldova is a **contracting party to the Energy Community**, by [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)|Legea nr. 117/2009]] ratifying the Athens Treaty of 2005. That treaty obliges it to implement the EU energy acquis, which is why every act here carries CELEX transposition notes.

The mechanism matters: EU instruments are **adapted and approved by Energy Community Ministerial Council decision**, and it is that adapted version Moldova transposes. Acts therefore cite decisions like `2021/13/MC-EnC` and `2022/03/MC-EnC` alongside the CELEX number. When testing whether transposition is correct, the reference text is the *adapted* version.

Post-2024 this is constitutionally reinforced: [[Constituția RM — text#Articolul 140¹. Aderarea la tratatele constitutive şi la actele de revizuire a tratatelor constitutive ale Uniunii Europene|art. 140¹]] gives binding EU acts priority over contrary domestic law on accession. Energy was the sectoral precursor — Moldova has been running an acquis obligation here since 2010.

Alignment landmarks in the corpus:

| Domestic act | EU instrument | Package |
|---|---|---|
| [[Legea 164-2025 — energia electrica (text)|L164/2025]] | **Dir. (EU) 2019/944** + **Reg. (EU) 2019/943** + **REMIT** (Reg. 1227/2011) + **CACM** (Reg. 2015/1222) | **Fourth** |
| [[Legea 108-2016 — gazele naturale (text)|L108/2016]] | Dir. 2009/73/EC — internal gas market | Third |
| [[Legea 139-2018 — eficienta energetica (text)|L139/2018]] | Energy efficiency directives | — |
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)|HG 820/2024]] | Reg. (EU) 2019/941 — risk preparedness | Fourth |
| ~~[[Legea 107-2016 — energia electrica (text)|L107/2016]]~~ *(repealed)* | Dir. 2009/72/EC | Third |

**Electricity is now a package ahead of gas.** L164/2025 includes the 2024 amending instruments (Dir. 2024/1711, Reg. 2024/1747), so it is a current transposition rather than a lagging one. Gas remains on the third package — expect a gas equivalent of L164/2025 to follow, and treat that as the next major legislative event in the domain.

**Enforcement is real.** The Energy Community Secretariat runs dispute settlement and publishes an **annual implementation report** scoring each contracting party. It is the best external assessment of where Moldovan energy law actually stands.

## 7. Where the risk sits — a practitioner's read

1. **Version risk is the dominant risk.** Two-thirds of what binds a market participant is ANRE-level and is amended continuously. The vault's `— text` files are dated snapshots. Always re-check [ANRE › Hotărâri](https://anre.md/acte-normative-3-18) before advising.
2. **The statute is the weaker authority in practice.** For an operational question, cite the HANRE and use the law only for the delegation chain.
3. **Truncation risk is specific and known.** The most-cited acts in the corpus are cut off before their substantive chapters. Do not infer absence from silence — see [[Status ingestie — Energetica]].
4. **The entire tier-3 layer is living on transitional provisions.** Every HANRE in this vault was issued under the now-repealed L107/2016. ANRE must re-adopt them under L164/2025's enabling articles. Until it does, each act's continued validity rests on transitional rules — check [ANRE › Hotărâri](https://anre.md/acte-normative-3-18) before relying on any of them.
5. **Three live transitions overlap right now** (mid-2026): the L164/2025 changeover, PSO withdrawal for industrial gas, and the return to market-based procurement including losses. All three change what a compliant contract looks like.

## 8. Open threads
- **Complete [[Legea 164-2025 — energia electrica (text)|L164/2025]] manually** — only art. 1 is in the vault; art. 2 alone has 150+ definitions. This is now the single highest-priority ingestion in the vault → [[Status ingestie — Energetica]]
- Complete **L108/2016** manually
- **Re-check every HANRE** against the new enabling articles; expect wholesale re-adoption
- Watch for a **gas equivalent of L164/2025** — gas is now a package behind electricity
- Not yet ingested: gas tariff methodologies (HANRE 535/2019, 443/2020), quality of service (422/2019, 537/2020), network development (94/2019), dispatch (316/2018), gas metering (297/2022)
- **HANRE 24/2017** — procurement by licence-holders → bridges to [[MOC — Achiziții publice & Statul]]
- Corporate-law overlap: unbundling is executed through **group restructuring** — see [[Societăți & guvernanță — sinteza]]

## Related
[[MOC — Energetică]] · [[ANRE]] · [[Concept — Tarif reglementat]] · [[Concept — Unbundling]] · [[Concept — Licență în energetică]] · [[Concept — Racordare la rețea]] · [[Concept — Furnizor de ultimă opțiune]] · [[Concept — Producător eligibil]] · [[Concept — Parte responsabilă de echilibrare]]
