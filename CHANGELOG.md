# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]


## [0.1.1] - 2024-12-16

### Added

- This `CHANGELOG.md`
- `scripts/run-module-tests.sh` for running in-module tests
- Continuous integration via GitHub Actions
- `Keyswitch.mounting_socket()` for rendering a negative shape for switch mounting holes
- `Keyswitch.plate_size()` and `Keyswitch.plate_with_board_mount_size()` for getting plate measurements
- `Keyswitch.with_screws()` and `Keyswitch.with_board()` for adding per-key PCBs
- `Keyswitch.screw_hole()`
- `types.HoleDef` and `types.Offset2D`
- `extra_spacing` arg to `spkb.single_key_pcb.single_key_board()`

### Changed

- Changed `spkb.keyswitch` to treat `z == 0` as the top surface of the plate,
  instead of having it protrude above the ground plane.

### Removed

- `Keyswitch.plate_with_board_mount` - use `Keyswitch.with_board().plate()` instead
- `Keyswitch.plate_with_board_mount_size` - use `Keyswitch.with_board().plate_size()` instead

### Deprecated

- `spkb.switch_plate` - use `spkb.keyswitch.Keyswitch` subclasses instead.


## [0.1.0] - 2024-12-09

Initial verion


[Unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/v0.1.1...HEAD
[0.1.1]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.1.1
[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/releases/tag/v0.1.0
