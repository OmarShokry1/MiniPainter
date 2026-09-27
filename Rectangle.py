import cv2

from Shape import Shape


class Rectangle(Shape):
    def __init__(self, color, width=100, height=60):
        super().__init__(color)
        self.width = width
        self.height = height

    def draw(self, canvas, x, y):
        x1 = x - self.width // 2
        y1 = y - self.height // 2
        x2 = x + self.width // 2
        y2 = y + self.height // 2

        cv2.rectangle(
            canvas,
            (x1, y1),
            (x2, y2),
            self.color,
            self.thickness
        )