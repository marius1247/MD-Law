---
title: "Energetică — synthesis"
type: domain-note
domeniu: [energetică]
tags: [domain, analysis, energetică]
status: draft
created: 2026-07-23
updated: 2026-08-07
---

# Energy — sector synthesis

The reasoning layer for the energy corpus. Raw acts: [[MOC — Energetică]]. Text completeness caveats: [[Status ingestie — Energetica]].

> [!tip] Analysis architecture (2026-08-07)
> Inter-law map + market-segmentation taxonomy: **[[Energetică — architecture map]]**. Build plan: [[Roadmap — Energy analysis architecture]]. First filled market hub: [[MOC — Piața de energie electrică]].

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

> **Connection guarantee:** plants **above 200 kW** need a financial guarantee (amount set by ANRE) — see [[HANRE 311-2026 — racordarea la retelele electrice (notă)]] and [[Concept — Racordare la rețea]]. Check transitional reach to pre-reform holders.

### 3.4 Universal service and the socially exposed consumer → public service obligations
A liberalised market will not, on its own, supply an unprofitable household. The mechanism is the **public service obligation** (`obligație de serviciu public`, [[Legea 164-2025 — energia electrica (text)#Articolul 17. Obligații de serviciu public|L164 art. 17]]; operational children arts. **114–115**), imposed on named participants and, where it imposes net cost, compensated. Its two operational children are the **supplier of last resort** ([[Concept — Furnizor de ultimă opțiune]]) and universal / regulated-tariff supply.

This is the pressure point in the current liberalisation programme: PSOs for large industrial gas consumers have been **progressively withdrawn**, a process run from October 2025 and targeted for completion by **1 April 2026**. The direction of travel is unambiguous — PSOs shrink toward households and small consumers only.

## 4. Market design

Segment-level navigation (actors, regulated activities, governing stack) lives in the architecture layer — do not expand this section into a catalogue. **Practitioner conflict rules** are named in [[Energetică — architecture map]] §1.3; per-vector risk matrices sit on each market MOC.

**Electricity.** → **[[MOC — Piața de energie electrică]]** · [[Energetică — segmente piață electricitate (notă)]]. Frame: [[Legea 164-2025 — energia electrica (notă)|L164/2025]]. Economic core: nominate → deviate → pay imbalance ([[Concept — Parte responsabilă de echilibrare|BRP]]). Live legal traps: **FUO ≥6 months** (art. 115) overrides HANRE 169’s 90-day text; **US** is households + micro/small only (art. 114); **REMIT** is a parallel gate to licensing; **flexible connection** (art. 2 pt. 2) is non-firm capacity — price curtailment; **FCEE** is mandatory buy/resell + supplier purchase (art. 87(2)) with RES→CfD sunset (art. 150(3)) and urban-CHP exit **calendar** duty (art. 150(4)); capacity mechanism is toolbox only (arts. 49–51). Prefer post-L164 HANRE where *temei* conflicts.

**A 2026 structural change:** suppliers and system operators are again required to procure electricity — **including for network losses** — through **market-based mechanisms**. During the crisis years this had been suspended in favour of directed/negotiated procurement. Its restoration is the single most consequential change to trading practice in the current period, and it interacts with [[MOC — Achiziții publice & Statul|procurement law]] via [[Legea 74-2020 — achizitii sectoriale (notă)|L74/2020]] (utilities/sectoral). Historic ANRE regulation [[HANRE 24-2017 — achizitii titulari de licenta (abrogata) (notă)|HANRE 24/2017]] was **abrogated** by [[HANRE 305-2021 — abrogare HANRE 24-2017 achizitii titulari (notă)|HANRE 305/2021]] (IF 06.08.2021) — do not cite it as live.

**Gas.** → **[[MOC — Piața gazelor naturale]]** · [[Energetică — segmente piață gaze (notă)]]. Hinge: entry-exit + [[Concept — Punct virtual de tranzacționare|PVT]] + daily imbalance (±10%). Frame: [[Legea 108-2016 — gazele naturale (notă)|L108]] — still **third package**. Live traps: **industrial PSO cliff → 1 Apr 2026** (re-paper ≥60 days out); **unbundling/TSO certification** currency before foreclosure opinions; uniform tariff **reconciliation** (arts. 2 & 99); art. **74** servitude compensation; REMIT arts. 94¹–94⁶. Do not import L164 fourth-package actors into gas opinions.

**Petroleum.** → **[[MOC — Piața produselor petroliere]]** · [[Energetică — segmente piață petrol (notă)]]. [[Legea 461-2001 — piata produselor petroliere (notă)|L461/2001]] is an **import–storage–wholesale–retail** chain with **daily ANRE max retail prices** ([[Concept — Preț maxim ANRE produse petroliere]]). Crisis decision tree: ordinary max → art. 4(2) stock-out ceiling → CNMC art. 6(7) derogation only if L248 crisis live. Licence 12(a) ≠ 12(b) LPG; depot minima are security gates. Do not conflate with HG 820 electricity crisis.

**Coal.** No dedicated ANRE coal market — [[Energetică — cărbune gap stub (notă)]].

**Heat / CHP.** → **[[MOC — Piața energiei termice]]** · [[Energetică — segmente piață termică (notă)]]. [[Legea 92-2014 — energia termica si cogenerarea (notă)|L92/2014]] art. 2(2): SACET activities are **public services of general interest** — regulated tariffs (art. 45), 25y licences (production/distribution/supply). **One plant, three regimes:** heat = L92; electricity = L164 (+ transitional FCEE); HE/GO = Cap. IV + [[Concept — Cogenerare de înaltă eficiență]] / HG 197. Cap. VI land/zones matter for network works. HANRE 23 body still incomplete — do not invent season rules from the contract annex. Geothermal: [[Energetică — geotermal gap stub (notă)]].

**Biofuels.** → **[[MOC — Biocarburanți și combustibili din biomasă]]** · [[Energetică — segmente piață biocarburanți (notă)]]. Not a wholesale market: L10 transport RES duty + importer blending/purchase on the L461 channel; [[HG 53-2025 — durabilitate biocarburanti emisii GES (notă)|HG 53]] sustainability/GHG (IF ≈11.02.2026). **Counting ≠ selling** — [[Concept — Criterii de durabilitate biocarburanți]]. ANRE annual mins + ceiling prices + sanctions (up to 5% purchase duty).

**Hydrogen.** No dedicated market statute — [[Energetică — hidrogen gap stub (notă)]]. Live hook: RFNBO ≥**70%** GHG reduction from **1 Jan 2026** (HG 53 pct. 2); GO/PNIEC watch.

**Cross-cutting (Step 7).** Prosumers / active consumers → [[Energetică — prosumatori și consumatori activi (notă)]] (boundary: [[Energetică — prosumer vs consumator activ (notă)]]). Incentives / support → [[Energetică — incentives și scheme de sprijin (notă)]]. ESG / climate governance → [[Energetică — ESG și guvernanță climatică (notă)]] (HG 10 · PNIEC · L139 — not a substitute for HANRE).

## 5. Renewables

[[Legea 10-2016 — surse regenerabile (text)|L10/2016]] runs a two-track support scheme:
- **Fixed tariff** for smaller eligible producers, set by ANRE under [[HANRE 375-2017 — Metodologie tarife regenerabile (text)|methodology 375/2017]];
- **Auction / ceiling price** for larger capacity, allocated competitively against a quota set by Government.

The gatekeeping concept is **eligible producer** ([[Concept — Producător eligibil]]) — status confers the support, and the capacity quota is what makes it scarce. **Net metering / net billing** handles the prosumer case.

The binding constraint on Moldovan renewables is not the support level; it is **system integration** — a small, historically import-dependent system with limited flexibility and an interconnection profile reshaped by the post-2022 synchronisation with ENTSO-E via Romania. Legal work on renewables is in practice work on connection, curtailment and balancing exposure, not on tariff.

## 6. EU alignment — the engine of the whole corpus

Moldova is a **contracting party to the Energy Community**, by [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)|Legea nr. 117/2009]] ratifying the Athens Treaty of 2005. That treaty obliges it to implement the EU energy acquis, which is why every act here carries CELEX transposition notes.

The mechanism matters: EU instruments are **adapted and approved by Energy Community Ministerial Council decision**, and it is that adapted version Moldova transposes. Acts therefore cite decisions like `2021/13/MC-EnC` and `2022/03/MC-EnC` alongside the CELEX number. When testing whether transposition is correct, the reference text is the *adapted* version.

Post-2024 this is constitutionally reinforced: [[Constituția RM (text)#Articolul 140¹. Aderarea la tratatele constitutive şi la actele de revizuire a tratatelor constitutive ale Uniunii Europene|art. 140¹]] gives binding EU acts priority over contrary domestic law on accession. Energy was the sectoral precursor — Moldova has been running an acquis obligation here since 2010.

Alignment landmarks in the corpus:

| Domestic act | EU instrument | Package |
|---|---|---|
| [[Legea 164-2025 — energia electrica (text)|L164/2025]] | **Dir. (EU) 2019/944** + **Reg. (EU) 2019/943** + **REMIT** (Reg. 1227/2011) + **CACM** (Reg. 2015/1222) | **Fourth** |
| [[Legea 108-2016 — gazele naturale (text)|L108/2016]] | Dir. 2009/73/EC — internal gas market | Third |
| [[Legea 139-2018 — eficienta energetica (text)|L139/2018]] | Dir. 2012/27/EU (EED) as amended by (EU) 2018/2002 · EnC 2021/14/MC-EnC | EE · [[Legea 139-2018 — eficienta energetica (notă)|notă]] |
| [[HG 820-2024 — situatii exceptionale electroenergetic (text)|HG 820/2024]] | Reg. (EU) 2019/941 — risk preparedness · EnC 2021/13/MC-EnC | Fourth · [[HG 820-2024 — situatii exceptionale electroenergetic (notă)|notă]] ⚠️ annex missing |
| ~~[[Legea 107-2016 — energia electrica (text)|L107/2016]]~~ *(repealed)* | Dir. 2009/72/EC | Third |

**Electricity is now a package ahead of gas.** L164/2025 includes the 2024 amending instruments (Dir. 2024/1711, Reg. 2024/1747), so it is a current transposition rather than a lagging one. Gas remains on the third package — expect a gas equivalent of L164/2025 to follow, and treat that as the next major legislative event in the domain.

**Enforcement is real.** The Energy Community Secretariat runs dispute settlement and publishes an **annual implementation report** scoring each contracting party. It is the best external assessment of where Moldovan energy law actually stands.

## 7. Where the risk sits — a practitioner's read

1. **Version risk is the dominant risk.** Two-thirds of what binds a market participant is ANRE-level and is amended continuously. The vault's `— text` files are dated snapshots. Always re-check [ANRE › Hotărâri](https://anre.md/acte-normative-3-18) before advising.
2. **The statute is the weaker authority in practice.** For an operational question, cite the HANRE and use the law only for the delegation chain.
3. **Truncation risk is specific and known.** The most-cited acts in the corpus are cut off before their substantive chapters. Do not infer absence from silence — see [[Status ingestie — Energetica]].
4. **The entire tier-3 layer is living on transitional provisions.** Every HANRE in this vault was issued under the now-repealed L107/2016. ANRE must re-adopt them under L164/2025's enabling articles. Until it does, each act's continued validity rests on transitional rules — check [ANRE › Hotărâri](https://anre.md/acte-normative-3-18) before relying on any of them.
5. **Three live transitions overlap right now** (mid-2026): the L164/2025 changeover, PSO withdrawal for industrial gas, and the return to market-based procurement including losses. All three change what a compliant contract looks like.
6. **Efficiency is now an operational compliance domain, not soft policy.** After LP111/2025, [[Legea 139-2018 — eficienta energetica (notă)|L139/2018]] designates DSOs and petroleum importers as obligated parties, puts large-enterprise audits on a CNED-notification clock with turnover sanctions, and runs EPC/FEE finance through [[CNED]]. Demand-response hooks in L139 still cite repealed L107 — route electricity flexibility through L164.
7. **Crisis tools are split across instruments.** Petroleum price derogations and procurement ±15% adjustment sit in [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (notă)|L101/2026]]; electricity risk-preparedness sits in [[HG 820-2024 — situatii exceptionale electroenergetic (notă)|HG 820/2024]] (annex still missing). Do not conflate them.

## 8. Open threads
- ✅ L164/L108 core texts are complete in vault (see [[Status ingestie — Energetica]]); keep currency checks live
- **Re-check every HANRE** against the new enabling articles; expect wholesale re-adoption
- Watch for a **gas equivalent of L164/2025** — gas is now a package behind electricity
- Ingest **HG 820 Annexes 1–2**; L101 parents [[Legea 461-2001 — piata produselor petroliere (notă)|L461]] + [[Legea 248-2025 — managementul situatiilor de criza (notă)|L248]] now ✅; L131/2015 still absent; balancing T&Cs [[HANRE 853-2025 — clauze echilibrare FSE si PRE (notă)|HANRE 853]] ✅ (**IF 1 Jul 2026**)
- Analysis backlog Batches 2–4: [[Analysis backlog — texts without notes]]
- Gas transmission methodology [[HANRE 535-2019 — Metodologie tarife transport gaze (notă)|HANRE 535/2019]] — decision ✅, **annex still missing**; amending [[HANRE 329-2025 — modificare Metodologie tarife transport gaze (notă)|329/2025]] ✅. Also not ingested: 443/2020, quality of service (422/2019, 537/2020 — 537 patched by [[HANRE 833-2023 — modificarea unor hotarari ANRE regenerabile (notă)|833/2023]]), network development (94/2019), dispatch (316/2018), gas metering (297/2022)
- Electricity network code: parent annex still incomplete; [[HANRE 656-2021 — modificare Codul retelelor electrice (notă)|656/2021]] now supplies Parts I–V substance
- Licence-holder procurement → [[Legea 74-2020 — achizitii sectoriale (notă)|L74/2020]] / [[MOC — Achiziții publice & Statul]] (HANRE 24 abrogated)
- Corporate-law overlap: unbundling is executed through **group restructuring** — see [[Societăți & guvernanță — synthesis]]

## Related
[[Energetică — architecture map]] · [[MOC — Piața de energie electrică]] · [[MOC — Piața gazelor naturale]] · [[MOC — Piața produselor petroliere]] · [[MOC — Piața energiei termice]] · [[MOC — Biocarburanți și combustibili din biomasă]] · [[Energetică — prosumatori și consumatori activi (notă)]] · [[Energetică — incentives și scheme de sprijin (notă)]] · [[Energetică — ESG și guvernanță climatică (notă)]] · [[Energetică — segmente piață electricitate (notă)]] · [[Energetică — segmente piață gaze (notă)]] · [[Energetică — segmente piață petrol (notă)]] · [[Energetică — segmente piață termică (notă)]] · [[Energetică — segmente piață biocarburanți (notă)]] · [[Energetică — cărbune gap stub (notă)]] · [[Energetică — geotermal gap stub (notă)]] · [[Energetică — hidrogen gap stub (notă)]] · [[Roadmap — Energy analysis architecture]] · [[MOC — Energetică]] · [[ANRE]] · [[CNED]] · [[Concept — Tarif reglementat]] · [[Concept — Unbundling]] · [[Concept — Licență în energetică]] · [[Concept — Racordare la rețea]] · [[Concept — Furnizor de ultimă opțiune]] · [[Concept — Producător eligibil]] · [[Concept — Parte responsabilă de echilibrare]] · [[Concept — Punct virtual de tranzacționare]] · [[Concept — Preț maxim ANRE produse petroliere]] · [[Concept — Situație de criză în domeniul petrolier]] · [[Concept — Cogenerare de înaltă eficiență]] · [[Concept — Criterii de durabilitate biocarburanți]] · [[Concept — Furnizor central de energie electrică]] · [[Concept — Facturare netă]] · [[Concept — OPEED]] · [[Concept — Consumator activ]] · [[Concept — Agregator independent]] · [[Concept — Stocare a energiei]] · [[Concept — Comunitate de energie a cetățenilor]] · [[Concept — Audit energetic]] · [[Concept — Contract de performanță energetică]] · [[Concept — Parte obligată (eficiență energetică)]]
