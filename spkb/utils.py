from collections.abc import Sequence
from math import pi, cos

from solid2 import cube, cylinder


def fudge_radius(r, segments=16):
    """Adjust the given radius for the given number of segments to make it generate a circumscribed circular object.

    See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/undersized_circular_objects for more info.

    :param r: The radius of both top and bottom ends of the cylinder. Use this
    parameter if you want plain cylinder. Default value is 1.
    :type r: number

    :param segments: Number of fragments in 360 degrees.
    :type segments: int
    """
    fudge = 1 / cos(pi / segments)
    return [ri * fudge for ri in r] if isinstance(r, Sequence) else r * fudge


def cylinder_outer(r, h, segments=16, center=False):
    """Create a cylinder using circumscribed polygons instead of the default inscribed polygons.

    See https://en.wikibooks.org/wiki/OpenSCAD_User_Manual/undersized_circular_objects for more info.

    :param r: The radius of both top and bottom ends of the cylinder. Use this
    parameter if you want plain cylinder. Default value is 1.
    :type r: number

    :param h: This is the height of the cylinder. Default value is 1.
    :type h: number

    :param segments: Number of fragments in 360 degrees.
    :type segments: int

    :param center: If True will center the height of the cone/cylinder around
    the origin. Default is False, placing the base of the cylinder or r1 radius
    of cone at the origin.
    :type center: boolean
    """
    adjusted_r = fudge_radius(r, segments)

    return cylinder(h=h, r=adjusted_r, _fn=segments, center=center)


"""Nothing. (a completely empty shape)
"""
nothing = cube((1, 1, 1), center=True) - cube((2, 2, 2), center=True)


def optional(condition):
    """Optionally include the wrapped part.

    If `condition` is truthy, the wrapped part will be returned; otherwise, spkb.utils.nothing will be returned.

    :param condition: the condition under which to include the part
    :type condition: bool
    """
    return lambda part: part if condition else nothing
