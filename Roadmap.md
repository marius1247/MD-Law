---
title: "Roadmap"
type: project
tags: [project, roadmap]
created: 2026-07-22
updated: 2026-07-23
---

# Roadmap

## Done — Foundations
- Vault scaffold, `.obsidian` config, [[Convenții vault|conventions]], templates
- [[Sistemul de drept al RM (overview)]] · [[Ierarhia actelor normative]] · [[Monitorul Oficial]] · [[Procesul legislativ]] · [[Glosar juridic]]
- [[Constituția RM — text|Constituția]] (complete, current to Nov 2024) + [[Legea 100-2017 — actele normative (text)|Legea 100/2017]], with analysis companions
- MOC hubs + [[00 - Harta instituțională|institutional map]]

## Done — Energy corpus (19 acts)
Three tiers ingested and wired into [[MOC — Energetică]]: 6 primary laws, 1 Government act, 12 ANRE acts. [[ANRE]] profile written with the law→regulator chain.

## Done — Analysis layer (2026-07-23)
The vault now has a reasoning layer on top of the texts. `20 Domenii` holds one synthesis per domain; `30 Concepte` holds 21 atomic notes; four new authority profiles.

- **Energy** — [[Energetică — sinteza sectorului]] + act companions for [[Legea 174-2017 — energetica (notă)|L174/2017]], [[Legea 108-2016 — gazele naturale (notă)|L108/2016]], [[Legea 10-2016 — surse regenerabile (notă)|L10/2016]] + 7 concepts
- **Companies & governance** — [[Societăți & guvernanță — sinteza]] + 6 concepts + [[ASP]], [[CNPF]]
- **Tax & accounting** — [[Fiscalitate — sinteza sistemului fiscal]] + [[Contabilitate & raportare financiară — sinteza]] + 5 concepts + [[SFS]]
- **Commercial** — [[Drept comercial — sinteza]] + 3 concepts + [[Consiliul Concurenței]]

## Diagnosed — the ingestion ceiling
The `— text` truncation is **not a bug that can be fixed by re-running the download**. Automated fetch from legis.md stops at **~96,000 characters**, mid-sentence, silently; legis.md has no per-chapter endpoint and its viewer is client-rendered. Confirmed by re-fetching L107/2016 and getting the identical cut. **Large acts require a manual browser download.** Full write-up: [[Status ingestie — Energetica]] · [[Convenții vault]].

## Done — the L107/2016 correction (2026-07-23, second pass)

Chasing the "Legea 164/2025 = REMIT amendment" roadmap item turned up something bigger: **L164/2025 is a complete replacement electricity law that repealed [[Legea 107-2016 — energia electrica (text)|L107/2016]] in full** on 19 August 2025. The vault's flagship energy act had been abrogated for eleven months.

Moldova moved from the EU **third package to the fourth**: Dir. (EU) 2019/944 (as amended by 2024/1711), Reg. (EU) 2019/943 (as amended by 2024/1747), **REMIT** and **CACM**, all in their Energy Community-adapted versions. New regulated activities — **storage, aggregation, trading**. New actors — active consumers, citizen energy communities, independent aggregators, OPEED. Universal service and supplier-of-last-resort now cleanly separated on the face of the statute. Flexible connection agreements introduced.

Actioned across the vault:
- [[Legea 164-2025 — energia electrica (text)]] (partial) + [[Legea 164-2025 — energia electrica (notă)|full analysis]]
- [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (text)]] ✅ **complete text** + [[Legea 117-2009 — aderarea la Tratatul Comunitatii Energetice (notă)|notă]] — the domain's anchor
- L107/2016 text and notă marked **abrogated / superseded**, retained for legacy positions
- Repeal banners on 7 energy concepts, [[ANRE]], and the 4 HANRE acts issued under the repealed law
- [[Energetică — sinteza sectorului]] §6 rewritten; [[MOC — Energetică]] and [[Status ingestie — Energetica]] restructured

> [!important] The lesson, generalised
> A vault of legal texts silently rots. **Currency is a bigger risk than completeness** — a truncated act announces itself, a repealed one does not. Every domain hub needs a periodic repeal check, not just an ingestion pass.

---

## Done — full energy texts ingested (2026-07-23, third pass)

Marius supplied consolidated PDFs from legis.md; the ~96 KB fetch ceiling is bypassed by manual download exactly as predicted. Now **complete** in the vault:

- [[Legea 164-2025 — energia electrica (text)]] — **151 articles**, consolidated incl. LP101/2026 (was: art. 1 only)
- [[Legea 108-2016 — gazele naturale (text)]] — 114 articles + bis, consolidated to LP227/2025 (was: art. 18)
- [[Legea 10-2016 — surse regenerabile (text)]] — 45 articles + bis (was: art. 34)
- [[Legea 139-2018 — eficienta energetica (text)]] — 30 articles + bis (was: art. 24)
- [[Legea 101-2026 — consolidarea mecanismelor de interventie in situatii de criza (text)]] — **new amending law**; touches L164/2025, petroleum, procurement, contraventional code

Superscript "bis" articles (art. 36¹ etc.) that pdftotext flattens were reconstructed on ingest. L164 and L108 `— notă` companions updated to drop the truncation warnings. Details: [[Status ingestie — Energetica]].

> [!success] Resolved 2026-07-26 — manual source dump ingested
> Marius supplied full legis.md downloads into `source/`. L174/2017, L92/2014, L100/2017, HANRE 283 annex, HANRE 420 annex, HANRE 112/113/168 are now **complete**. New L164-era acts ingested: HANRE 311/2026 (connection), 626/2023 + 261/2026 (transport tariffs), 383/2026 (market rules amend), 328/2025 + 310/2026 (gas network code amends). Keystone statutes for companies, tax, commercial, civil, procedure and sectoral procurement are now in the vault with analysis companions.

---

## Next — highest value first

### 1. Re-verify the remaining pre-L164 HANRE layer
[[HANRE 283-2020 — Regulile pietei energiei electrice (text)|HANRE 283/2020]] still rests on L107 enabling articles (even though amended 2026). [[HANRE 423-2019 — Codul retelelor electrice (text)|HANRE 423/2019]] annex is **still missing**. Check [ANRE › Hotărâri](https://anre.md/acte-normative-3-18) for re-adoptions under L164.

### 2. Remaining energy tier-3 downloads
Gas tariff methodologies (HANRE 535/2019, 443/2020), quality of service (422/2019, 537/2020), network development (94/2019), dispatch (316/2018), gas metering (297/2022), **HANRE 24/2017** (licence-holder procurement), electricity network code annex (423/2019), distribution & renewables tariff methodology annexes (64/2018, 375/2017).

### 3. General public procurement
**Legea nr. 131/2015** — the core procurement statute (L74/2020 sectoral is already in). Plus AAP/ANSC authority profiles.

### 4. Deepen analysis layer
- Domain syntheses for Achiziții / Proceduri / Drept civil (currently thin)
- Atomic concepts for those domains
- Double-tax-treaty table; IT Park regime detail; SNC map
- State aid law (exact number — verify on legis.md)

### 5. Watch list (unchanged — still live)
See table below. Especially: gas equivalent of L164/2025; entrepreneurship law replacing L845/1992; Fiscal/Customs Code rewrite concept.

## Done — 2026-07-26 corpus expansion
- **Companies:** [[Legea 135-2007 — SRL (text)|L135/2007]], [[Legea 1134-1997 — societati pe actiuni (text)|L1134/1997]], [[Legea 220-2007 — inregistrarea de stat (text)|L220/2007]], [[Legea 149-2012 — insolvabilitate (text)|L149/2012]]
- **Tax:** [[Codul fiscal 1163-1997 (text) — Index|Codul fiscal]] (Titluri I–X), [[Legea 287-2017 — contabilitate (text)|L287/2017]], [[Legea 86-2026 — modificare Legea contabilitatii (text)|L86/2026]], [[Codul vamal 95-2021 (text)|Codul vamal]]
- **Commercial:** [[Legea 183-2012 — concurenta (text)|L183/2012]], [[Legea 235-2006 — principii reglementare intreprinzator (text)|L235/2006]], [[Legea 160-2011 — reglementarea prin autorizare (text)|L160/2011]]
- **Civil / procedure:** [[Codul civil 1107-2002 (text) — Index|Codul civil]] (I–V), [[Codul administrativ 116-2018 (text)|Cod administrativ]], [[Codul de procedura civila 225-2003 (text)|CPC]], [[Codul de executare 443-2004 (text)|Cod de executare]], [[Legea 23-2008 — arbitraj (text)|L23/2008]]
- **Procurement:** [[Legea 74-2020 — achizitii sectoriale (text)|L74/2020]]

## Blocked / deferred
- ~~Bulk act ingestion~~ — largely unblocked by manual `source/` dumps
- Currency-check remaining pre-L164 electricity HANRE acts before citing operationally
- `.obsidian` config / Dataview — still not in the repo (open `Moldovan Law/` as the vault root)

## Watch list — live legislative movement
| File | Why it matters |
|---|---|
| **New entrepreneurship law** (project 345/MDED/2025) | Repeals **L845/1992** entirely, 2-year transition → [[Drept comercial — sinteza]] |
| **Legea nr. 86/2026** → in force **1 Jan 2027** | Raises accounting size thresholds sharply; many entities drop a category → [[Contabilitate & raportare financiară — sinteza]] |
| **Fiscal Code / Customs Code rewrite** (MF concept) | Would restructure the Titlu map |
| **Gas PSO withdrawal** — target **1 Apr 2026** | Large industrial consumers move to market supply → [[Concept — Furnizor de ultimă opțiune]] |
| **Market-based procurement incl. losses**, from 2026 | Changes what a compliant supply contract looks like |
| **SA remuneration policy** amendments to L1134/1997 | EU governance alignment → [[Societăți & guvernanță — sinteza]] |
| **Gas equivalent of L164/2025** | Gas is a package behind electricity |
| **Re-adoption of remaining ANRE tier-3 under L164** | Connection already done (HANRE 311/2026); market rules / network code still transitional |

## Housekeeping
- Verify current consolidations — legis.md snapshots go stale
- Swap in the post-2024 Constitution `doc_id` when legis publishes it
- Enable **Dataview** — frontmatter is structured for auto-tables
- Keep `source/` as the raw-dump inbox; do not edit ingested `— text` files except to update consolidations
- Cross-vault link [[FP — Marginal Pricing in Electricity Markets]] points into GeoMacro and will not resolve here — expected
