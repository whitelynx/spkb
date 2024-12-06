from collections.abc import Callable, Sequence
from math import pi, cos
from typing import List, Union

from solid2 import cube, cylinder
from solid2.core.object_base import OpenSCADObject


def fudge_radius(r: Union[float, Sequence[float]], segments: int = 16) -> Union[float, List[float]]:
    """Adjust the given radius for the given number of segments to make it generate a circumscribed circular object.

    See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/undersized_circular_objects for more info.

    :param r: The radius of the cylinder, or a sequence containing the radii of the top and bottom ends.
    :param segments: Number of fragments in 360 degrees.
    """
    fudge = 1 / cos(pi / segments)
    return [ri * fudge for ri in r] if isinstance(r, Sequence) else r * fudge


def cylinder_outer(r: Union[float, Sequence[float]], h: float = 1, segments: int = 16, center: bool = False) -> OpenSCADObject:
    """Create a cylinder using circumscribed polygons instead of the default inscribed polygons.

    See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/undersized_circular_objects for more info.

    :param r: The radius of the cylinder, or a sequence containing the radii of the top and bottom ends.
    :param h: This is the height of the cylinder.
    :param segments: Number of fragments in 360 degrees.
    :param center: If True will center the height of the cone/cylinder around
    the origin. Default is False, placing the base of the cylinder or r1 radius
    of cone at the origin.
    """
    adjusted_r = fudge_radius(r, segments)

    radii = {}
    if isinstance(adjusted_r, (int, float)):
        radii['r'] = adjusted_r
    elif isinstance(adjusted_r, (tuple, list)):
        radii['r1'], radii['r2'] = adjusted_r

    return cylinder(
        h=h,
        _fn=segments,
        center=center,
        **radii,
    )


"""Nothing. (a completely empty shape)
"""
nothing = cube((1, 1, 1), center=True) - cube((2, 2, 2), center=True)


def optional(condition: bool) -> Callable[[OpenSCADObject], OpenSCADObject]:
    """Optionally include the wrapped part.

    If `condition` is truthy, the wrapped part will be returned; otherwise, spkb.utils.nothing will be returned.

    :param condition: the condition under which to include the part
    """
    return lambda part: part if condition else nothing
