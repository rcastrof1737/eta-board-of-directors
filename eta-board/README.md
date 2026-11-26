# ETA Board of Directors

**An AI board of directors for SMBs acquired through a Search Fund or ETA, built to make sound decisions and to mentor the searcher who became CEO.**

Adapted from [markusbegerow/board-of-directors](https://github.com/markusbegerow/board-of-directors). The original multi-agent mechanics are kept: parallel independent director votes, a conflict matrix, synthesis, and the same skill/agent layout for Claude Code, Codex CLI and OpenCode. The directors and the objectives of the board have been redesigned.

> **Important notice:** All directors are **fictional composite role archetypes** built from the typical profiles of Search Fund and ETA board members (ex-SMB CEOs, ex-searchers, lead search investors, ex-CFOs, sector operators, independent directors). They do not represent any real person. Outputs are analytical and mentoring aids, **not** a substitute for your real board, investors, counsel, tax advisors or lenders.

## Who It Is For

- A searcher (solo or duo) who has acquired a company and is now its CEO.
- Search-fund and ETA investors who want a consistent board playbook across portfolio companies.
- Companies in the **United States, Canada and Europe**, and exceptionally **Mexico and Brazil**.

## The Board

| Agent | Persona skill | Director archetype | Primary perspective |
|---|---|---|---|
| `operating-chair` | `chair-skills` | Operating Chair — Ex-SMB CEO | Board leadership, CEO-board operating rhythm, first-100-days discipline, and whole-company prioritization |
| `searcher-mentor` | `mentor-skills` | Searcher Mentor — Ex-Search-Fund CEO | Searcher-to-CEO transition, solo vs. duo dynamics, leadership credibility, board relationship, and personal resilience |
| `lead-investor` | `investor-skills` | Lead Search Investor — Capital, Returns & Exit | Capital structure, investor returns (MOIC/IRR), add-ons, refinancing, follow-ons, and exit readiness |
| `finance-director` | `cfo-skills` | Finance Director — Ex-SMB CFO | Cash, 13-week cash flow, covenants, working capital, budgeting, reporting quality, and lender relationships |
| `industry-operator` | `industry-skills` | Industry Operator — Sector Ex-CEO | Sector economics, customers, competitors, suppliers, regulation, and operating benchmarks for the company's specific industry |
| `commercial-director` | `commercial-skills` | Commercial Director — Growth, Pricing & Go-to-Market | Pricing, sales process, customer retention and concentration, marketing basics, and organic growth for owner-founded SMBs |
| `operations-director` | `ops-skills` | Operations Director — Ex-COO, Systems & Digital | Operational excellence, processes, ERP/IT systems, pragmatic automation and AI, quality, and integration of add-ons |
| `people-director` | `people-skills` | People Director — Ex-CHRO, Talent & Culture | Leadership team, key-employee retention, hiring, compensation and equity, culture through ownership change, and labour law exposure |
| `independent-director` | `governance-skills` | Independent Director — Governance, Risk & Alignment | Board governance, conflicts of interest, minority and seller-rollover rights, related parties, compliance, and investor–CEO alignment |
| `cross-border-director` | `jurisdiction-skills` | Cross-Border Director — US, Canada, Europe, Mexico & Brazil | Jurisdiction-specific financing, tax, labour, regulatory and cultural considerations; cross-border expansion and add-ons |

Every director is hands-on: each vote ends with a concrete next step for the next 30 days and a **coaching note to the CEO**.

## What Changed vs. the Original

| Original | ETA Board |
|---|---|
| 10 archetypes inspired by famous tech CEOs / AI leaders | 10 fictional composite roles typical of strong search-fund boards |
| Generic strategy (AI, platforms, infrastructure) | SMB lifecycle: first 100 days, budget, pricing, people, covenants, add-ons, refinancing, exit |
| Vote = thesis, argument, risk, next step | + coaching note to the CEO; board output adds stakeholder alignment check and mentoring summary |
| Generic risk categories | Key person, concentration, liquidity/covenants, labour, jurisdiction, investor–searcher–seller alignment |
| No geography | `cross-border-director` + `references/geography-playbook.md` (sourced, dated rules for US, Canada, Europe, Mexico, Brazil) |
| 6 shared skills | + `value-creation-plan`, `board-pack-review`, `ceo-checkin` |
| 44 hand-synced files | One spec (`scripts/directors_spec.py`) + generator (`scripts/build_board.py`) with a `--check` drift test |

## Selection Table

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

## Quick Start

1. `git clone` this repository and open it as the project directory in Claude Code, Codex CLI or OpenCode.
2. Fill in `references/company-context-template.md` (keep real data outside the repo).
3. Run `/board [decision question]`, or ask one director: `Use the finance-director agent and evaluate: [question]`.

See `QUICKSTART.md` and `INSTALLATION.md` for details.

## Repository Layout

| Path | Count | Purpose |
|---|---|---|
| `.claude/agents/` | 10 | Claude Code director subagents (generated) |
| `.claude/skills/` | 20 | Orchestrator, 9 shared skills, 10 persona skills |
| `.agents/skills/` | 20 | Codex CLI mirror (generated, byte-identical) |
| `.opencode/agent/` | 10 | OpenCode subagents (generated) |
| `.opencode/command/` | 20 | OpenCode slash commands |
| `references/` | 5 | Methodology, archetype rules, source hygiene, geography playbook, company-context template |
| `scripts/` | 4 | Spec, generator, frontmatter validator, `SKILLS.md` generator |

## Maintaining

```bash
pip install -r requirements.txt
python scripts/build_board.py            # regenerate from scripts/directors_spec.py
python scripts/build_board.py --check    # fail on drift
python scripts/validate_yaml_frontmatter.py
python scripts/generate_skills_md.py
```

## License

Same license as the original repository (see `LICENSE`).
