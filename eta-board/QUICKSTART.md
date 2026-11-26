# Quickstart (2 minutes)

1. Clone and open this repository as the project directory in Claude Code, Codex CLI or OpenCode. No install step.
2. Fill in `references/company-context-template.md` for your company (keep the filled copy outside the repo).
3. Convene the board: Claude Code / OpenCode `/board [decision question]`; Codex CLI: describe the decision in plain language.
4. Or ask one director:
   - `Use the operating-chair agent and evaluate: [question]`
   - `Use the finance-director agent and evaluate: [question]`
   - OpenCode: `/cfo-skills [question]`, `/mentor-skills [question]`, ...
5. You get a structured output with the disclaimer, labelled recommendations, coaching notes and a mentoring summary for the CEO.

## Typical Session

```text
/board
Company context: 7 months post-close, Mexico (Monterrey) industrial maintenance services,
MXN 180M revenue, duo co-CEOs, senior bank debt in MXN + USD seller note, investors from US and LatAm.
Decision question: Should we acquire a smaller competitor in Querétaro now, funded by an earn-out and a follow-on equity round?
```

The orchestrator selects lead-investor, finance-director, operations-director, industry-operator and cross-border-director (always added outside the US), collects independent votes, builds the conflict matrix and stakeholder alignment check, and proposes a decision plus a mentoring summary.

## Useful Shared Skills

- `/value-creation-plan` — 100-day plan, 12-month priorities, equity value bridge
- `/board-pack-review` — KPI pack and quarterly board-meeting review, with feedback to the CEO
- `/ceo-checkin` — monthly mentoring check-in or rehearsal of a difficult conversation
- `/risk-assess`, `/decision-matrix`, `/analyze`, `/brainstorm`, `/synthesize`, `/report`

Outputs are analytical and mentoring aids, not legal, tax, investment or financial advice. See `INSTALLATION.md` for the full setup guide.
