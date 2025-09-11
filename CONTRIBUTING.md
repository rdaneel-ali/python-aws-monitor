# Contributing to Python Health Monitor

Thank you for your interest in contributing!

## Environment Setup

```bash
git clone https://github.com/rdaneel-ali/python-health-monitor.git
cd python-health-monitor
pip install -e '.[dev]'
```

(Once pre-commit hooks are added:)
```bash
pre-commit install
# If a commit-msg hook is introduced:
pre-commit install --hook-type commit-msg
```

## Branch Naming

Pattern:
```
[milestone-slug]/[issue#]-[feature-slug]
```

Examples:
```
phase-2/8-mypy-baseline
phase-2/9-config-profiles
hardening/22-auth-refactor
```

Avoid branches without an issue; if necessary:
```
misc/short-exploratory-thing
```

## Commit Messages

Format:
```
<Action>: short imperative description
```

Allowed actions:
```
Add, Update, Fix, Refactor, Remove, Rename, Deprecate,
Test, Document, Format, Optimize, Configure, Revert, Merge
```

Examples:
```
Add: mypy baseline (Resolves #8)
Fix: retry delay off by one (#11)
Format: apply Black 24.4.2
Document: add config profile examples
```

Longer bodies (optional):
```
Why:
 - (reason for change)
How:
 - (brief notes)
Refs: #8
```

Auto-close issues with:
```
Resolves #8
Closes #11
```

## Code Quality

Tools:
- Black (formatting, line length 88)
- isort (imports)
- Flake8 + flake8-bugbear (lint)
- Pytest (tests)
- (Planned) mypy (types)

Run locally:
```bash
isort .
black .
flake8
pytest --cov=python_health_monitor
```

With pre-commit (if enabled):
```bash
pre-commit run --all-files
```

## Roadmap & Milestone Maintenance

The README serves as a living “status page” for milestones and key issues.
Keep the README’s roadmap in sync:
- Update the [Milestones & Progress](./README.md#milestones--progress) table when statuses change.
- Keep the [Active Milestone Detail](./README.md#active-milestone-detail) section current with ✅ 🚧 ⏳ icons and links.

Status legend:
- ✅ Completed & merged
- 🚧 In progress / actively worked
- ⏳ Not started

Update rules:
1. When an issue’s status changes:
   - ⏳ → 🚧 when work starts; 🚧 → ✅ when merged/closed.
2. When a milestone completes:
   - Flip its status to ✅ in the “Milestones & Progress” table.
3. Linking discipline:
   - Link milestone titles to their GitHub pages.
   - Link all issue numbers (e.g., [#12]) to the issue.
4. Detail sections:
   - Keep the active milestone’s expandable table current (icons + summaries).
   - Order by status: ✅ (first), then 🚧, then ⏳.
5. Representative issues:
   - In the “Milestones & Progress” table, include representative linked issues (not an exhaustive list).


## Pull Request Checklist

- [ ] Branch name follows convention
- [ ] `isort .` & `black .` produce no changes
- [ ] `flake8` passes
- [ ] Tests pass
- [ ] Docs updated (if behavior changes)
- [ ] Issue referenced (Resolves/Closes where appropriate)
- [ ] README Roadmap updated (icons, links, milestone status) if relevant
- [ ] CHANGELOG updated under “Unreleased” if user-visible behavior or contributor workflow changes

## Tests

Add/update tests when:
- Adding a new feature
- Changing configuration parsing
- Adjusting retry logic
- Fixing a bug

## CHANGELOG Policy

We use a simple Keep a Changelog–style [CHANGELOG](./CHANGELOG.md) file with an “Unreleased” section.

Update the CHANGELOG when:
- User-visible behavior changes (CLI flags, config keys/defaults, output)
- Notable features/fixes land
- Breaking changes occur
- Significant contributor-experience changes (e.g., mandatory hooks/CI) happen

Categorize under:
- Added, Changed, Deprecated, Removed, Fixed, Security
- Optionally tag contributor-only notes as “Internal” in the text

## Security

No secrets in code, config, or tests. Report concerns privately if needed.

## Questions?

Open an issue with label `question` or start a Discussion.
