from typing import Tuple


class HoleDef:
    def __init__(self, x: float, y: float, radius: float):
        self.x = x
        "The X position (left to right) of this hole"
        self.y = y
        "The Y position (front to back) of this hole"
        self.radius = radius
        "The radius of this hole"

    def __iter__(self):
        """Unpack the X and Y position of this hole.
        """
        return iter((self.x, self.y))


class Offset2D:
    def __init__(self, x: float, y: float):
        self.x = x
        "The X position (left to right)"
        self.y = y
        "The Y position (front to back)"

    def __iter__(self):
        """Unpack the X and Y position of this `Offset2D`.
        """
        return iter((self.x, self.y))


__all__ = ["HoleDef", "Offset2D"]
