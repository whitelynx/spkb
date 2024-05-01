from solid2 import cube, cylinder, hull, mirror, rotate, up, down, left, right, forward, back, scad_render_to_file


SEGMENTS = 48

keyswitch_length = 14.0
keyswitch_width = 14.0
keyswitch_depth = 5.08  # From the base of the switch to the mounting plate face

plate_thickness = 3
notch_plate_thickness = 1.3  # The thickness of the plate at the notches where the switch's clips are located
notch_width = 5
notch_width_outer = 6
notch_depth = 0.5
notch_height = 8
notch_height_outer = 9
backplate_thickness = 1.25
backplate_orientation = 180
mount_width = keyswitch_width + 3
mount_length = keyswitch_length + 3

cherry_backplate_clearance_distance = 3.5


def mx_plate(full_depth=False, extra_depth=0, wall_thickness=1.5):
    """Build a segment of plate for an MX-compatible switch.
    """
    thickness = (keyswitch_depth if full_depth else plate_thickness) + extra_depth
    top_wall = forward((wall_thickness + keyswitch_length) / 2)(
        up(plate_thickness - thickness / 2)(
            cube((keyswitch_width + wall_thickness * 2, wall_thickness, thickness), center=True)
        )
        - down(notch_plate_thickness + notch_height / 2 - plate_thickness)(  # Notch for switch clips
            back(wall_thickness / 2)(
                hull()(
                    cube((notch_width, notch_depth * 2, notch_height), center=True),
                    back(notch_depth)(
                        cube((notch_width_outer, notch_depth * 2, notch_height_outer), center=True)
                    )
                )
            )
        )
    )

    left_wall = left((wall_thickness + keyswitch_width) / 2)(
        up(plate_thickness - thickness / 2)(
            cube((wall_thickness, keyswitch_length + wall_thickness * 2, thickness), center=True)
        )
    )

    plate_half = top_wall + left_wall

    return plate_half + mirror((0, 1, 0))(mirror((1, 0, 0))(plate_half))


def mx_plate_with_board_mount(full_depth=False, extra_depth=0):
    """Build a segment of plate for an MX-compatible switch, with mounting holes for a single-key PCB.

    Some compatible single-key PCBs:
    - https://www.flux.ai/whitelynx/mx-single-keyswitch-hot-swap-board
    """
    screw_hole = down(keyswitch_depth / 2)(
        cylinder(r=0.5, h=keyswitch_depth + plate_thickness / 2, center=True, _fn=16)
    )

    return (
        mx_plate(full_depth=True, wall_thickness=2.625)
        - forward(8)(right(8)(screw_hole))
        - forward(8)(left(8)(screw_hole))
        - back(8)(right(8)(screw_hole))
        - back(8)(left(8)(screw_hole))
    )


def mx_backplate():
    return up(plate_thickness - keyswitch_depth - backplate_thickness / 2)(
        rotate(backplate_orientation, [0, 0, 1])(
            cube((keyswitch_width + 3, keyswitch_length + 3, backplate_thickness), center=True)
            - cylinder(r=1.9939, h=backplate_thickness + 1, center=True, _fn=16)
            - right(5.08)(cylinder(r=0.8509, h=backplate_thickness + 1, center=True, _fn=16))
            - left(5.08)(cylinder(r=0.8509, h=backplate_thickness + 1, center=True, _fn=16))
            - left(3.81)(forward(2.54)(cylinder(r=1.5, h=backplate_thickness + 1, center=True, _fn=16)))
            - right(2.54)(forward(5.08)(cylinder(r=1.5, h=backplate_thickness + 1, center=True, _fn=16)))
            - right(1.27)(back(5.08)(cylinder(r=0.4953, h=backplate_thickness + 1, center=True, _fn=16)))
            - left(1.27)(back(5.08)(cylinder(r=0.4953, h=backplate_thickness + 1, center=True, _fn=16)))
            - right(3.81)(back(5.08)(cylinder(r=0.4953, h=backplate_thickness + 1, center=True, _fn=16)))
            - left(3.81)(back(5.08)(cylinder(r=0.4953, h=backplate_thickness + 1, center=True, _fn=16)))
        )
    )


def mx_backplate_clearance():
    return back(-7.5 / 2)(
        up(plate_thickness - keyswitch_depth - backplate_thickness - cherry_backplate_clearance_distance / 2)(
            rotate(backplate_orientation, [0, 0, 1])(
                cube((16.5, 7.5, cherry_backplate_clearance_distance))
            )
        )
    )


def mx_plate_with_backplate():
    """Build a segment of plate for an MX-compatible switch, with a backplate capable of holding a hot-swap socket.
    """
    return mx_plate(full_depth=True, extra_depth=1) + mx_backplate()


switch_plate = mx_plate


# To test, use the command line: pipenv run python -m spkb.switch_plate
if __name__ == "__main__":
    print("Rendering mx_plate() to mx_plate.scad...")
    scad_render_to_file(
        mx_plate(), filename="mx_plate.scad", file_header=f"$fn = {SEGMENTS};"
    )

    print("Rendering mx_plate_with_backplate() to mx_plate_with_backplate.scad...")
    scad_render_to_file(
        mx_plate_with_backplate(), filename="mx_plate_with_backplate.scad", file_header=f"$fn = {SEGMENTS};"
    )

    print("Rendering mx_plate_with_board_mount() to mx_plate_with_board_mount.scad...")
    scad_render_to_file(
        mx_plate_with_board_mount(), filename="mx_plate_with_board_mount.scad", file_header=f"$fn = {SEGMENTS};"
    )
