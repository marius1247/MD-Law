---
title: MOC — Piața de energie electrică
type: moc
domain: energie_electrica
domeniu:
- energie electrică
- piață
- energetică
status: draft
tags:
- moc
- piata_energiei
- anre
created: '2026-07-28'
updated: '2026-08-07'
---

# Map of Content: Piața de Energie Electrică

Note centrală de indexare pentru cadrul normativ, participanții și regulile care guvernează funcționarea pieței energiei electrice din Republica Moldova.

---

## 1. Cadrul Legislativ Primar
* [[Legea 164-2025 — energia electrica (notă)|Legea nr. 164/2025]] — **law in force**
* ~~[[Legea 107-2016 — energia electrica (text)|Legea nr. 107/2016]]~~ — abrogated 19.08.2025
* [[Legea 10-2016 — surse regenerabile (text)|Legea nr. 10/2016]] — renewables support · imbalance deadbands via [[Legea 45-2025 — garantiile avizelor de racordare si tolerante dezechilibre (notă)|LP45/2025]]
* [[HG 156-2025 — modificare HG 1059-2023 PSO securitate EE (notă)|HG 156/2025]] — security-of-supply PSO calendar (parent HG 1059 not in vault)

## 2. Reglementări Secundare ANRE (Piață și Operare)
* [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)|HANRE 283/2020]] — *Regulile pieței energiei electrice*
* [[HANRE 853-2025 — clauze echilibrare FSE si PRE (notă)|HANRE 853/2025]] — FSE/PRE balancing T&Cs (**IF 1 Jul 2026**)
* [[HANRE 423-2019 — Codul retelelor electrice (notă)|HANRE 423/2019]] — *Codul rețelei electrice*
* [[HANRE 169-2019 — furnizarea energiei electrice (text)|HANRE 169/2019]] — *Regulamentul privind furnizarea energiei electrice*

## 3. Concepte Atomice Asociate
* [[Concept — Producător eligibil]]
* [[Concept — Loc de consum]]
* [[Concept — Furnizor de ultimă opțiune]]
* [[Concept — Parte responsabilă de echilibrare]]
* [[Concept — Furnizor de servicii de echilibrare]]

## 4. Indice Automatizat de Acte (Dataview)
```dataview
TABLE issuer AS "Emitent", legal_status AS "Statut", last_amended AS "Ultima Modificare"
FROM #acte_normative AND "10 Legislation"
WHERE domain = "energie_electrica"
SORT file.name ASC
```
