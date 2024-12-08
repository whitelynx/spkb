from solid2 import cube
from solid2.core.object_base import OpenSCADObject

from ..utils import cylinder_outer
from .base import Keyswitch


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

        See page 10 of https://www.kailhswitch.com/Content/upload/pdf/201815927/PaleBlueSpeed.pdf?rnd=782 for standard
        switch layout, and https://www.kailhswitch.com/Content/upload/pdf/202215927/CPG151101S11-16.pdf?rnd=494 for
        hot-swap socket dimensions.
        """
        return (
            cube((self.keyswitch_width + 3, self.keyswitch_length + 3, self.backplate_thickness), center=True)
            # Center post:
            - cylinder_outer(r=1.995, h=self.backplate_thickness + 1, center=True)
            # Side posts:
            - cylinder_outer(r=0.85, h=self.backplate_thickness + 1, center=True).right(5.08)
            - cylinder_outer(r=0.85, h=self.backplate_thickness + 1, center=True).left(5.08)
            # Contacts:
            - cylinder_outer(r=1.5, h=self.backplate_thickness + 1, center=True).forward(2.54).left(3.81)
            - cylinder_outer(r=1.5, h=self.backplate_thickness + 1, center=True).forward(5.08).right(2.54)
            # LEDs (for up to 4-lead through-hole LEDs):
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(5.08).right(1.27)
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(5.08).left(1.27)
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(5.08).right(3.81)
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(5.08).left(3.81)
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


# To test, use the command line: pipenv run python -m spkb.keyswitch.mx
if __name__ == "__main__":
    print("Rendering MX().plate_with_backplate() to mx_plate_with_backplate.scad...")
    MX().plate_with_backplate().save_as_scad("mx_plate_with_backplate.scad")
