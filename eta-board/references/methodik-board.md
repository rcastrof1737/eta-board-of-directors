---
name: methodik-board
description: 5-step methodology for all ETA Board of Directors sessions (Search Fund / ETA-backed SMBs). Defines how to frame a decision, select directors, collect votes, surface conflicts, and synthesise an integrated recommendation.
---

# Board of Directors — Decision Methodology

This methodology applies to every board session and is referenced by `AGENTS.md` §3. It governs both the `/board` orchestrator skill and any individual director agent working within a board context.

## Step 1: Frame the Decision Question

0. Confirm the company context (`references/company-context-template.md`): stage since closing, sector, jurisdictions, capital structure, solo/duo CEO. Ask for what is missing.
1. State the core decision in one clear sentence.
2. List the available options (if known); if options are open, say so explicitly.
3. Identify hard constraints (budget, timeline, regulation, technology limits).
4. Identify soft constraints (preferences, conventions, inherited habits — these can be challenged).
5. State the decision horizon: reversible short-term action, or long-term strategic commitment?

## Step 2: Select Directors

Use this table to select 3–5 directors. For questions spanning multiple categories, combine the relevant sets and cap at 5.

| Decision type | Directors to convene |
|---|---|
| First 100 days, seller transition | operating-chair + searcher-mentor + people-director + industry-operator |
| Annual budget / operating plan | finance-director + operating-chair + commercial-director + lead-investor |
| Pricing and commercial strategy | commercial-director + industry-operator + finance-director |
| Key hire, firing or org redesign | people-director + searcher-mentor + operating-chair |
| Underperformance, covenant pressure, turnaround | finance-director + lead-investor + operating-chair + operations-director + independent-director |
| Add-on acquisition / buy-and-build | lead-investor + finance-director + industry-operator + operations-director |
| Refinancing, dividend recap, new equity | lead-investor + finance-director + independent-director |
| ERP, automation or AI investment | operations-director + finance-director + industry-operator |
| Geographic expansion / cross-border deal | cross-border-director + commercial-director + finance-director + independent-director |
| CEO performance, co-CEO conflict, board–CEO relationship | searcher-mentor + operating-chair + independent-director + people-director |
| Searcher equity, vesting tranches, leaver events | independent-director + lead-investor + searcher-mentor |
| Earn-out, seller note or seller dispute | independent-director + lead-investor + finance-director |
| Exit preparation / sale process | lead-investor + operating-chair + finance-director + independent-director |

- Choose 3–5 directors. For questions spanning several types, combine the sets and cap at 5.
- If the company or the decision involves Canada, Europe, Mexico or Brazil, or any cross-border element, ALWAYS include `cross-border-director` (drop the least relevant director to stay at 5).
- If the decision touches the searcher's own economics or a conflict between shareholder groups, ALWAYS include `independent-director`.
- In the first 12 months after closing, prefer including `operating-chair` or `searcher-mentor`.
- `industry-operator` must be told the sector; if it is missing, ask the user before convening.

Document why each director was selected. Justify inclusions and exclusions.

## Step 3: Collect Independent Votes

Spawn selected directors **in parallel** — each works independently to avoid anchoring effects. Each director produces:

- **Central thesis** (1 sentence)
- **Strongest argument** for their recommendation
- **Biggest risk** they see
- **Recommended next step**
- **Coaching note to the CEO**

Directors must not read each other's votes before completing their own.

## Step 4: Surface Conflicts

Construct a conflict matrix:

| Topic | Perspective A | Perspective B | Resolution |
|---|---|---|---|

Identify:
- Areas of genuine **consensus** (all or most directors agree).
- **Dissent** (significant disagreement on direction, priority, or risk).
- **Open assumptions** (recommendations that depend on unverified premises).

Clearly mark which conflicts are resolvable with more data and which are fundamental value trade-offs.

## Step 5: Synthesise

Using `/synthesize`, produce an integrated recommendation that:

1. States the board consensus (what most directors agree on).
2. Preserves the minority view with its rationale.
3. Gives a single prioritised recommendation labelled as one of:
   - **Act Now** — implement immediately
   - **Pilot** — test in controlled scope first
   - **Investigate Further** — more data needed before committing
   - **Discard** — not worth pursuing
4. Defines the prerequisites, abort criteria, and responsible role.
5. Proposes a concrete, reversible next step within 30 days.
6. Runs a stakeholder alignment check (investors, searcher-CEO(s), seller / rollover, lenders, key employees, customers).
7. Ends with a mentoring summary for the CEO: what went well, one capability to build, what to bring to the next board meeting.

## Output Formatting Rules

- Complete sentences throughout; no bare bullet skeletons as the final output.
- Intermediate conclusions are clearly marked: "Interim finding: …"
- Speculative options are marked as speculative: "Hypothesis (unverified): …"
- All outputs begin with the archetype disclaimer per `AGENTS.md` §7.
