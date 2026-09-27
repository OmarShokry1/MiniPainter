import cv2
import numpy as np

from Rectangle import Rectangle
from Circle import Circle
from Polygon import Polygon

class MiniPainter:
    WINDOW_NAME = "Mini Painter"

    # OpenCV uses BGR, not RGB.
    COLORS = {
        1: ("Red", (0, 0, 255)),
        2: ("Green", (0, 200, 0)),
        3: ("Blue", (255, 0, 0)),
        4: ("Yellow", (0, 255, 255)),
        5: ("White", (255, 255, 255)),
    }

    def __init__(self, width=700, height=500):
        self.width = width
        self.height = height

        # White canvas.
        self.canvas = np.full(
            (self.height, self.width, 3),
            255,
            dtype=np.uint8
        )

        self.mode = "circle"
        self.color_number = 1
        self.color_name = self.COLORS[1][0]
        self.color = self.COLORS[1][1]

    def create_shape(self):
        if self.mode == "circle":
            return Circle(self.color)

        if self.mode == "rectangle":
            return Rectangle(self.color)

        if self.mode == "polygon":
            return Polygon(self.color)

        return Circle(self.color)

    def draw_shape(self, x, y):
        shape = self.create_shape()
        shape.draw(self.canvas, x, y)

    def draw_status(self):
        # Status panel in the top-left corner.
        overlay = self.canvas.copy()

        cv2.rectangle(
            overlay,
            (10, 10),
            (275, 100),
            (245, 245, 245),
            -1
        )

        cv2.addWeighted(overlay, 0.85, self.canvas, 0.15, 0, self.canvas)

        cv2.putText(
            self.canvas,
            f"Mode: {self.mode}",
            (20, 38),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (0, 0, 0),
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            self.canvas,
            f"Color: {self.color_name} ({self.color_number})",
            (20, 65),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 0),
            2,
            cv2.LINE_AA
        )

        cv2.putText(
            self.canvas,
            "C/R/P  1-5  W=Save  Q=Quit",
            (20, 90),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.43,
            (0, 0, 0),
            1,
            cv2.LINE_AA
        )

    def update_color(self, number):
        if number in self.COLORS:
            self.color_number = number
            self.color_name, self.color = self.COLORS[number]

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.draw_shape(x, y)

    def save_canvas(self):
        filename = "mini_painter_output.png"
        cv2.imwrite(filename, self.canvas)
        print(f"Canvas saved as: {filename}")

    def run(self):
        cv2.namedWindow(self.WINDOW_NAME)
        cv2.setMouseCallback(self.WINDOW_NAME, self.mouse_callback)

        print("=== Mini Painter ===")
        print("C = Circle")
        print("R = Rectangle")
        print("P = Polygon")
        print("1-5 = Select color")
        print("W = Save")
        print("Q = Quit")
        print("Left click = Draw selected shape")

        while True:
            display = self.canvas.copy()

            # Draw status only on the displayed copy so it does not become
            # part of the actual drawing canvas.
            old_canvas = self.canvas
            self.canvas = display
            self.draw_status()
            display = self.canvas
            self.canvas = old_canvas

            cv2.imshow(self.WINDOW_NAME, display)

            key = cv2.waitKey(20) & 0xFF

            if key == ord("q"):
                break

            elif key == ord("c"):
                self.mode = "circle"
                print("Mode changed to Circle")

            elif key == ord("r"):
                self.mode = "rectangle"
                print("Mode changed to Rectangle")

            elif key == ord("p"):
                self.mode = "polygon"
                print("Mode changed to Polygon")

            elif ord("1") <= key <= ord("5"):
                self.update_color(key - ord("0"))
                print(f"Color changed to {self.color_name}")

            elif key == ord("w"):
                self.save_canvas()

        cv2.destroyAllWindows()


if __name__ == "__main__":
    painter = MiniPainter()
    painter.run()
