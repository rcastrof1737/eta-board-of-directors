---
name: geography-playbook
description: Jurisdiction checklist for ETA board sessions covering the United States, Canada, Europe, Mexico and Brazil. Lists what to verify per country, with sourced facts and verification dates. Loaded by cross-border-director and by any director advising on financing, labour or tax.
---

# Geography Playbook — US, Canada, Europe, Mexico, Brazil

**Rule of use:** every fact below carries its source and the date it was checked. Rules change. Before any real decision, re-verify with the official source and a local advisor. Anything not listed with a source is a **checklist item to verify**, not a fact.

Last reviewed: **2026-11-26**.

## 1. United States

### Verified facts (as of 2026-11-26)

| Topic | Fact | Source |
|---|---|---|
| SBA 7(a) rulebook | SOP 50 10 8.1 applies to applications receiving an SBA loan number on or after **1 Oct 2026**; earlier applications stay under SOP 50 10 8. | SBA Information Notice 5000-880695 (issued 14 Aug 2026) |
| Ownership / citizenship | Policy updates in 2026 require 100% of direct and indirect owners to be U.S. Citizens or U.S. Nationals whose principal residence is in the U.S. (lawful permanent residents were eligible under the earlier SOP 50 10 8 text). | SBA Procedural Notice 5000-876626; law-firm summaries of SOP 50 10 8.1 |
| Equity injection | Complete changes of ownership require at least 10% equity injection; seller debt counts only if subordinated and on full standby for the life of the 7(a) loan, and only for part of the injection. | SOP 50 10 8 / 8.1 (Appendix 15 in 8.1); lender and law-firm summaries |
| Debt-service coverage | Reported increase from 1.15x to 1.25x for most change-of-ownership loans under 8.1. | Law-firm summary of SOP 50 10 8.1 — **verify in SOP text** |
| Quality of earnings | Lender-obtained QoE required for initial-acquisition / business-expansion change-of-ownership loans with purchase price ≥ USD 3M (excluding real estate) under 8.1. | Accounting-firm summaries of SOP 50 10 8.1 — **verify in SOP text** |

**Board implication:** a traditional search fund with institutional, foreign or non-citizen investors (or a non-citizen searcher) is usually **not SBA-eligible**. SBA is a realistic route mainly for self-funded searchers who are U.S. citizens/nationals. Never assume SBA in a model; set it as an eligibility-gated option.

### Checklist to verify
- Conventional senior lender covenants (leverage, fixed-charge coverage), amortisation, cash sweep.
- State-level tax nexus, sales tax, payroll and non-compete enforceability (varies by state and has been subject to federal rule-making and litigation).
- Seller-note subordination and standby terms in the intercreditor agreement.

## 2. Canada

### Verified facts (as of 2026-11-26)

| Topic | Fact | Source |
|---|---|---|
| Canada Small Business Financing Program (CSBFP) | Maximum per borrower CAD 1.15M (up to CAD 1M term loans + CAD 150k line of credit). | ISED CSBFP pages and FAQ |
| CSBFP and acquisitions | The purchase of eligible **assets** of an existing business may qualify; **share purchases** are not eligible. | ISED CSBFP FAQ for small businesses |

**Board implication:** CSBFP is small relative to most search-fund deals and only fits asset purchases; most deals rely on Schedule I banks, BDC (verify current products), seller financing and subordinated debt.

### Checklist to verify
- Provincial employment standards (termination notice and common-law reasonable-notice exposure can be material).
- Quebec language and labour specifics (Charter of the French Language) where relevant.
- Lifetime capital gains exemption and seller tax planning (affects seller rollover and price structure).

## 3. Europe (country-by-country; never use one "EU" assumption)

### Checklist to verify per country
- Senior bank debt market depth for SMB acquisitions; typical structures (bank + vendor loan + equity) and covenant packages.
- Vendor loans (seller financing) and earn-outs: enforceability and tax treatment.
- Works councils / employee information and consultation duties before restructurings or transfers (e.g., Germany, France, Netherlands, Spain, Italy).
- Transfer-of-undertakings rules (TUPE-type regimes) for asset deals and carve-outs.
- Financial-assistance restrictions on the target guaranteeing acquisition debt.
- GDPR for any customer, employee or AI/data project.
- Management equity / sweet-equity taxation (varies strongly by country).

## 4. Mexico

### Verified facts (as of 2026-11-26)

| Topic | Fact | Source |
|---|---|---|
| Employee profit sharing (PTU) | Employers distribute 10% of adjusted taxable profit to eligible employees; directors / general managers are excluded. Since the 2021 labour reform, each employee's PTU is capped at the greater of three months' salary or the average PTU received in the last three years. The Supreme Court upheld the cap (Amparo en revisión 633/2023). | Federal Labour Law reform (2021); EY, Mercer, Ogletree summaries |
| Outsourcing | The 2021 reform heavily restricted personnel subcontracting; only registered specialised services are allowed. | 2021 labour reform; law-firm summaries |

**Board implication:** model PTU as an operating cost that rises with profitability; diligence and monitor outsourcing, IMSS / INFONAVIT and tax contingencies continuously; price MXN and local-rate exposure explicitly.

### Checklist to verify
- Current working-hours reform status and implementation timeline.
- IMSS, INFONAVIT and payroll-tax obligations by state.
- Availability and cost of MXN bank debt for acquisitions vs. USD debt (FX mismatch).
- Withholding on dividends and interest to foreign shareholders; treaty eligibility.
- Severance rules and labour-court exposure.

## 5. Brazil

### Checklist to verify (no facts asserted without a current source)
- CLT labour obligations and the size of the labour-litigation contingency; history of claims.
- Tax regime of the target (Simples Nacional, Lucro Presumido, Lucro Real) and how an acquisition changes it.
- Status and timeline of the consumption-tax reform (CBS / IBS transition) and its effect on pricing and margins.
- Cost of BRL debt (CDI-linked) vs. USD debt and the FX mismatch.
- Succession liability: tax and labour liabilities can follow the business in asset deals; structure and indemnities accordingly.
- LGPD for any data or AI project.
- Withholding and remittance rules for dividends, interest and services to foreign shareholders.

## How directors use this file

1. `cross-border-director` loads it for every non-US company or cross-border decision.
2. `finance-director` and `lead-investor` use the financing sections; `people-director` uses the labour sections.
3. Any figure used in an output must be copied **with** its source and date, or labelled *unverified*.
4. If a session finds a rule has changed, update this file, the "Last reviewed" date and `CHANGELOG.md`.
