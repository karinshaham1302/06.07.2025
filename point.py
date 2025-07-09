from typing import override


class Point:
    """
    A class representing a 2D point with private x and y coordinates,
    accessed through properties.
    """

    def __init__(self, x: float, y: float):
        """
        Constructor that receives x and y and stores them as private attributes.
        """
        self.__x = x
        self.__y = y


    @property
    def x(self) -> float:
        """
        Gets the x-coordinate of the point.
        """
        return self.__x

    @x.setter
    def x(self, value: float) -> None:
        """
        Sets the x-coordinate of the point.
        """
        self.__x = value

    @property
    def y(self) -> float:
        """
        Gets the y-coordinate of the point.
        """
        return self.__y

    @y.setter
    def y(self, value: float) -> None:
        """
        Sets the y-coordinate of the point.
        """
        self.__y = value


    @override
    def __repr__(self) -> str:
        """
        Returns a developer-friendly string: Point(x, y)
        """
        return f"Point({self.__x}, {self.__y})"

    @override
    def __str__(self) -> str:
        """
        Returns a user-friendly string: (x, y)
        """
        return f"({self.__x}, {self.__y})"

    @override
    def __eq__(self, other: object) -> bool:
        """
        Compares two Point objects for equality based on x and y values.
        """
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        return False

    @override
    def __hash__(self) -> int:
        """
        Allows using Point objects as dictionary keys by returning a hash based on x and y.
        """
        return hash((self.__x, self.__y))




