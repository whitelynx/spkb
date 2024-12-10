from itertools import chain
from math import fabs
from typing import List, Optional, Tuple

from solid2 import cube, hull
from solid2.core.object_base import OpenSCADObject

from ..utils import cylinder_outer

Offset2D = Tuple[float, float]


class Keyswitch:
    """An encapsulation of all measurements and shapes related to a given type of keyswitch.
    """
    keyswitch_length: float = 14.0
    "The length (front to back) of the keyswitch mounting hole"
    keyswitch_width: float = 14.0
    "The width (left to right) of the keyswitch mounting hole"
    keyswitch_depth: float = 5.08
    "From the base of the switch to the mounting plate face"

    plate_thickness: float = 3
    "The thickness of the plate above the origin"
    notch_plate_thickness: float = 1.3
    "The thickness of the plate at the notches where the switch's clips are located"
    notch_width: float = 5
    "The width of the notch for the switch's clips at the deepest part of the notch"
    notch_width_outer: float = 6
    "The width of the notch for the switch's clips at the edge of the mounting hole"
    notch_depth: float = 0.5
    "The depth of the notch for the switch's clips"
    notch_height: float = 3
    "The height of the notch for the switch's clips at the deepest part of the notch"
    notch_height_outer: float = 4
    "The height of the notch for the switch's clips at the edge of the mounting hole"

    wall_thickness: float = 1.5
    "The thickness of the mounting hole walls"

    switch_midline_width: float = 13.95
    "The width (left to right) of the switch at its midline (at the top of the plate)"
    switch_midline_length: float = 15.6
    "The length (front to back) of the switch at its midline (at the top of the plate)"
    switch_topline_width: float = 10.5
    "The width (left to right) of the switch at its top"
    switch_topline_length: float = 10.5
    "The length (front to back) of the switch at its top"
    switch_height_above_plate: float = 6.2
    "The height of the switch body above the top of the plate"

    def plate(
        self,
        full_depth: bool = False,
        extra_depth: float = 0,
        wall_thickness: Optional[float] = None
    ) -> OpenSCADObject:
        """Build a segment of plate for mounting this type of switch.

        :param full_depth: If True, extend the walls of the socket to the full depth of the switch; otherwise, only
        extend to the plate thickness.
        :param extra_depth: Extra depth (`z` height) to add to the walls of the socket.
        :param wall_thickness: The thickness of the walls of the socket.
        """
        if wall_thickness is None:
            wall_thickness = self.wall_thickness

        thickness = (self.keyswitch_depth if full_depth else self.plate_thickness) + extra_depth

        top_wall = (
            cube((self.keyswitch_width + wall_thickness * 2, wall_thickness, thickness), center=True)
            .up(self.plate_thickness - thickness / 2)
            # Notch for switch clips
            - hull()(
                cube((self.notch_width, self.notch_depth * 2, self.notch_height), center=True),
                cube((self.notch_width_outer, self.notch_depth * 2, self.notch_height_outer), center=True)
                .back(self.notch_depth),
            )
            .back(wall_thickness / 2)
            .down(self.notch_plate_thickness + self.notch_height / 2 - self.plate_thickness)
        ).forward((wall_thickness + self.keyswitch_length) / 2)

        left_wall = (
            cube((wall_thickness, self.keyswitch_length + wall_thickness * 2, thickness), center=True)
            .up(self.plate_thickness - thickness / 2)
            .left((wall_thickness + self.keyswitch_width) / 2)
        )

        plate_half = top_wall + left_wall

        return plate_half + plate_half.rotate(180, [0, 0, 1])

    def mounting_socket(
        self,
        extra_depth: float = 0,
    ):
        """Build a socket (negative shape) for mounting this type of switch.

        :param extra_depth: Extra depth (`z` height) to add to the bottom of the walls of the socket.
        """
        # Notch for switch clips
        notch = (
            hull()(
                cube((self.notch_width, self.notch_depth * 2, self.notch_height), center=True),
                cube((self.notch_width_outer, self.notch_depth * 2, self.notch_height_outer), center=True)
                .back(self.notch_depth),
            )
            .down(self.notch_plate_thickness + self.notch_height / 2)
        ).forward(self.keyswitch_length / 2)

        # Extra height above the top of the plate to ensure subtraction doesn't leave stray polygons.
        extra_height = 1

        return (
            cube((self.keyswitch_width, self.keyswitch_length, self.keyswitch_depth + extra_height), center=True)
            .down((self.keyswitch_depth - extra_height) / 2)
            + notch
            + notch.rotate(180, [0, 0, 1])
        )

    def plate_with_board_mount(
        self,
        screw_positions: List[Offset2D],
        screw_radius: float = 0.5,
        extra_depth: float = 0,
        wall_thickness: Optional[float] = None
    ) -> OpenSCADObject:
        """Build a segment of plate for mounting this type of switch, with mounting holes for a single-key PCB.

        :param screw_positions: The positions (`(x, y)` tuples) of the screws for mounting the PCB.
        :param extra_depth: Extra depth (`z` height) to add to the walls of the socket.
        :param wall_thickness: The thickness of the walls of the socket.
        """
        screw_hole = (
            cylinder_outer(r=screw_radius, h=self.keyswitch_depth + self.plate_thickness / 2, center=True)
            .down(self.keyswitch_depth / 2)
        )

        if wall_thickness is None:
            # Find the furthest screw center from the edges of the keyswitch mounting hole.
            max_screw_offset_from_hole = max(
                chain.from_iterable(
                    (fabs(screw_x) - self.keyswitch_width / 2, fabs(screw_y) - self.keyswitch_length / 2)
                    for screw_x, screw_y in screw_positions
                )
            )

            # Add an extra screw_radius outside the screw hole, and use that to determine our wall thickness.
            wall_thickness = max_screw_offset_from_hole + 2 * screw_radius

        plate = self.plate(full_depth=True, wall_thickness=wall_thickness)
        for screw_x, screw_y in screw_positions:
            plate -= screw_hole.right(screw_y).forward(screw_x)

        return plate

    def switch(self) -> OpenSCADObject:
        """Build an simplified approximation of (the top half of) an MX-style keyswitch.
        """
        return hull()(
            cube(self.switch_midline_width, self.switch_midline_length, 0.1, center=True)
            .up(3.05),
            cube(self.switch_topline_width, self.switch_topline_length, 0.1, center=True)
            .up(self.switch_height_above_plate + 2.95),
        )


# To test, use the command line: pipenv run python -m spkb.keyswitch.base
if __name__ == "__main__":
    print("Rendering Keyswitch().mounting_socket() to keyswitch_mounting_socket.scad...")
    Keyswitch().mounting_socket().save_as_scad("keyswitch_mounting_socket.scad")

    print("Rendering Keyswitch().plate_with_board_mount(screw_positions=[(-8, -8), (8, 8)]) to "
          "keyswitch_plate_with_board_mount.scad...")
    Keyswitch().plate_with_board_mount(screw_positions=[(-8, -8), (8, 8)]) \
        .save_as_scad("keyswitch_plate_with_board_mount.scad")

    print("Rendering Keyswitch().switch() to keyswitch_switch.scad...")
    Keyswitch().switch().save_as_scad("keyswitch_switch.scad")
