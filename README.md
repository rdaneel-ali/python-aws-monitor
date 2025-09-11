# Python Health Monitor
[![CI](https://github.com/rdaneel-ali/python-health-monitor/actions/workflows/ci.yaml/badge.svg)](https://github.com/rdaneel-ali/python-health-monitor/actions/workflows/ci.yaml)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](./LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen)](https://www.python.org/downloads/)

[![Latest Release](https://img.shields.io/github/v/release/rdaneel-ali/python-health-monitor?include_prereleases&display_name=tag&sort=semver&label=latest%20release)](https://github.com/rdaneel-ali/python-health-monitor/releases)
[![Changelog](https://img.shields.io/badge/changelog-CHANGELOG.md-blue)](./CHANGELOG.md#010-beta---2025-09-10) <!-- update date to your actual release date -->

> Resilient, configurable endpoint health monitoring with structured logging and disciplined engineering practices.

## Executive Summary
Python Health Monitor provides a configuration‑driven way to probe HTTP endpoints with retries, timeouts, and clear success/failure reporting. The project intentionally demonstrates:
- Thoughtful milestone planning (phased evolution)
- Enforced contributor workflow (branch naming, commit conventions, pre-commit hooks)
- Quality automation (formatting, linting, hygiene)
- Extensibility foundation (future notification & typed resilience layers)

## Key Features
- YAML configuration (override or extend defaults)
- Retry + timeout control per monitor settings
- Structured logging to file + console
- Clean success/failure summarization
- Predictable project conventions & tooling

## Tech & Tooling
| Area | Choice |
|------|--------|
| Language | Python |
| Packaging | `pyproject.toml` (PEP 621) |
| Formatting | black + isort |
| Lint | flake8 + bugbear (Ruff considered later) |
| Hook Automation | pre-commit |
| Branch Policy | Regex‑validated (workflow) |
| Commit Convention | Action: imperative description |
| Testing | pytest (coverage planned) |
| Typing | Gradual – mypy planned (Phase 3) |

## Installation
```bash
pip install python-health-monitor
# Development mode
pip install -e '.[dev]'
```

## Quick Start
```bash
python-health-monitor
```
Example output (abridged):
```
Loaded configuration from config/config.yaml
Starting health checks...
Health check summary: 3/3 endpoints healthy
🎉 All endpoints are healthy!
```

## Configuration
Use a custom file:
```bash
python-health-monitor --config custom.yaml
```
Minimal override:
```yaml
monitor:
  timeout: 10
  retries: 5
```

Default (`config/config.yaml`):
```yaml
monitor:
  timeout: 5
  retries: 3

logging:
  file: "logs/health_monitor.log"
  level: "INFO"

endpoints:
  - name: "Python.org"
    url: "https://python.org"
```

## Architecture Snapshot
- Configuration layer (YAML → in-memory model)
- Monitor engine (loop, per-endpoint execution, retry logic)
- Logging abstraction (console + file)
- Summary reporting aggregator
- Extension vectors (notifications, richer status taxonomy, typed resilience wrappers)

## Milestones & Progress
| Phase | Status | Highlights | Representative Issues |
|-------|--------|------------|-----------------------|
| [Phase 1 – Foundations](https://github.com/rdaneel-ali/python-health-monitor/milestone/1) | ✅ Completed | Core monitor, config loading, basic logging | [#2](https://github.com/rdaneel-ali/python-health-monitor/issues/2) |
| [Phase 2 – Cloud Readiness & LocalStack Integration](https://github.com/rdaneel-ali/python-health-monitor/milestone/2) | 🚧 In Progress | Tooling, quality automation, config evolution groundwork | [#7](https://github.com/rdaneel-ali/python-health-monitor/issues/7), [#12](https://github.com/rdaneel-ali/python-health-monitor/issues/12), [#8](https://github.com/rdaneel-ali/python-health-monitor/issues/8), [#10](https://github.com/rdaneel-ali/python-health-monitor/issues/10) |
| Phase 3 – Typing & Extensibility | ⏳ Planned | Mypy baseline, typed response models | #8 (carried forward if unfinished) |
| Phase 4 – Config Evolution | ⏳ Planned | Layered / profile configs, env overrides | [#9](https://github.com/rdaneel-ali/python-health-monitor/issues/9) |
| Phase 5 – Resilience Enhancements | ⏳ Planned | Backoff strategies, jitter, circuit guards | [#11](https://github.com/rdaneel-ali/python-health-monitor/issues/11) |
| Ongoing – Hardening | ⏳ Rolling | Logging enrichment, fault classification | (label: hardening) |

> Current Focus: Phase 2 (tooling maturity + contributor experience) → then Phase 3 (types + programmatic API shape).

## Completed Milestones (Detail)
<details>
<summary><strong>Phase 1 – Foundations (Completed)</strong></summary>

**Closed Issues**

| Issue | Status | Summary |
|-------|--------|---------|
| [#2](https://github.com/rdaneel-ali/python-health-monitor/issues/2) | ✅ | Foundational Codebase |
| [#3](https://github.com/rdaneel-ali/python-health-monitor/issues/3) | ✅ | Comprehensive unit testing with `pytest` |
| [#4](https://github.com/rdaneel-ali/python-health-monitor/issues/4) | ✅ | Structured Logging |
| [#5](https://github.com/rdaneel-ali/python-health-monitor/issues/5) | ✅ | Packaging as Python module & CLI |
| [#6](https://github.com/rdaneel-ali/python-health-monitor/issues/6) | ✅ | Automated CI/CD workflow with GitHub Actions |

Rationale: Establish a minimal but extensible core before layering quality gates and typing.

</details>

## Active Milestone Detail
<details open>
<summary><strong>Phase 2 – Cloud Readiness & LocalStack Integration (In Progress)</strong></summary>

**Legend:** ✅ Completed & merged · 🚧 In progress / actively worked · ⏳ Not started

| Issue | Status | Summary |
|-------|--------|---------|
| [#7](https://github.com/rdaneel-ali/python-health-monitor/issues/7) | ✅ | Code Quality enforcement with flake8 and black |
| [#12](https://github.com/rdaneel-ali/python-health-monitor/issues/12) | 🚧 | Pre-Commit Hooks for Code Style |
| [#8](https://github.com/rdaneel-ali/python-health-monitor/issues/8) | ⏳ | Type Checking with mypy |
| [#10](https://github.com/rdaneel-ali/python-health-monitor/issues/10) | ⏳ | Environment Variable Overrides |
| [#9](https://github.com/rdaneel-ali/python-health-monitor/issues/9) | ⏳ | Config Profiles (dev/prod) |
| [#11](https://github.com/rdaneel-ali/python-health-monitor/issues/11) | ⏳ | Retry Improvements |

**Focus This Phase**
- Mature contributor workflow (hooks, branch policy, documentation)
- Prepare ground for typing & layered configs
- Begin resilience refinements (retry enhancements; env/config overrides)

</details>

## Upcoming Roadmap (High-Level)
- Phase 3: Type safety (mypy), improved error surface (result objects)
- Phase 4: Layered configuration (base → env → local override), validation
- Phase 5: Retry backoff strategies (exponential, jitter), failure classification
- Notification Plugins: Slack / Webhook / Email (post Phase 5)
- Operational Enhancements: Coverage reporting, CI matrix (Python versions), release automation

## Engineering Practices
| Practice | Mechanism |
|----------|-----------|
| Branch Naming | GitHub Action (`branch-name-check.yml`) |
| Commit Convention | Commit-msg hook (regex validation) |
| Formatting Enforcement | black + isort via pre-commit |
| Hygiene | trailing whitespace / EOF / mixed line endings |
| Security Hygiene | detect-private-key hook |
| Lint Strictness | flake8 + bugbear (potential Ruff migration) |
| Planned Static Types | mypy (gradual introduction) |

## Project Structure
Core layout:
```
python-health-monitor/
├── src/python_health_monitor/
│   └── monitor.py
├── config/
├── tests/
├── pyproject.toml
├── README.md
└── LICENSE
```
<details>
<summary><strong>Development & Automation Files</strong></summary>

```
.pre-commit-config.yaml
CONTRIBUTING.md
.flake8
scripts/
  └── validate_commit_msg.py
.github/
  ├── workflows/
  │   ├── branch-name-check.yml
  │   └── (CI workflows)
  ├── pull_request_template.md
  └── commit_template.txt
```
</details>

## Issues & Planning Links
- [Open Issues](https://github.com/rdaneel-ali/python-health-monitor/issues)
- [Milestones](https://github.com/rdaneel-ali/python-health-monitor/milestones)
- [Changelog](./CHANGELOG.md)
- [Contributing Guide](./CONTRIBUTING.md)
- [Roadmap Label](https://github.com/rdaneel-ali/python-health-monitor/issues?q=is%3Aopen+label%3Aroadmap)
- [Good First Issues](https://github.com/rdaneel-ali/python-health-monitor/issues?q=is%3Aopen+label%3A%22good+first+issue%22)
- [Help Wanted](https://github.com/rdaneel-ali/python-health-monitor/issues?q=is%3Aopen+label%3A%22help+wanted%22)
- [Recently Updated](https://github.com/rdaneel-ali/python-health-monitor/issues?q=is%3Aopen+sort%3Aupdated-desc)

## Contributing (Snapshot)
1. Create a branch: `phase-2/12-pre-commit-hooks`
2. Run: `pip install -e '.[dev]'`
3. Install hooks: `pre-commit install && pre-commit install --hook-type commit-msg`
4. Validate: `pre-commit run --all-files && pytest`
5. PR referencing an issue: `Resolves #12`

Full details: see [CONTRIBUTING.md](./CONTRIBUTING.md)

## License
GPL v2 – see [LICENSE](./LICENSE)

---

> Looking at this project for collaboration or evaluation? Feel free to open a discussion or issue; roadmap items are intentionally staged for incremental refinement.
