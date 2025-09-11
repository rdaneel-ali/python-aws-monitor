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

## Pull Request Checklist

- [ ] Branch name follows convention
- [ ] `isort .` & `black .` produce no changes
- [ ] `flake8` passes
- [ ] Tests pass
- [ ] Docs updated (if behavior changes)
- [ ] Issue referenced (Resolves/Closes where appropriate)

## Tests

Add/update tests when:
- Adding a new feature
- Changing configuration parsing
- Adjusting retry logic
- Fixing a bug

## Security

No secrets in code, config, or tests. Report concerns privately if needed.

## Questions?

Open an issue with label `question` or start a Discussion.