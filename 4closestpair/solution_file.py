import math
import sys


class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def get_dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return f"{self.x, self.y}"


def closest_points(all_points):
    # list sorted by x values
    p_x = sorted(all_points, key=lambda p: p.x)

    # list sorted by y values
    p_y = sorted(all_points, key=lambda p: p.y)

    return closest(p_x, p_y, len(all_points))


def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]


def closest(p_x, p_y, n):
    l_x, r_x = split_list(p_x)
    l_y, r_y = split_list(p_y)

    if n >= 4:
        d_1 = closest(r_x, r_y, n/2)
        d_2 = closest(l_x, l_y, n/2)
        delta = min(d_1, d_2)
        streck = r_y[0].y
        s_y = [point for point in p_y if abs(point.y - streck) < delta]
        for i in range(len(s_y)):
            for j in range(i + 1, len(s_y)):
                dist = s_y[i].get_dist(s_y[j])
                if dist < delta:
                    delta = dist
        return delta
    # Fuck it we hardcoding
    else:
        small_path = -1
        for i in range(len(p_x)):
            for j in range(i + 1, len(p_x)):
                dist = p_x[i].get_dist(p_x[j])
                if small_path == -1:
                    small_path = dist
                else:
                    if dist < small_path:
                        small_path = dist

        return small_path


def main():
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N = input_lines.pop(0)
    points = []
    for line in input_lines:
        x, y = line.split()
        point = Point(x, y)
        points.append(point)

    # TODO remember floating point stuff
    print("{:.6f}".format(closest_points(points), 6))


if __name__ == "__main__":
    main()
