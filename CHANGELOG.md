# Changelog
All notable changes to this project will be documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and the project aims for [Semantic Versioning](https://semver.org/).

For contribution guidelines on when and how to update this file, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## [Unreleased]
### Added
- (place new changes here)

### Changed
- (place new changes here)

### Fixed
- (place new changes here)

## [0.1.0] - 2025-09-11
Promotes the project from beta to the first stable release, carrying forward the Phase 1 baseline and introducing contributor tooling and documentation improvements.

Release focus:
- Phase 1 foundations promoted from [0.1.0-beta](#010-beta---2025-09-10).
- Early Phase 2 developer-experience improvements.

### Added
- Project-wide [CHANGELOG](./CHANGELOG.md).
- Contributing guide enhancements and cross-links with the README.

### Changed
- README: Milestones & Progress table with linked milestones/issues; Active Milestone detail with status icons.
- README/CONTRIBUTING cross-links and roadmap maintenance guidance.

### Internal
- Code quality enforcement with flake8 and black ([#7](https://github.com/rdaneel-ali/python-health-monitor/issues/7)).
- Pre-commit hooks for code style and hygiene ([#12](https://github.com/rdaneel-ali/python-health-monitor/issues/12)).

## [0.1.0-beta] - 2025-09-10
Release focus: [Phase 1 – Foundations](https://github.com/rdaneel-ali/python-health-monitor/milestone/1)

### Added
- Core health monitor, configuration loading, retries/timeouts ([#2](https://github.com/rdaneel-ali/python-health-monitor/issues/2)).
- Unit testing with `pytest` ([#3](https://github.com/rdaneel-ali/python-health-monitor/issues/3)).
- Structured logging ([#4](https://github.com/rdaneel-ali/python-health-monitor/issues/4)).
- Package as python module and CLI ([#5](https://github.com/rdaneel-ali/python-health-monitor/issues/5)).
- Automated CI/CD workflow with GitHub Actions ([#6](https://github.com/rdaneel-ali/python-health-monitor/issues/6)).

### Notes
- Beta pre-release establishing the baseline architecture and CLI behavior.

[Unreleased]: https://github.com/rdaneel-ali/python-health-monitor/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/rdaneel-ali/python-health-monitor/releases/tag/v0.1.0
[0.1.0-beta]: https://github.com/rdaneel-ali/python-health-monitor/releases/tag/v0.1.0-beta
