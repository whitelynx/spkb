#!/bin/sh

set -e

assert_created() {
	if [ ! -e "$1" ]; then
		echo "Expected file $1 was not created!" >/dev/stderr
		exit 1
	fi
}

pipenv run python -m spkb.keycaps
assert_created keycaps.scad

pipenv run python -m spkb.single_key_pcb
assert_created single_key_board.scad

pipenv run python -m spkb.single_tester
assert_created single_tester.scad

pipenv run python -m spkb.keyswitch.choc
assert_created choc_plate_with_backplate.scad

pipenv run python -m spkb.keyswitch.mx
assert_created mx_plate_with_backplate.scad

# Deprecated modules
pipenv run python -m spkb.switch_plate
assert_created mx_plate.scad
assert_created mx_plate_with_backplate.scad
assert_created mx_plate_with_board_mount.scad

pipenv run python -m spkb.keyswitch
assert_created mx_keyswitch.scad
