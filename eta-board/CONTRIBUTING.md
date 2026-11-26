# Contributing

## PR Checklist

- [ ] Content in English unless a translation is the purpose of the PR (see `AGENTS.md` §2).
- [ ] Directors remain fictional composite role archetypes (`references/archetype-guidelines.md`).
- [ ] Methodology followed per `references/methodik-board.md`.
- [ ] Any regulatory, tax or financing fact has country, source and verification date; `references/geography-playbook.md` updated if a rule changed.
- [ ] No real company data, personal data, cap tables, loan agreements or secrets.
- [ ] `python scripts/build_board.py --check` passes.
- [ ] `python scripts/validate_yaml_frontmatter.py` passes.
- [ ] `SKILLS.md` regenerated (`python scripts/generate_skills_md.py`) if names or descriptions changed.
- [ ] `CHANGELOG.md` updated.

## How the Files Are Produced

| Path | Count | Produced by |
|---|---|---|
| `.claude/agents/<name>.md` | 10 | `scripts/build_board.py` from `scripts/directors_spec.py` |
| `.claude/skills/<persona>-skills/SKILL.md` | 10 | `scripts/build_board.py` |
| `.claude/skills/board/SKILL.md` | 1 | `scripts/build_board.py` (selection table from the spec) |
| `.claude/skills/<shared>/SKILL.md` | 9 | hand-edited |
| `.agents/skills/*/SKILL.md` | 20 | byte-identical mirror written by `scripts/build_board.py` |
| `.opencode/agent/<name>.md` | 10 | `scripts/build_board.py` |
| `.opencode/command/<name>.md` | 20 | 11 generated (persona + board), 9 hand-edited (shared) |

## Adding or Changing a Director

1. Edit or add an entry in `DIRECTORS` in `scripts/directors_spec.py` (all fields required: profile, role, mission, when, principles, questions, method, kpis, mentoring, red_flags, output, boundaries, skills).
2. Add the director to the relevant rows of `SELECTION` and, if needed, `SELECTION_RULES`.
3. Run `python scripts/build_board.py`, then `python scripts/validate_yaml_frontmatter.py` and `python scripts/generate_skills_md.py`.
4. Update `README.md` and `CLAUDE.md` if the roster changed.

## Adding a Shared Skill

1. Create `.claude/skills/<name>/SKILL.md` with frontmatter, the disclaimer, inputs, steps, output format and usage.
2. Create `.opencode/command/<name>.md`.
3. Add the skill's one-line blurb to `SKILL_BLURBS` in `scripts/build_board.py` if directors will reference it.
4. Run the build, validation and `SKILLS.md` scripts.
