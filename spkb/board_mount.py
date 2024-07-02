from solid2 import rotate, cube, hull, scad_render_to_file, up, left, right, forward, back

from .utils import cylinder_outer, optional


SEGMENTS = 48

FUDGE = 0.2

m2_head_radius = 5 / 2
m2_shaft_radius = 2 / 2
m2_nut_radius = 3.9 / 2

mount_post_m2_radius = 6 / 2


def mount_post_m2(height):
    return (
        cylinder_outer(mount_post_m2_radius, height)
        - cylinder_outer(m2_shaft_radius, height + 0.1).down(0.05)
    )


class BoardMount:
    def __init__(self, board_width, board_length, board_thickness, has_connector=True, front_mounting_post_separation=10, back_mounting_post_separation=None):
        self.board_width = board_width
        self.board_length = board_length
        self.board_thickness = board_thickness
        self.has_connector = has_connector

        self.front_mounting_post_separation = front_mounting_post_separation
        self.back_mounting_post_separation = back_mounting_post_separation

        # Distance from the front edge of the board to the front of the large portion of the plug
        self.plug_offset = 2

        # Length of the plug clearance volume
        self.plug_length = 20

    def pcb_only(self, distance_from_surface):
        return up(distance_from_surface + self.board_thickness / 2)(
            back(self.board_length / 2)(
                cube(
                    (self.board_width, self.board_length, self.board_thickness),
                    center=True,
                )
            )
        )

    def connector(self, distance_from_surface):
        """An approximation of a USB-C connector.
        """
        return optional(self.has_connector)(
            up(distance_from_surface - 1.25)(
                forward(self.plug_offset + 0.01)(
                    rotate((90, 0, 0))(
                        hull()(
                            left(4 - 1.25)(cylinder_outer(2.5 / 2, 6.02)),
                            right(4 - 1.25)(cylinder_outer(2.5 / 2, 6.02)),
                        )
                    )
                )
                + forward(self.plug_offset + self.plug_length)(
                    rotate((90, 0, 0))(
                        hull()(
                            left(4 - 1.25)(cylinder_outer(8.5 / 2, self.plug_length)),
                            right(4 - 1.25)(cylinder_outer(8.5 / 2, self.plug_length)),
                        )
                    )
                )
            )
        )

    def board_profile(self, distance_from_surface):
        return (
            self.pcb_only(distance_from_surface)
            + self.connector(distance_from_surface)
        )
        # TODO: Maybe add pin clearance!

    def back_mounting_posts(self, distance_from_surface):
        mounting_post = mount_post_m2(distance_from_surface)

        if self.back_mounting_post_separation is not None:
            mounting_post_shift = mount_post_m2_radius + self.back_mounting_post_separation / 2

        return back(self.board_length + m2_shaft_radius + FUDGE)(
            mount_post_m2(distance_from_surface)
            if self.back_mounting_post_separation is None else (
                mount_post_m2(distance_from_surface).left(mounting_post_shift)
                + mount_post_m2(distance_from_surface).right(mounting_post_shift)
            )
        )

    def front_mounting_posts(self, distance_from_surface):
        positioning_post_height = distance_from_surface + self.board_thickness + 3
        positioning_post = cube((4, 4, positioning_post_height), center=True) \
            .up(positioning_post_height / 2) \
            .forward(1)

        positioning_post_shift = 2 + self.front_mounting_post_separation / 2

        return (
            left(positioning_post_shift)(positioning_post)
            + right(positioning_post_shift)(positioning_post)
        ) - self.board_profile(distance_from_surface)

    def mounting_posts(self, distance_from_surface):
        return (
            self.back_mounting_posts(distance_from_surface)
            + self.front_mounting_posts(distance_from_surface)
        )

    def render(self, distance_from_surface):
        return self.mounting_posts(distance_from_surface) - self.board_profile(
            distance_from_surface
        )


pro_micro = BoardMount(18.3, 33.1, 1.7)
stm32_blackpill = BoardMount(20.66, 53, 1.64, back_mounting_post_separation=11)
