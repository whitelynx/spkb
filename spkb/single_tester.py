"""Renders a single-switch tester.

<span class="todo">TODO: Document or remove this module.</span>
"""
from solid2 import cube, rotate, up, forward
from solid2.core.object_base import OpenSCADObject

from .switch_plate import (
    switch_plate,
    keyswitch_depth,
    plate_thickness,
    mount_width,
    mount_length,
)


switch_spacing = 10

wall_height = keyswitch_depth + 15
wall_length = max(mount_width, mount_length) + 2 * switch_spacing
wall_thickness = 5


def spaced_switch_plate() -> OpenSCADObject:
    plate_spacer = up(plate_thickness / 2)(
        forward((max(mount_width, mount_length) + switch_spacing) / 2)(
            cube((wall_length, switch_spacing, plate_thickness), center=True)
        )
    )

    return (
        switch_plate()
        + plate_spacer
        + rotate(90)(plate_spacer)
        + rotate(180)(plate_spacer)
        + rotate(270)(plate_spacer)
    )


def single_tester_walls() -> OpenSCADObject:
    wall = up(wall_height / 2)(
        forward((wall_length - wall_thickness) / 2)(
            cube((wall_length, wall_thickness, wall_height), center=True)
        )
    )

    return wall + rotate(90)(wall) + rotate(180)(wall) + rotate(270)(wall)


def single_tester() -> OpenSCADObject:
    return single_tester_walls() + up(wall_height - plate_thickness)(
        spaced_switch_plate()
    )


# To test, use the command line: pipenv run python -m spkb.single_tester
if __name__ == "__main__":
    print("Rendering single_tester() to single_tester.scad...")
    single_tester().save_as_scad("single_tester.scad")
