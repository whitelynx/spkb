from typing import Tuple

from solid2 import rotate, cube, up, left, right, forward, back
from solid2.core.object_base import OpenSCADObject

from .switch_plate import (
    switch_plate,
    keyswitch_depth,
    plate_thickness,
    mount_width,
    mount_length,
)


switch_spacing = 2

default_wall_height = keyswitch_depth + 15
wall_length = mount_length + 2 * switch_spacing
wall_thickness = 3


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


def key_grid_tester_wall_dimensions(
    length_units: int, width_units: int, wall_height: float, margin_length: float, margin_width: float
) -> Tuple[float, float]:
    wall_length = (
        (mount_length + switch_spacing) * length_units
        + switch_spacing
        + 2 * margin_length
    )
    wall_width = (
        (mount_width + switch_spacing) * width_units + switch_spacing + 2 * margin_width
    )

    return wall_length, wall_width


def key_grid_tester_walls(
    length_units: int, width_units: int, wall_height: float, margin_length: float, margin_width: float
) -> OpenSCADObject:
    wall_length, wall_width = key_grid_tester_wall_dimensions(
        length_units, width_units, wall_height, margin_length, margin_width
    )

    top_wall = forward((wall_length - wall_thickness) / 2)(
        cube((wall_width, wall_thickness, wall_height), center=True)
    )

    left_wall = left((wall_width - wall_thickness) / 2)(
        cube((wall_thickness, wall_length, wall_height), center=True)
    )

    return up(wall_height / 2)(
        top_wall + left_wall + rotate(180)(top_wall) + rotate(180)(left_wall)
    )


def key_grid_tester(
    length_units: int,
    width_units: int,
    wall_height: float = default_wall_height,
    margin_length: float = 0,
    margin_width: float = 0,
) -> OpenSCADObject:
    x_grid_size = mount_width + switch_spacing
    y_grid_size = mount_length + switch_spacing

    case = key_grid_tester_walls(
        length_units, width_units, wall_height, margin_length, margin_width
    ) + up(wall_height - plate_thickness)(
        right(x_grid_size * (width_units - 1) / 2)(
            back(y_grid_size * (length_units - 1) / 2)(
                *[
                    left(x_grid_size * x_units)(
                        forward(y_grid_size * y_units)(spaced_switch_plate())
                    )
                    for y_units in range(length_units)
                    for x_units in range(width_units)
                ]
            )
        )
    )

    return case
