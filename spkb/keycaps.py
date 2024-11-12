from solid2 import polygon, hull

from spkb.switch_plate import plate_thickness


sa_length = 18.25
sa_1_5_length = 28
sa_double_length = 37.5
sa_mid_shrink = 0.625
sa_top_shrink = 3.125


def sa_cap(units):
    """Create an "SA" keycap shape.

    (actually something akin to SA row 3, but with flat tops)

    :param units: the size of the key, in key units
    :type units: number
    """
    if units == 1:
        bl2 = sa_length / 2
        ml2 = sa_length / 2 - sa_mid_shrink
        tl2 = sa_length / 2 - sa_top_shrink
        key_cap = hull()(
            polygon(((bl2, bl2), (bl2, -bl2), (-bl2, -bl2), (-bl2, bl2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 0.05)),
            polygon(((ml2, ml2), (ml2, -ml2), (-ml2, -ml2), (-ml2, ml2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 6)),
            polygon(((tl2, tl2), (tl2, -tl2), (-tl2, -tl2), (-tl2, tl2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 12)),
        )
        return (
            key_cap
            .translate((0, 0, 5 + plate_thickness))
            .color((220/255, 163/255, 163/255, 1))
        )

    elif units == 2:
        bl2 = sa_double_length / 2
        bw2 = sa_length / 2
        ml2 = sa_double_length / 2 - sa_mid_shrink
        mw2 = sa_length / 2 - sa_mid_shrink
        tl2 = sa_double_length / 2 - sa_top_shrink
        tw2 = sa_length / 2 - sa_top_shrink
        key_cap = hull()(
            polygon(((bw2, bl2), (bw2, -bl2), (-bw2, -bl2), (-bw2, bl2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 0.05)),
            polygon(((mw2, ml2), (mw2, -ml2), (-mw2, -ml2), (-mw2, ml2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 6)),
            polygon(((tw2, tl2), (tw2, -tl2), (-tw2, -tl2), (-tw2, tl2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 12)),
        )
        return (
            key_cap
            .translate((0, 0, 5 + plate_thickness))
            .color((127/255, 159/255, 127/255, 1))
        )

    elif units == 1.5:
        bl2 = sa_1_5_length / 2
        bw2 = sa_length / 2
        ml2 = sa_1_5_length / 2 - sa_mid_shrink
        mw2 = sa_length / 2 - sa_mid_shrink
        tl2 = sa_1_5_length / 2 - sa_top_shrink
        tw2 = sa_length / 2 - sa_top_shrink
        key_cap = hull()(
            polygon(((bw2, bl2), (bw2, -bl2), (-bw2, -bl2), (-bw2, bl2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 0.05)),
            polygon(((mw2, ml2), (mw2, -ml2), (-mw2, -ml2), (-mw2, ml2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 6)),
            polygon(((tw2, tl2), (tw2, -tl2), (-tw2, -tl2), (-tw2, tl2)))
            .linear_extrude(height=0.1, twist=0, convexity=0)
            .translate((0, 0, 12)),
        )
        return (
            key_cap
            .translate((0, 0, 5 + plate_thickness))
            .color((240/255, 223/255, 175/255, 1))
        )

    else:
        raise ValueError(f"Unrecognized key size: {units} units")


if __name__ == "__main__":
    (
        sa_cap(1).translate((-30, 0, 0))
        + sa_cap(1.5)
        + sa_cap(2).translate((30, 0, 0))
    ).save_as_scad()
