#!/usr/bin/env python3
"""Render the ETA / Search Fund board from scripts/directors_spec.py.

Writes, for every director:
  .claude/agents/<name>.md            Claude Code subagent
  .claude/skills/<skill>/SKILL.md     persona skill (Claude Code / OpenCode)
  .opencode/agent/<name>.md           OpenCode subagent
  .opencode/command/<skill>.md        OpenCode slash command
and the `board` orchestrator (skill + OpenCode command). Finally mirrors every
.claude/skills/*/SKILL.md byte-identically into .agents/skills/ (Codex CLI).

Usage:  python scripts/build_board.py          # write files
        python scripts/build_board.py --check  # exit 1 if anything is out of date
"""
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from directors_spec import (  # noqa: E402
    DECISION_LOGIC, DIRECTORS, DISCLAIMER, LABELS, SELECTION, SELECTION_RULES,
)

ROOT = Path(__file__).resolve().parent.parent
BY_NAME = {d["name"]: d for d in DIRECTORS}

SKILL_BLURBS = {
    "analyze": "decompose the problem and classify assumptions",
    "brainstorm": "generate options before converging",
    "decision-matrix": "score options against weighted criteria",
    "risk-assess": "likelihood × impact register with SMB risk categories",
    "synthesize": "merge perspectives into one recommendation",
    "report": "format the final memo for the board or the CEO",
    "value-creation-plan": "link the decision to the value-creation plan",
    "board-pack-review": "define or review the KPIs and board-pack content",
    "ceo-checkin": "structure a coaching conversation with the CEO",
}


def lc(s):
    """Lower-case only the first character, preserving acronyms (CEO, ERP, SBA)."""
    return s[:1].lower() + s[1:] if s and not s[:2].isupper() else s


def bullets(items, numbered=False):
    return "\n".join(f"{i}. {x}" if numbered else f"- {x}" for i, x in enumerate(items, 1))


def description(d):
    return f"{d['title']}. Spawnable ETA board director for {lc(d['tagline'])}. Use for Search Fund / ETA-backed SMB decisions in the US, Canada, Europe, Mexico or Brazil."


def persona_body(d, mode):
    """Shared long-form body for the Claude agent and the persona skill."""
    skills = "\n".join(f"- `/{s}` — {SKILL_BLURBS[s]}" for s in d["skills"])
    start = f"""```text
Adopt the ETA board archetype "{d['title']}" for the following task.

Company context (see references/company-context-template.md):
[stage since closing, sector, country, size, capital structure, solo/duo CEO]

Decision or question:
[insert]

Constraints:
[cash, covenants, time, people, regulation]

Lay out key assumptions and open questions first. Then give a prioritized
recommendation with concrete next steps and a coaching note to the CEO.
Separate robust findings, hypotheses and speculative options.
```"""
    if mode == "agent":
        invoke = (f"```text\nUse the `{d['name']}` agent and evaluate:\n[question]\n```\n\n"
                  f"This Task-spawnable subagent format is Claude-Code-specific. Codex CLI and OpenCode users reach this "
                  f"director via the `{d['skill']}` skill (`.agents/skills/{d['skill']}/` or `.claude/skills/{d['skill']}/`) "
                  f"or the `/{d['skill']}` OpenCode command.")
        invoke_h = "## Short Command"
    else:
        invoke = (f"- Claude Code: `/{d['skill']} [question]`, or spawn the `{d['name']}` agent\n"
                  f"- OpenCode: `/{d['skill']} [question]`\n"
                  f"- Codex CLI: describe the task and reference `{d['skill']}`; it auto-loads from `.agents/skills/{d['skill']}/`.")
        invoke_h = "## Invocation"
    return f"""# {d['title']}

{DISCLAIMER}

## Profile

{d['profile']}

## Role

**{d['role']}**

## Mission

{d['mission']}

## When to Use

{bullets(d['when'])}

## Inputs

- Company context: stage since closing, sector, country / jurisdictions, revenue and EBITDA, capital structure, solo or duo CEO (template: `references/company-context-template.md`).
- The decision or question, with options if known.
- Constraints: cash, covenants, time, people, regulation.
- Any relevant data (board pack, budget, KPI history).

If the stage, country or sector is missing and matters for the answer, ask before advising.

## Guiding Principles

{bullets(d['principles'], numbered=True)}

## Key Questions

{bullets(d['questions'])}

## Working Method

{bullets(d['method'], numbered=True)}

## KPIs This Director Watches

{bullets(d['kpis'])}

## Mentoring Stance Toward the Searcher-CEO

{d['mentoring']}

## Red Flags

{bullets(d['red_flags'])}

## Output Format

Respond in this structure by default:

{bullets(f"**{x}**" for x in d['output'])}

## Decision Logic

Prioritize recommendations by:
{bullets(DECISION_LOGIC, numbered=True)}

Label every recommendation as one of:
{bullets(f"**{x}**" for x in LABELS)}

Separate **robust findings**, **hypotheses** and **speculative options**. Any regulatory, tax or financing figure must carry its source and verification date, or be marked as unverified.

## Boundaries

{bullets(d['boundaries'])}
- Strategic analysis only: not legal, tax, investment or financial advice.

## Shared Skills Available

{skills}

## Start Prompt

{start}

{invoke_h}

{invoke}
"""


def render_agent(d):
    return f"---\nname: {d['name']}\ndescription: \"{description(d)}\"\ntools: [Read, WebSearch, WebFetch]\n---\n\n" + persona_body(d, "agent")


def render_skill(d):
    desc = f"Invoke the {d['title']} archetype for the current conversation. Use for {lc(d['tagline'])} in Search Fund / ETA-backed SMBs."
    return f"---\nname: {d['skill']}\ndescription: \"{desc}\"\n---\n\n" + persona_body(d, "skill")


def render_opencode_agent(d):
    return f"""---
description: "{description(d)}"
mode: subagent
---

{DISCLAIMER}

You are the {d['title']} archetype on the board of a Search Fund / ETA-backed SMB. {d['profile']} Your role: {lc(d['role'])}. Mission: {d['mission']}

Principles: {' '.join(d['principles'])}

Ask yourself: {' '.join(d['questions'])}

Method: {' '.join(m.split(' *(')[0] for m in d['method'])} Watch these KPIs: {', '.join(d['kpis'])}. Mentoring stance: {d['mentoring']} Red flags: {'; '.join(d['red_flags'])}.

Respond with: {', '.join(lc(x) for x in d['output'])}. Prioritize by {', '.join(lc(x.split(' (')[0]) for x in DECISION_LOGIC)}; label every recommendation **Act Now / Pilot / Investigate Further / Discard**. If stage, country or sector is missing and matters, ask first. Boundaries: {' '.join(d['boundaries'])} Strategic analysis only, not legal, tax, investment or financial advice.
"""


def render_opencode_command(d):
    return f"""---
description: "Invoke the {d['title']} archetype. Use for {lc(d['tagline'])}."
agent: {d['name']}
---
Adopt the "{d['title']}" ETA board archetype (a fictional composite role, not a real person — see the disclaimer in `.opencode/agent/{d['name']}.md`). Apply its principles to the company context and question below, and give a prioritized recommendation labelled Act Now / Pilot / Investigate Further / Discard, plus a coaching note to the CEO.

Task: $ARGUMENTS
"""


def selection_table():
    rows = "\n".join(f"| {t} | {' + '.join(ds)} |" for t, ds in SELECTION)
    return "| Decision type | Directors to convene |\n|---|---|\n" + rows


def roster_table():
    rows = "\n".join(f"| `{d['name']}` | {d['title']} | {d['tagline']} |" for d in DIRECTORS)
    return "| Agent | Director archetype | Primary perspective |\n|---|---|---|\n" + rows


def render_board():
    return f"""---
name: board
description: "ETA Board of Directors orchestrator for Search Fund and ETA-backed SMBs (US, Canada, Europe, Mexico, Brazil). Convenes 3–5 director archetypes (operating chair, searcher mentor, lead investor, finance, industry, commercial, operations, people, independent governance, cross-border), collects independent votes, surfaces conflicts, and synthesizes a decision proposal plus mentoring guidance for the searcher-CEO."
---

# ETA Board of Directors — Orchestrator

{DISCLAIMER}

## Purpose

Simulate a high-quality Search Fund / ETA board for a searcher (solo or duo) who has become the CEO of an acquired SMB. The board's job is twofold: help reach a sound decision, and **develop the CEO** while doing so.

## Available Directors

{roster_table()}

## Inputs

1. **Company context** — use `references/company-context-template.md` (stage since closing, sector, jurisdictions, size, capital structure, solo/duo CEO, investor base). If stage, country or sector is missing and matters, ask before convening.
2. **Decision question** and options, if known.
3. **Constraints** — cash, covenants, time, people, regulation.

## Selection Rules

{selection_table()}

{bullets(SELECTION_RULES)}

## Moderation Process

1. Frame the decision question, options and company stage. *(use `/analyze` if the question is fuzzy)*
2. Select 3–5 directors using the rules above and state why each was chosen and who was left out.
3. Spawn the selected director agents **in parallel**; each argues independently and does not see the others' votes.
4. Collect each vote: thesis, strongest argument, biggest risk, recommended next step, coaching note to the CEO.
5. Build the conflict matrix; separate consensus, dissent and open assumptions; mark conflicts resolvable with data vs. genuine value trade-offs.
6. Run the **alignment check**: does the decision affect investors, the searcher(s), the seller rollover, lenders or employees differently?
7. Synthesize with `/synthesize`; use `/decision-matrix` if directors disagree on direction and `/risk-assess` for a combined risk register.
8. Define a reversible next step and what the CEO brings to the next board meeting.

## Output Format

### 1. Decision question and company stage
### 2. Directors convened (and why; who was left out)
### 3. Individual votes
For each director: **Central thesis**, **Strongest argument**, **Biggest risk**, **Recommended next step**, **Coaching note to the CEO**.
### 4. Conflict matrix
| Topic | Perspective A | Perspective B | Resolvable with data? | Resolution |
|---|---|---|---|---|
### 5. Stakeholder alignment check
| Party | Effect of the decision | Aligned? | Action |
|---|---|---|---|
(investors, searcher-CEO(s), seller / rollover, lenders, key employees, customers)
### 6. Board consensus
### 7. Minority view
### 8. Decision proposal
- **Recommendation** (Act Now / Pilot / Investigate Further / Discard)
- **Prerequisites** (including approvals and consents required)
- **Abort criteria**
- **Next 30 days**
- **Owner**
- **Success metric**
- **Jurisdiction-specific conditions** (if any; with verification date)
### 9. Mentoring summary for the CEO
Three sentences: what the CEO did well in framing this, the one capability to build, and what to bring to the next board meeting.

## Shared Skills

- `/synthesize` — merge director votes into the integrated recommendation
- `/risk-assess` — cross-perspective risk register (SMB categories)
- `/decision-matrix` — score options when directors disagree
- `/value-creation-plan` — anchor the decision in the value-creation plan
- `/board-pack-review` — define the KPIs and the board-pack follow-up
- `/ceo-checkin` — turn the board's feedback into a coaching conversation
- `/report` — format the final memo

## Start Prompt

```text
Use the ETA Board of Directors orchestrator.

Company context:
[stage since closing, sector, country, revenue/EBITDA, capital structure, solo/duo CEO]

Decision question:
[question]

Options:
[options]

Constraints:
[cash, covenants, time, people, regulation]

Select the appropriate directors, produce independent votes with coaching notes,
surface conflicts and stakeholder alignment, and synthesize a prioritized decision
proposal plus a mentoring summary for the CEO.
```

## Invocation

- Claude Code: `/board [decision question]`
- OpenCode: `/board [decision question]`
- Codex CLI: describe the task; the skill auto-loads from `.agents/skills/board/`.
"""


def render_board_command():
    return f"""---
description: "ETA Board of Directors orchestrator for Search Fund / ETA-backed SMBs. Convene 3–5 director archetypes, collect independent votes, surface conflicts and stakeholder alignment, and synthesize a decision proposal plus mentoring guidance for the CEO."
---
Disclaimer: all directors are fictional composite role archetypes, not real people (see `AGENTS.md`).

Follow `.claude/skills/board/SKILL.md`: confirm the company context (stage, sector, jurisdictions, capital structure, solo/duo CEO), select 3–5 directors with the selection table and rules (always add cross-border-director for Canada/Europe/Mexico/Brazil or cross-border decisions, and independent-director when shareholder interests may diverge), produce each director's independent vote (thesis, strongest argument, biggest risk, next step, coaching note), build the conflict matrix and stakeholder alignment check, and synthesize a decision proposal labelled Act Now / Pilot / Investigate Further / Discard with a mentoring summary for the CEO.

Decision question: $ARGUMENTS
"""


def outputs():
    files = {}
    for d in DIRECTORS:
        files[f".claude/agents/{d['name']}.md"] = render_agent(d)
        files[f".claude/skills/{d['skill']}/SKILL.md"] = render_skill(d)
        files[f".opencode/agent/{d['name']}.md"] = render_opencode_agent(d)
        files[f".opencode/command/{d['skill']}.md"] = render_opencode_command(d)
    files[".claude/skills/board/SKILL.md"] = render_board()
    files[".opencode/command/board.md"] = render_board_command()
    return files


def main():
    check = "--check" in sys.argv
    stale = []
    for rel, content in outputs().items():
        p = ROOT / rel
        if check:
            if not p.exists() or p.read_text(encoding="utf-8") != content:
                stale.append(rel)
            continue
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    # Mirror every Claude skill to the Codex path.
    for skill_md in sorted((ROOT / ".claude/skills").glob("*/SKILL.md")):
        target = ROOT / ".agents/skills" / skill_md.parent.name / "SKILL.md"
        if check:
            if not target.exists() or target.read_bytes() != skill_md.read_bytes():
                stale.append(str(target.relative_to(ROOT)))
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(skill_md, target)
    if check:
        if stale:
            print("Out of date (run python scripts/build_board.py):\n  " + "\n  ".join(stale))
            return 1
        print("OK: generated files are up to date.")
    else:
        print(f"Wrote {len(outputs())} generated files and mirrored .claude/skills -> .agents/skills.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
