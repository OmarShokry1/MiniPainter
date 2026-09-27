import cv2
import numpy as np
import math

from Shape import Shape


class Polygon(Shape):
    def __init__(self, color, sides=6, radius=50):
        super().__init__(color)
        self.sides = sides
        self.radius = radius

    def draw(self, canvas, x, y):
        points = []

        for i in range(self.sides):
            angle = (
                2 * math.pi * i / self.sides
                - math.pi / 2
            )

            px = int(x + self.radius * math.cos(angle))
            py = int(y + self.radius * math.sin(angle))

            points.append([px, py])

        points = np.array(points, dtype=np.int32)

        cv2.fillPoly(
            canvas,
            [points],
            self.color
        )