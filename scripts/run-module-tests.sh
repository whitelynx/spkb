#!/bin/sh

set -e

assert_created() {
	if [ ! -e "$1" ]; then
		echo "Expected file $1 was not created!" >/dev/stderr
		exit 1
	fi
}

poetry run python -m spkb.keycaps
assert_created keycaps.scad

poetry run python -m spkb.single_key_pcb
assert_created single_key_board.scad

poetry run python -m spkb.board_mount
assert_created pro_micro.scad
assert_created stm32_blackpill.scad

poetry run python -m spkb.single_tester
assert_created single_tester.scad

poetry run python -m spkb.keyswitch.choc
assert_created choc_plate_with_backplate.scad

poetry run python -m spkb.keyswitch.mx
assert_created mx_plate_with_backplate.scad

# Deprecated modules
poetry run python -m spkb.switch_plate
assert_created mx_plate.scad
assert_created mx_plate_with_backplate.scad
assert_created mx_plate_with_board_mount.scad

poetry run python -m spkb.keyswitch
assert_created mx_keyswitch.scad
