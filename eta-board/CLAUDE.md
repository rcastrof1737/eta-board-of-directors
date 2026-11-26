@AGENTS.md

## Claude Code specifics

Ten director subagents live under `.claude/agents/`: `operating-chair`, `searcher-mentor`, `lead-investor`, `finance-director`, `industry-operator`, `commercial-director`, `operations-director`, `people-director`, `independent-director`, `cross-border-director`.

Twenty skills live under `.claude/skills/` and trigger based on the request: the `board` orchestrator; 9 shared skills (`analyze`, `brainstorm`, `decision-matrix`, `risk-assess`, `synthesize`, `report`, `value-creation-plan`, `board-pack-review`, `ceo-checkin`); and 10 persona shortcuts (`chair-skills`, `mentor-skills`, `investor-skills`, `cfo-skills`, `industry-skills`, `commercial-skills`, `ops-skills`, `people-skills`, `governance-skills`, `jurisdiction-skills`).

Do not hand-edit generated director files; edit `scripts/directors_spec.py` and run `python scripts/build_board.py`.
