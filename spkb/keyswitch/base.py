from itertools import chain
from math import fabs
from typing import List, Optional

from solid2 import cube, hull
from solid2.core.object_base import OpenSCADObject

from ..types import HoleDef, Offset2D
from ..utils import cylinder_outer


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

    with_backplate: bool = False
    "Whether to render a backplate (True) or not when rendering the mounting hole shape"
    backplate_holes: List[HoleDef] = []
    "The positions and radii of any holes in the backplate (for positioning posts, contacts, LED leads, etc.)"

    screws: Optional[List[HoleDef]] = None
    "The positions and radii of any mounting screw holes on the bottom of the switch mount"

    def __init__(self, with_backplate=False):
        self.with_backplate = with_backplate

    @classmethod
    def with_screws(cls, *screws: List[HoleDef]):
        """Return a copy of this `Keyswitch` with the given screw holes.

        :param screws: The positions and radii of any mounting screw holes on the bottom of the switch mount.
        """
        keyswitch = cls()
        keyswitch.screws = screws
        return keyswitch

    def plate_size(
        self,
        wall_thickness: Optional[float] = None,
    ) -> Offset2D:
        """Get the dimensions of a `Keyswitch.plate` shape.

        :param wall_thickness: The thickness of the walls of the socket. Omit to calculate from the defined wall
        thickness and screw hole definitions.
        """
        if wall_thickness is None:
            wall_thickness = self._calc_wall_thickness()

        return Offset2D(self.keyswitch_width + wall_thickness * 2, self.keyswitch_length + wall_thickness * 2)

    def _calc_wall_thickness(self) -> float:
        """Calculate the effective `wall_thickness` for this `Keyswitch` definition.
        """
        if self.screws is None:
            # No screws are defined; use the defined self.wall_thickness.
            return self.wall_thickness

        # Find the furthest screw hole edge from from the edges of the keyswitch mounting hole.
        max_screw_offset_from_hole = max(
            chain.from_iterable(
                (
                    fabs(screw_def.x) - self.keyswitch_width / 2 + screw_def.radius,
                    fabs(screw_def.y) - self.keyswitch_length / 2 + screw_def.radius,
                )
                for screw_def in self.screws
            )
        )

        # Add self.wall_thickness outside the screw hole, and use that to determine our effective wall thickness.
        return max_screw_offset_from_hole + self.wall_thickness

    def plate(
        self,
        full_depth: Optional[bool] = None,
        extra_depth: float = 0,
        wall_thickness: Optional[float] = None
    ) -> OpenSCADObject:
        """Build a segment of plate for mounting this type of switch.

        :param full_depth: If True, extend the walls of the socket to the full depth of the switch; otherwise, only
        extend to the plate thickness. If `self.screws` is set, defaults to full depth.
        :param extra_depth: Extra depth (`z` height) to add to the walls of the socket.
        :param wall_thickness: The thickness of the walls of the socket.
        """
        if wall_thickness is None:
            wall_thickness = self.wall_thickness

        if full_depth is None:
            full_depth = self.screws is not None

        thickness = (self.keyswitch_depth if full_depth else self.plate_thickness) + extra_depth

        plate = cube(
            tuple(self.plate_size(wall_thickness)) + (thickness, ),
            center=True,
        ).down(thickness / 2)

        plate -= self.mounting_socket(extra_depth=extra_depth + 1)

        if self.screws is not None:
            for screw in self.screws:
                plate -= self.screw_hole(screw)

        return plate

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
            ).down(self.notch_plate_thickness + self.notch_height / 2)
        ).forward(self.keyswitch_length / 2)

        # Extra height above the top of the plate to ensure subtraction doesn't leave stray polygons.
        extra_height = 1

        return (
            cube(
                (self.keyswitch_width, self.keyswitch_length, self.keyswitch_depth + extra_height + extra_depth),
                center=True
            ).down((self.keyswitch_depth - extra_height) / 2)
            + notch
            + notch.rotate(180, [0, 0, 1])
        )

    def screw_hole(self, screw: HoleDef):
        """Build a screw hole (negative shape) for the given hole definition.
        """
        return (
            cylinder_outer(r=screw.radius, h=self.keyswitch_depth + self.plate_thickness / 2, center=True)
            .forward(screw.x)
            .right(screw.y)
            .down(self.keyswitch_depth / 2 + self.plate_thickness)
        )

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

    print("Rendering Keyswitch.with_screws(HoleDef(-8, -8, 0.5), HoleDef(8, 8, 0.5)).plate() to "
          "keyswitch_plate_with_board_mount.scad...")
    Keyswitch.with_screws(HoleDef(-8, -8, 0.5), HoleDef(8, 8, 0.5)).plate() \
        .save_as_scad("keyswitch_plate_with_board_mount.scad")

    print("Rendering Keyswitch().switch() to keyswitch_switch.scad...")
    Keyswitch().switch().save_as_scad("keyswitch_switch.scad")
