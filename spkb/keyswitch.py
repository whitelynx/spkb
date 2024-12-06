from itertools import chain
from math import fabs
from typing import List, Optional, Tuple

from solid2 import cube, hull, mirror, rotate, scad_render_to_file
from solid2.core.object_base import OpenSCADObject

from .utils import cylinder_outer

Offset2D = Tuple[float, float]


mx_midline_width = 13.95
mx_midline_length = 15.6
mx_topline_width = 10.5
mx_topline_length = 10.5
mx_height_above_plate = 6.2


def mx_keyswitch() -> OpenSCADObject:
    """Build an simplified approximation of (the top half of) an MX-style keyswitch.
    """
    return hull()(
        cube(mx_midline_width, mx_midline_length, 0.1, center=True).up(3.05),
        cube(mx_topline_width, mx_topline_length, 0.1, center=True).up(mx_height_above_plate + 2.95),
    )


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
    notch_height: float = 8
    "The height of the notch for the switch's clips at the deepest part of the notch"
    notch_height_outer: float = 9
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
        wall_thickness: float = None
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

        return plate_half + rotate(180, [0, 0, 1])(plate_half)

    def plate_with_board_mount(
        self,
        screw_positions: List[Offset2D],
        screw_radius: float = 0.5,
        extra_depth: float = 0,
        wall_thickness: float = None
    ) -> OpenSCADObject:
        """Build a segment of plate for mounting this type of switch, with mounting holes for a single-key PCB.

        :param screw_positions: The positions (`(x, y)` tuples) of the screws for mounting the PCB.
        :param extra_depth: Extra depth (`z` height) to add to the walls of the socket.
        :param wall_thickness: The thickness of the walls of the socket.
        """
        screw_hole = down(self.keyswitch_depth / 2)(
            cylinder_outer(r=screw_radius, h=self.keyswitch_depth + self.plate_thickness / 2, center=True)
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
            wall_thickness = max_screw_offset_from_hole + screw_radius

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


class MX(Keyswitch):
    """An encapsulation of all measurements and shapes related to Cherry MX-style switches.
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
    notch_height: float = 8
    "The height of the notch for the switch's clips at the deepest part of the notch"
    notch_height_outer: float = 9
    "The height of the notch for the switch's clips at the edge of the mounting hole"
    backplate_thickness: float = 1.25
    "The thickness of the backplate, for plate methods that use it"

    backplate_clearance_distance: float = 3.5
    "Depth to clear behind the backplate"
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

    def mx_backplate(self) -> OpenSCADObject:
        """Build a backplate for MX-style switches, with Kailh MX hot-swap socket support.

        You can still use this without hot-swap sockets; the holes are left at the larger size to avoid melting when
        soldering directly.
        """
        return (
            cube((self.keyswitch_width + 3, self.keyswitch_length + 3, self.backplate_thickness), center=True)
            # Center post:
            - cylinder_outer(r=1.9939, h=self.backplate_thickness + 1, center=True)
            # Side posts:
            - cylinder_outer(r=0.8509, h=self.backplate_thickness + 1, center=True).right(5.08)
            - cylinder_outer(r=0.8509, h=self.backplate_thickness + 1, center=True).left(5.08)
            # Contacts:
            - cylinder_outer(r=1.5, h=self.backplate_thickness + 1, center=True).forward(2.54).left(3.81)
            - cylinder_outer(r=1.5, h=self.backplate_thickness + 1, center=True).forward(5.08).right(2.54)
            # LEDs (for up to 4-lead through-hole LEDs):
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(5.08).right(1.27)
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(5.08).left(1.27)
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(5.08).right(3.81)
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(5.08).left(3.81)
        ).up(self.plate_thickness - self.keyswitch_depth - self.backplate_thickness / 2)

    def backplate_clearance(self) -> OpenSCADObject:
        """Build a shape to subtract in order to provide clearance around the backplate of the switch.
        """
        z_offset = self.plate_thickness - self.keyswitch_depth - self.backplate_thickness
        return forward(7.5 / 2)(
            up(z_offset - self.backplate_clearance_distance / 2)(
                cube((16.5, 7.5, self.backplate_clearance_distance))
            )
        )

    def plate_with_backplate(self) -> OpenSCADObject:
        """Build a segment of plate for an MX-compatible switch, with a backplate capable of holding a hot-swap socket.
        """
        return self.plate(full_depth=True, extra_depth=1) + self.mx_backplate()


class Choc(Keyswitch):
    """An encapsulation of all measurements and shapes related to Kailh Choc-style switches.
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
    notch_height: float = 8
    "The height of the notch for the switch's clips at the deepest part of the notch"
    notch_height_outer: float = 9
    "The height of the notch for the switch's clips at the edge of the mounting hole"
    backplate_thickness: float = 1.25
    "The thickness of the backplate, for plate methods that use it"

    backplate_clearance_distance: float = 3.5
    "Depth to clear behind the backplate"
    wall_thickness: float = 1.5
    "The thickness of the mounting hole walls"

    switch_midline_width: float = 15
    "The width (left to right) of the switch at its midline (at the top of the plate)"
    switch_midline_length: float = 15
    "The length (front to back) of the switch at its midline (at the top of the plate)"
    switch_topline_width: float = 12.5
    "The width (left to right) of the switch at its top"
    switch_topline_length: float = 12.5
    "The length (front to back) of the switch at its top"
    switch_height_above_plate: float = 3.3
    "The height of the switch body above the top of the plate"

    def choc_backplate(self) -> OpenSCADObject:
        """Build a backplate for Choc-style switches, with Kailh Choc hot-swap socket support.

        You can still use this without hot-swap sockets; the holes are left at the larger size to avoid melting when
        soldering directly.
        """
        return (
            cube((self.keyswitch_width + 3, self.keyswitch_length + 3, self.backplate_thickness), center=True)
            # Center post:
            - cylinder_outer(r=2.5, h=self.backplate_thickness + 1, center=True)
            # Side posts:
            - cylinder_outer(r=0.95, h=self.backplate_thickness + 1, center=True).right(5.5)
            - cylinder_outer(r=0.95, h=self.backplate_thickness + 1, center=True).left(5.5)
            # Corner post:
            - hull()(
                cylinder_outer(r=0.75, h=self.backplate_thickness + 1, center=True).back(0.25),
                cylinder_outer(r=0.75, h=self.backplate_thickness + 1, center=True).forward(0.25),
            ).back(5.15).right(5)
            # Contacts:
            - cylinder_outer(r=1.5, h=self.backplate_thickness + 1, center=True).forward(3.8).left(5)
            - cylinder_outer(r=1.5, h=self.backplate_thickness + 1, center=True).forward(5.9)
            # LEDs (for up to 4-lead through-hole LEDs):
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(4.815).right(1.27)
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(4.815).left(1.27)
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(4.815).right(3.81)
            - cylinder_outer(r=0.4953, h=self.backplate_thickness + 1, center=True).back(4.815).left(3.81)
        ).up(self.plate_thickness - self.keyswitch_depth - self.backplate_thickness / 2)

    def backplate_clearance(self) -> OpenSCADObject:
        """Build a shape to subtract in order to provide clearance around the backplate of the switch.
        """
        z_offset = self.plate_thickness - self.keyswitch_depth - self.backplate_thickness
        return back(-7.5 / 2)(
            up(z_offset - self.backplate_clearance_distance / 2)(
                cube((16.5, 7.5, self.backplate_clearance_distance))
            )
        )

    def plate_with_backplate(self) -> OpenSCADObject:
        """Build a segment of plate for an MX-compatible switch, with a backplate capable of holding a hot-swap socket.
        """
        return self.plate(full_depth=True, extra_depth=1) + self.choc_backplate()


# To test, use the command line: pipenv run python -m spkb.keyswitch
if __name__ == "__main__":
    print("Rendering mx_keyswitch() to mx_keyswitch.scad...")
    mx_keyswitch().save_as_scad("mx_keyswitch.scad")

    print("Rendering Choc().plate_with_backplate() to choc_plate_with_backplate.scad...")
    Choc().plate_with_backplate().save_as_scad("choc_plate_with_backplate.scad")

    print("Rendering MX().plate_with_backplate() to mx_plate_with_backplate.scad...")
    MX().plate_with_backplate().save_as_scad("mx_plate_with_backplate.scad")
