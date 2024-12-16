"""Build an approximation of a single-key PCB.

<span class="todo">TODO: Enapsulate and document this better.</span>
"""
from solid2 import cube, hull
from solid2.core.object_base import OpenSCADObject

from .switch_plate import (
    keyswitch_depth,
    plate_thickness,
)
from .utils import cylinder_outer


pcb_thickness = 1.57
pcb_size = 19
pcb_corner_radius = 1.25
pcb_corner_offset = pcb_size / 2 - pcb_corner_radius
pcb_hole_radius = 1.7 / 2
pcb_hole_offset = 8


def single_key_board(simple: bool = False) -> OpenSCADObject:
    """Build an approximation of a single-key PCB.

    If `simple=True`, then just approximate the size of one of these with a rectangular prism.

    Some compatible single-key PCBs:
    - https://www.flux.ai/whitelynx/mx-single-keyswitch-hot-swap-board
    - https://www.flux.ai/whitelynx/choc-single-keyswitch-hot-swap-board
    """
    if simple:
        pcb = cube((pcb_size, pcb_size, pcb_thickness), center=True)
    else:
        pcb_corner = cylinder_outer(r=pcb_corner_radius, h=pcb_thickness, center=True)
        pcb_hole = cylinder_outer(r=pcb_hole_radius, h=pcb_thickness * 2, center=True)

        pcb = (
            hull()(
                pcb_corner.left(pcb_corner_offset).forward(pcb_corner_offset),
                pcb_corner.left(pcb_corner_offset).back(pcb_corner_offset),
                pcb_corner.right(pcb_corner_offset).forward(pcb_corner_offset),
                pcb_corner.right(pcb_corner_offset).back(pcb_corner_offset),
            )
            - pcb_hole.left(pcb_hole_offset).forward(pcb_hole_offset)
            - pcb_hole.left(pcb_hole_offset).back(pcb_hole_offset)
            - pcb_hole.right(pcb_hole_offset).forward(pcb_hole_offset)
            - pcb_hole.right(pcb_hole_offset).back(pcb_hole_offset)
        )

    return pcb.down(pcb_thickness / 2 + keyswitch_depth)


# To test, use the command line: pipenv run python -m spkb.single_key_pcb
if __name__ == "__main__":
    print("Rendering single_key_board() to single_key_board.scad...")
    single_key_board().save_as_scad("single_key_board.scad")
