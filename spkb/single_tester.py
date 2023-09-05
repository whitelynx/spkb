from solid2 import cube, rotate, up, forward, scad_render_to_file

from .switch_plate import (
    switch_plate,
    keyswitch_depth,
    plate_thickness,
    mount_width,
    mount_height,
)


SEGMENTS = 48

switch_spacing = 10

wall_height = keyswitch_depth + 15
wall_length = max(mount_width, mount_height) + 2 * switch_spacing
wall_thickness = 5


def spaced_switch_plate():
    plate_spacer = up(plate_thickness / 2)(
        forward((max(mount_width, mount_height) + switch_spacing) / 2)(
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


def single_tester_walls():
    wall = up(wall_height / 2)(
        forward((wall_length - wall_thickness) / 2)(
            cube((wall_length, wall_thickness, wall_height), center=True)
        )
    )

    return wall + rotate(90)(wall) + rotate(180)(wall) + rotate(270)(wall)


def single_tester():
    return single_tester_walls() + up(wall_height - plate_thickness)(
        spaced_switch_plate()
    )


if __name__ == "__main__":
    scad_render_to_file(
        single_tester(), file_header=f"$fn = {SEGMENTS};", include_orig_code=True
    )
