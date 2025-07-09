from math import sqrt
from point import Point


def main():
    p1 = Point(3, 4)
    p2 = Point(3, 4)

    points_dict = {}
    points_dict[p1] = sqrt(p1.x**2 + p1.y**2)

    points_dict[p2] = "Same coordinates as p1"

    print(points_dict)


if __name__ == "__main__":
    main()


