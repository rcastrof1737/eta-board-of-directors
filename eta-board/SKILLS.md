# SKILLS.md — Flat Index of All Agents and Skills

Format: `<type>:<name>` — Description

Directors are generated from `scripts/directors_spec.py` by `scripts/build_board.py`, which also mirrors `.claude/skills/` to `.agents/skills/` (Codex CLI) and writes `.opencode/` files — see `CONTRIBUTING.md`.

## Director Agents (`.claude/agents/`)

- `agent:commercial-director` — Commercial Director — Growth, Pricing & Go-to-Market
- `agent:cross-border-director` — Cross-Border Director — US, Canada, Europe, Mexico & Brazil
- `agent:finance-director` — Finance Director — Ex-SMB CFO
- `agent:independent-director` — Independent Director — Governance, Risk & Alignment
- `agent:industry-operator` — Industry Operator — Sector Ex-CEO
- `agent:lead-investor` — Lead Search Investor — Capital, Returns & Exit
- `agent:operating-chair` — Operating Chair — Ex-SMB CEO
- `agent:operations-director` — Operations Director — Ex-COO, Systems & Digital
- `agent:people-director` — People Director — Ex-CHRO, Talent & Culture
- `agent:searcher-mentor` — Searcher Mentor — Ex-Search-Fund CEO

## Generic Methodology Skills (`.claude/skills/`)

- `skill:board` — ETA Board of Directors orchestrator for Search Fund and ETA-backed SMBs (US, Canada, Europe, Mexico, Brazil)
- `skill:analyze` — Generic problem analysis skill
- `skill:board-pack-review` — Design or review the board pack and KPI dashboard of a Search Fund / ETA-backed SMB: monthly KPI report, quarterly board meeting agenda, 13-week cash, covenant compliance, and action-item tracking
- `skill:brainstorm` — Generic brainstorming skill
- `skill:ceo-checkin` — Structure a mentoring / coaching check-in between a board director (typically the operating chair or searcher mentor) and the searcher-CEO or co-CEOs of a Search Fund / ETA-backed SMB
- `skill:decision-matrix` — Generic decision matrix skill
- `skill:report` — Generic structured report skill
- `skill:risk-assess` — Risk assessment skill for Search Fund / ETA-backed SMBs
- `skill:synthesize` — Generic synthesis skill
- `skill:value-creation-plan` — Build or update the value-creation plan (VCP) of a Search Fund / ETA-backed SMB, or test a decision against it

## Director Persona Invocation Shortcuts (`.claude/skills/`)

- `skill:cfo-skills` — Invoke the Finance Director — Ex-SMB CFO archetype for the current conversation
- `skill:chair-skills` — Invoke the Operating Chair — Ex-SMB CEO archetype for the current conversation
- `skill:commercial-skills` — Invoke the Commercial Director — Growth, Pricing & Go-to-Market archetype for the current conversation
- `skill:governance-skills` — Invoke the Independent Director — Governance, Risk & Alignment archetype for the current conversation
- `skill:industry-skills` — Invoke the Industry Operator — Sector Ex-CEO archetype for the current conversation
- `skill:investor-skills` — Invoke the Lead Search Investor — Capital, Returns & Exit archetype for the current conversation
- `skill:jurisdiction-skills` — Invoke the Cross-Border Director — US, Canada, Europe, Mexico & Brazil archetype for the current conversation
- `skill:mentor-skills` — Invoke the Searcher Mentor — Ex-Search-Fund CEO archetype for the current conversation
- `skill:ops-skills` — Invoke the Operations Director — Ex-COO, Systems & Digital archetype for the current conversation
- `skill:people-skills` — Invoke the People Director — Ex-CHRO, Talent & Culture archetype for the current conversation
