# Mini Painter

An object-oriented Mini Painter application built with Python and OpenCV.

## Features
- Draw circles, rectangles, and polygons.
- Select shapes and colors using the keyboard.
- Draw with a left mouse click.
- Save the current canvas as an image.
- Display the current drawing mode and color.

## Controls
| Key | Action |
|---|---|
| C | Circle |
| R | Rectangle |
| P | Polygon |
| 1 | Red |
| 2 | Green |
| 3 | Blue |
| 4 | Yellow |
| 5 | White |
| W | Save canvas |
| Q | Quit |
| Left Click | Draw selected shape |

## Project Structure
```text
MiniPainter/
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
├── shapes/
│   ├── __init__.py
│   ├── shape.py
│   ├── circle.py
│   ├── rectangle.py
│   └── polygon.py
└── painter/
    ├── __init__.py
    └── mini_painter.py
```

## OOP Design
`Shape` is the base class. `Circle`, `Rectangle`, and `Polygon` inherit from it and implement `draw()`.

The `MiniPainter` class manages the application state, canvas, input, colors, and saving. Polymorphism is used through the common `Shape.draw()` interface.

## Installation
```powershell
python -m pip install -r requirements.txt
```

## Run
```powershell
python main.py
```
