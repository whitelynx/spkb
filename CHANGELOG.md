# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added

- This `CHANGELOG.md`
- `scripts/run-module-tests.sh` for running in-module tests
- Continuous integration via GitHub Actions
- `Keyswitch.mounting_socket()` for rendering a negative shape for switch mounting holes

### Changed

- Changed `spkb.keysitch` to treat `z == 0` as the top surface of the plate,
  instead of having it protrude above the ground plane.


## [0.1.0] - 2024-12-09

Initial verion


[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.1.0
