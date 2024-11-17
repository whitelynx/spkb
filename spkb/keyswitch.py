from solid2 import cube, cylinder, hull, mirror, rotate, up, down, left, right, forward, back, scad_render_to_file
from solid2.core.object_base import OpenSCADObject

from .switch_plate import (
    keyswitch_depth,
    plate_thickness,
)
from .utils import cylinder_outer


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


# To test, use the command line: pipenv run python -m spkb.keyswitch
if __name__ == "__main__":
    print("Rendering mx_keyswitch() to mx_keyswitch.scad...")
    mx_keyswitch().save_as_scad("mx_keyswitch.scad")
