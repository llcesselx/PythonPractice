def main():
    assert get_area(10, 10)
    assert get_area(0, 9999) == 0
    assert get_area(5, 8) == 40
    assert get_perimeter(10, 10) == 40
    assert get_perimeter(0, 9999) == 19998
    assert get_perimeter(5, 8) == 26
    assert get_volume(10, 10, 10) == 1000
    assert get_volume(9999, 0, 9999) == 0
    assert get_volume(5, 8, 10) == 400
    assert get_surface_area(10, 10, 10) == 600
    assert get_surface_area(9999, 0, 9999) == 199960002
    assert get_surface_area(5, 8, 10) == 340

    return 0


def get_area(length, width):
    return length * width


def get_perimeter(length, width):
    return length + length + width + width


def get_volume(length, width, height):
    return length * width * height


def get_surface_area(length, width, height):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)


if __name__ == "__main__":
    main()