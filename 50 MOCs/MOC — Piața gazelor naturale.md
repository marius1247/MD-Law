---
title: "MOC — Piața gazelor naturale"
type: moc
domeniu: [energetică, gaze-naturale, piață]
tags: [moc, index, energetică, gaze, piață]
status: draft
created: 2026-08-07
updated: 2026-08-07
---

# MOC — Piața gazelor naturale

Regulation-oriented map of Moldova’s **natural gas markets**: segments, actors, regulated activities, and the acts that bind them.

Architecture spine: [[Energetică — architecture map]] · **Segment briefs:** [[Energetică — segmente piață gaze (notă)]] · Master inventory: [[MOC — Energetică]] · Narrative: [[Energetică — synthesis]] · Sector dossier: [[Energetică — sector gaze ANRE (notă)]]

> [!warning] Package lag
> Gas remains on the **EU third package** ([[Legea 108-2016 — gazele naturale (notă)|L108/2016]] / Dir. 2009/73/EC). Electricity is already on the **fourth** ([[Legea 164-2025 — energia electrica (notă)|L164/2025]]). Expect a gas L164-equivalent rewrite — treat that as the next major legislative event in the vector.

> [!danger] Live transition — PSO withdrawal
> Large industrial gas consumers lose public-service protection on a track running Oct 2025 → target **1 Apr 2026**. Regulated fallback assumptions in industrial supply contracts may disappear. → [[Concept — Furnizor de ultimă opțiune]] · [[HANRE 177-2026 — modificarea unor hotarari ANRE (notă)|HANRE 177/2026]]

---

## 1. Governing stack (how the acts talk)

| Tier | Act | Role for the market |
|---|---|---|
| Treaty | [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)\|L117/2009]] | EnC acquis (Dir. 2009/73, Reg. 715/2009, SoS Reg. 2017/1938, REMIT — adapted) |
| Framework | [[Legea 174-2017 — energetica (notă)\|L174/2017]] | ANRE independence; who may regulate |
| Sectoral market | **[[Legea 108-2016 — gazele naturale (notă)\|L108/2016]]** | Licensing, unbundling, TPA, PSO, REMIT (arts. 94¹–94⁶), consumer protection |
| Market rules | [[HANRE 534-2019 — Regulile pietei gazelor naturale (notă)\|HANRE 534/2019]] | Entry-exit, [[Concept — Punct virtual de tranzacționare\|PVT]], PRE, imbalance cash-out |
| Network code | [[HANRE 420-2019 — Codul retelelor de gaze naturale (notă)\|420]] + [[HANRE 328-2025 — modificare Codul retelelor de gaze naturale (notă)\|328/2025]] + [[HANRE 310-2026 — modificare Codul retelelor de gaze naturale (notă)\|310/2026]] | Nominations, capacity products, [[Concept — Capacitate condiționată\|conditional capacity]] |
| Connection | [[HANRE 112-2019 — racordarea la retelele de gaze (notă)\|HANRE 112/2019]] (+ [[HANRE 8-2023 — modificare racordare gaze si masurare gaze (notă)\|8/2023]]) | Physical access |
| Supply / switching | [[HANRE 113-2019 — furnizarea gazelor naturale (notă)\|HANRE 113]] · [[HANRE 363-2020 — schimbarea furnizorului de gaze (notă)\|363]] · [[HANRE 177-2026 — modificarea unor hotarari ANRE (notă)\|177/2026]] | Retail, FUO, fixed-price ≥12m, comparison tool |
| Metering | [[HANRE 297-2022 — masurare gaze naturale comerciale (notă)\|HANRE 297/2022]] | Commercial metering |
| Tariffs | [[HANRE 535-2019 — Metodologie tarife transport gaze (notă)\|535]] · [[HANRE 443-2020 — Metodologie tarife distributie gaze (notă)\|443]] · [[HANRE 355-2021 — preturi reglementate furnizare gaze (notă)\|355]] (+ [[HANRE 540-2024 — modificare Metodologie preturi furnizare gaze (notă)\|540]]) | Entry-exit T, D, regulated supply / FUO prices |
| SoS / storage obligation | [[HG 365-2024 — obligatie stocare gaze naturale (notă)\|HG 365]] · [[HG 364-2024 — modificare stocuri securitate gaze (notă)\|364]] · [[HG 677-2024 — plan sezon incalzire 2024-2025 (notă)\|677]] · L108 arts. 108²–108³ | Security stocks ≠ market storage product |
| Crisis bridge | [[Legea 248-2025 — managementul situatiilor de criza (notă)\|L248]] · [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (notă)\|L101]] | Do not conflate with electricity HG 820 |
| Procurement / special law | [[Legea 234-2022 — Energocom securitate furnizare gaze (notă)\|L234/2022]] · [[Legea 74-2020 — achizitii sectoriale (notă)\|L74/2020]] | Energocom security project; utilities procurement |

Horizontal logic: **L108 creates the market; HANRE 534 runs wholesale at the PVT; 420 runs the pipes; 112/113 are the consumer/developer gates; HG storage instruments are SoS overlays, not ordinary trading.** Bridges: [[Energetică — architecture map]] §1.2.

---

## 2. Market segments (regulatory view)

| Segment | MD name | Who operates / clears | Governing ops rules | Status |
|---|---|---|---|---|
| Wholesale bilaterals | Contracte angro (delivery at PVT) | Parties + TSO/balancing entity notifications | HANRE 534 | Brief ✅ |
| Virtual trading point | **[[Concept — Punct virtual de tranzacționare\|PVT]]** | TSO / balancing entity (EE) | HANRE 534 · 420 | Brief ✅ · Concept ✅ |
| Entry-exit capacity | Capacitate intrare/ieșire (firm / interruptible / secondary) | TSO (Vestmoldtransgaz) | HANRE 534 · 420 · 535 tariffs | Brief ✅ |
| Conditional / corridor capacity | **[[Concept — Capacitate condiționată\|Capacitate condiționată]]** | TSO | 328/310 · 535 §7² | Concept ✅ · Brief ✅ |
| Balancing | Echilibrare zilnică (gas day) | Balancing entity + PRE | HANRE 534 (asymmetric ±10% cash-out) · 420 | Brief ✅ |
| Storage (commercial + SoS) | Stocare / obligație de stocare | Storage operator · Energocom obligation | L108 arts. 51, 56 · HG 365/364/677 | Brief ✅ |
| Retail / switching | Furnizare · schimbare furnizor | Suppliers · DSO meter transfer | HANRE 113 · 363 · 177 | Brief ✅ |
| Regulated / PSO supply · FUO | OSP · **FUO** | Designated suppliers | L108 arts. 89–90 · HANRE 113 · 355/540 | Brief ✅ · [[Concept — Furnizor de ultimă opțiune]] |

Gas has **no** PZU/PI/OPEED stack like electricity — organised short-term trading is thinner; the hinge is **PVT + daily imbalance**.

---

## 3. Actors

| Actor | Role | Primary source |
|---|---|---|
| **OST** (Vestmoldtransgaz) | Transmission, capacity, PVT interface, often balancing functions | L108 · HANRE 420/534 · [[Concept — Unbundling]] |
| **OSD** | Distribution; network development; meter reads for switching | L108 · HANRE 112/113 · 138 · 443 |
| **Storage operator** | Commercial storage access | L108 arts. 51, 56 |
| **Producers** | Domestic production (limited in practice) | L108 arts. 19–21 |
| **Suppliers** | Wholesale + retail; often PRE | L108 · HANRE 113 |
| **Traders** | Wholesale trading licence (art. 10(1)(d¹)) | L108 |
| **PRE** | Financial responsibility for daily imbalance | HANRE 534 |
| **EE (entitate de echilibrare)** | Registers PRE, confirms PVT notifications, cash-out | HANRE 534 |
| **FUO / PSO suppliers** | Last-resort / regulated categories | L108 arts. 89–90 · [[Concept — Furnizor de ultimă opțiune]] |
| **Energocom** | Storage-obligation holder; security-of-supply roles | HG 365 · L234 |
| **ANRE** | Licensing, tariffs, market rules, REMIT, certification | [[ANRE]] · L174 · L108 |
| Final customers | Switching rights; industrial PSO exit | HANRE 113/177 |

---

## 4. Regulated activities (licensing — L108 arts. 10–12)

| Activity (art. 10) | Licence (art. 12) | Notes |
|---|---|---|
| Production | Production | Limited domestic relevance |
| Transmission | Transmission | Exclusive territory; unbundling / certification gate |
| Distribution | Distribution | Exclusive territory |
| Storage | Storage | Commercial storage; distinct from HG SoS obligation |
| **Trading** | Trading | Wholesale only |
| Supply | Supply | Wholesale + retail; PSO/FUO designations |
| CNG vehicle sales | CNG station sales | Specific licence type |
| Ownership of transmission networks (ISO case) | Ownership right | When independent system operator designated |

Doctrine: [[Concept — Licență în energetică]] (gas parallel under L108). Separate gate: **connection** ([[Concept — Racordare la rețea]] · HANRE 112). REMIT registration for wholesale: [[Energetică — licențiere cross-border și REMIT (notă)]].

---

## 5. Monopoly layer

- Connection & access — HANRE 112 · [[MOC — Racordare și acces la rețele]]
- Network code — HANRE 420 / 328 / 310
- QoS — [[HANRE 422-2019 — calitate servicii transport distributie gaze (notă)|HANRE 422]]
- Network development — [[HANRE 138-2018 — dezvoltarea retelelor de distributie gaze (notă)|HANRE 138]]
- Tariffs — [[MOC — Tarife și metodologii ANRE]] · [[Concept — Tarif de transport]] · [[Concept — Tarif de distribuție]] · [[Concept — Consum tehnologic gaze]] · [[Concept — Unbundling]]
- **Land / gas servitude (art. 74)** — pipeline works on agricultural land; compensation procedure thin → pre-agree appraisals (see §8)

---

## 6. Support, SoS, crisis (bridges out of pure wholesale)

| Theme | Acts | Note |
|---|---|---|
| Industrial PSO withdrawal | L108 · HANRE 177 path · regulated prices 355/540 | Live cliff → **1 Apr 2026** — see §8 |
| FUO / regulated retail prices | HANRE 113 · 355/540 | Narrowing toward households/small |
| Storage obligation / security stocks | HG 365 · 364 · 677 | **≠** commercial storage product |
| Energocom special statute | L234 / LP20 | Fiscal/customs + guarantee release |
| Vulnerability fund | [[Legea 241-2022 — Fond reducere vulnerabilitate energetica (notă)\|L241]] | Social overlay |
| Crisis governance | L248 · L101 · CNMC HGs | Distinct from electricity HG 820 |
| REMIT (wholesale integrity) | L108 arts. **94¹–94⁶** | Parallel gate — [[Energetică — licențiere cross-border și REMIT (notă)]] |

---

## 7. Concepts (gas market)

**Live:** [[Concept — Punct virtual de tranzacționare]] · [[Concept — Capacitate condiționată]] · [[Concept — Consum tehnologic gaze]] · [[Concept — Unbundling]] · [[Concept — Furnizor de ultimă opțiune]] · [[Concept — Licență în energetică]] · [[Concept — Racordare la rețea]] · [[Concept — Tarif de transport]] · [[Concept — Tarif de distribuție]] · [[Concept — Tarif reglementat]]

**Electricity analogues (do not conflate):** [[Concept — Parte responsabilă de echilibrare]] · [[Concept — Stocare a energiei]] *(electricity BESS — not gas storage)*

---

## 8. Professional legal analysis (risk matrix)

Lifted from [[Legea 108-2016 — gazele naturale (notă)|L108 act-note]] and segment practice. Cross-vector rules: [[Energetică — architecture map]] §1.3.

| Issue | Flaw / ambiguity | Practical risk | Advice rule |
|---|---|---|---|
| **Package lag** | Gas still **third** package; electricity already **fourth** | Importing L164 actors (OPEED, aggregators, active consumers) into gas opinions | Cite L108/HANRE 534; forecast gas rewrite — do not invent fourth-package gas |
| **Unbundling / TSO certification** | Incumbent history (Moldovagaz/Gazprom) vs Vestmoldtransgaz carve-out; certification is the concrete enforcement act | Foreclosure / TPA opinions that ignore current perimeter | Verify **current** TSO certification and corporate perimeter before any foreclosure opinion; watch EnC Secretariat reports |
| **Industrial PSO cliff** | Withdrawal track Oct 2025 → target **1 Apr 2026** | Industrial contracts assuming regulated fallback | Re-paper **≥ 60 days** before cliff; confirm which HANRE 177 / 355–540 instruments actually withdrew protection; FUO ≠ permanent industrial PSO |
| **Uniform DSO tariff reconciliation (arts. 2 & 99)** | Settlement delays / default by reconciliation entity | Regional DSO cash-flow deficits waiting for equalisation | Pre-litigation petition to ANRE demanding reconciliation audit; map cash-flow in tariff disputes |
| **Art. 74 gas servitude** | Thin procedural rules for agricultural compensation | Landowner suits halt pipeline works | Pre-agreed voluntary compensation on certified agricultural appraisals |
| **REMIT gas** | Arts. 94¹–94⁶ parallel to electricity | Trading without registration / inside-info SOP | Same four-gate discipline as electricity |
| **SoS vs commercial storage** | HG 365/364/677 overlays ≠ storage licence product | Conflating obligation costs with market storage tariffs | Three questions: commercial access? 15% obligation? security stocks? |
| **Transnistria overhang** | Consumption/debt not resolved by L108 | Political/SoS risk outside statute | Flag as commercial/political overhang — not a licensing defence |
| **HANRE 535 annex** | Decision present; **methodology annex missing** in vault | Inventing entry-exit formula detail | Quote only what is ingested; pull official annex for tariff math |

**Commercial hinge remains:** entry-exit capacity + [[Concept — Punct virtual de tranzacționare|PVT]] + daily imbalance (±10% cash-out) — not a PZU clone.

---

## 9. Open threads

1. ✅ Hub + segment briefs (Step 3)
2. ✅ Professional risk matrix (§8) — unbundling, PSO cliff, reconciliation, servitude, REMIT
3. Watch **gas equivalent of L164/2025** (fourth-package catch-up)
4. Confirm industrial PSO withdrawal instruments after 1 Apr 2026
5. Deepen gas PRE concept if mechanics diverge enough from electricity PRE note
6. Cross-border capacity platforms (PRISMA etc.) — operational, not fully mapped in vault
7. Ingest HANRE 535 methodology annex before tariff-formula advice

## Related
[[Energetică — segmente piață gaze (notă)]] · [[Energetică — architecture map]] · [[Roadmap — Energy analysis architecture]] · [[MOC — Energetică]] · [[MOC — Piața de energie electrică]] · [[Energetică — sector gaze ANRE (notă)]] · [[Energetică — licențiere cross-border și REMIT (notă)]] · [[ANRE]]
