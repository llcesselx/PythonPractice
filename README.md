# Python Programming Exercises #4: Area & Volume
## By: Al Sweigart
You will write four functions for this exercise. The functions `area()` and `perimeter()` have `length` and `width` parameters and the functions `volume()` and `surfaceArea()` have `length`, `width`, and `height` parameters. These functions return the area, perimeter, volume, and surface area respectively.

The formulas for calculating area, perimeter, volume, and surface area are based on the length(L), width(W), and height(H) of the shape:
  <li>area = L * W</li>
  <li>perimeter = L + W + L + W</li>
  <li>volume = L * W * H</li>
  <li>surface area = (L * W * 2) + (L * W * 2) + (L * W * 2)</li>

![area volume](https://github.com/llcesselx/PythonPractice/assets/108751430/b5358af1-a39a-4695-944e-6cb6af28ee4a)


These python `assert` statements stop the program if their condition is `False`. Copy them to the botttom of your solution program. Your solution is correct if the following `assert`statements' conditions are all `True`:

```
    assert area(10, 10)
    assert area(0, 9999) == 0
    assert area(5, 8) == 40
    assert perimeter(10, 10) == 40
    assert perimeter(0, 9999) == 19998
    assert perimeter(5, 8) == 26
    assert volume(10, 10, 10) == 1000
    assert volume(9999, 0, 9999) == 0
    assert volume(5, 8, 10) == 400
    assert surface_area(10, 10, 10) == 600
    assert surface_area(9999, 0, 9999) == 199960002
    assert surface_area(5, 8, 10) == 340
```
