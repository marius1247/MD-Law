---
title: MOC Piața de Energie Electrică
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
updated: '2026-07-28'
---

# ⚡ Map of Content: Piața de Energie Electrică

Note centrală de indexare pentru cadrul normativ, participanții și regulile care guvernează funcționarea pieței energiei electrice din Republica Moldova.

---

## 1. Cadrul Legislativ Primar
* [[Legea 107-2016 — energia electrica (text)|Legea nr. 107/2016 cu privire la energia electrică]] — Legea-cadru
* [[Legea 10-2016 — surse regenerabile (text)|Legea nr. 10/2016 privind promovarea utilizării energiei din surse regenerabile]]

## 2. Reglementări Secundare ANRE (Piață și Operare)
* [[HANRE 283-2020 — Regulile pietei energiei electrice (notă)|HANRE 283/2020]] — *Regulile pieței energiei electrice*
* [[HANRE 423-2019 — Codul retelelor electrice (notă)|HANRE 423/2019]] — *Codul rețelei electrice*
* [[HANRE 169-2019 — furnizarea energiei electrice (text)|HANRE 169/2019]] — *Regulamentul privind furnizarea energiei electrice*

## 3. Concepte Atomice Asociate
* [[Producător Eligibil]]
* [[Loc de Consum]]
* [[Furnizor de Ultimă Opțiune]]
* [[Parte Responsabilă de Echilibrare]]

## 4. Indice Automatizat de Acte (Dataview)
```dataview
TABLE issuer AS "Emitent", legal_status AS "Statut", last_amended AS "Ultima Modificare"
FROM #acte_normative AND "10 Acte normative"
WHERE domain = "energie_electrica"
SORT file.name ASC
```
