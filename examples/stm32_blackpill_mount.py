from spkb.board_mount import stm32_blackpill

if __name__ == "__main__":
    (
        stm32_blackpill.render(5).color((0.2, 0.2, 0.2))
        + up(20)(
            stm32_blackpill.render(5).color((0.2, 0.2, 0.2))
            + stm32_blackpill.board_profile(5).color((0.0, 0.4, 0.0))
        )
    ).save_as_scad()
