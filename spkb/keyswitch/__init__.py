"""Classes representing different types of keyswitches, able to generate switch plates, backplates, etc.
"""
import sys
from typing_extensions import deprecated

from solid2 import cube, hull
from solid2.core.object_base import OpenSCADObject

if not "-m" in sys.argv:
    from .choc import Choc
    from .mx import MX

    __all__ = [
        "Choc",
        "MX",
        "mx_midline_width", "mx_midline_length", "mx_topline_width", "mx_topline_length", "mx_height_above_plate",
        "mx_keyswitch",
    ]


mx_midline_width = 13.95
mx_midline_length = 15.6
mx_topline_width = 10.5
mx_topline_length = 10.5
mx_height_above_plate = 6.2


@deprecated("Use MX().keyswitch() instead")
def mx_keyswitch() -> OpenSCADObject:
    """Build an simplified approximation of (the top half of) an MX-style keyswitch.
    """
    return hull()(
        cube(mx_midline_width, mx_midline_length, 0.1, center=True).up(3.05),
        cube(mx_topline_width, mx_topline_length, 0.1, center=True).up(mx_height_above_plate + 2.95),
    )
