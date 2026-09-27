import cv2

from Shape import Shape


class Circle(Shape):
    def __init__(self, color, radius=40):
        super().__init__(color)
        self.radius = radius

    def draw(self, canvas, x, y):
        cv2.circle(
            canvas,
            (x, y),
            self.radius,
            self.color,
            self.thickness
        )