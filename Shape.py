class Shape:
    """Base class for drawable shapes."""

    def __init__(self, color, thickness=-1):
        self.color = color
        self.thickness = thickness

    def draw(self, canvas, x, y):
        raise NotImplementedError