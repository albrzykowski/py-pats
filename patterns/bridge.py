# Based on: https://proudtobeanengineer.blogspot.com/2012/07/wzorce-projektowe-bridge.html

from abc import ABC, abstractmethod
import math


class Norm(ABC):
    @abstractmethod
    def compute(self, vector):
        pass


class EuclideanNorm(Norm):
    def compute(self, vector):
        return math.sqrt(sum(x * x for x in vector))


class ManhattanNorm(Norm):
    def compute(self, vector):
        return sum(abs(x) for x in vector)


class Vector(ABC):
    def __init__(self, norm: Norm):
        self.norm = norm

    @abstractmethod
    def get_components(self):
        pass

    def length(self):
        return self.norm.compute(self.get_components())


class Vector2D(Vector):
    def __init__(self, x, y, norm: Norm):
        super().__init__(norm)
        self.x = x
        self.y = y

    def get_components(self):
        return [self.x, self.y]


class Vector3D(Vector):
    def __init__(self, x, y, z, norm: Norm):
        super().__init__(norm)
        self.x = x
        self.y = y
        self.z = z

    def get_components(self):
        return [self.x, self.y, self.z]


if __name__ == "__main__":
    euclidean = EuclideanNorm()
    manhattan = ManhattanNorm()

    v2 = Vector2D(3, 4, euclidean)
    v3 = Vector3D(1, 2, 3, manhattan)

    print("Vector2D (Euclidean):", v2.length())   # 5.0
    print("Vector3D (Manhattan):", v3.length())   # 6

    # swap implementation at runtime
    v2.norm = manhattan
    print("Vector2D (Manhattan):", v2.length())   # 7