from solid2 import cube, hull
from solid2.core.object_base import OpenSCADObject

from ..utils import cylinder_outer
from .base import Keyswitch


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

        See https://www.kailhswitch.com/Content/upload/pdf/201915927/CPG135001D03-3_choc-Navy.pdf?rnd=565 for standard
        switch layout, and https://www.kailhswitch.com/Content/upload/pdf/202115927/CPG135001S30-data-sheet.pdf?rnd=903
        for hot-swap socket dimensions.
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
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(4.815).right(1.27)
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(4.815).left(1.27)
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(4.815).right(3.81)
            - cylinder_outer(r=0.5, h=self.backplate_thickness + 1, center=True).back(4.815).left(3.81)
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


# To test, use the command line: pipenv run python -m spkb.keyswitch.choc
if __name__ == "__main__":
    print("Rendering Choc().plate_with_backplate() to choc_plate_with_backplate.scad...")
    Choc().plate_with_backplate().save_as_scad("choc_plate_with_backplate.scad")
