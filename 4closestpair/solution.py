import math
import sys
import time

class Point:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def get_dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def __repr__(self):
        return f"{self.x, self.y}"

def closest_points(points):
    n = len(points)
    p_x = sorted(points, key=lambda p: p.x) #sorted on x, O(nlogn)
    p_y = sorted(points, key=lambda p: p.y) #sorted on x, O(nlogn)
    return closest(p_x, p_y, n) 

def closest(p_x, p_y, n):
    l_x, l_y, r_x, r_y, split_x  = split_list(p_x, p_y)

    #Divide and conquer
    if n >= 4:
        d_1 = closest(r_x, r_y, n/2)
        d_2 = closest(l_x, l_y, n/2)
        delta = min(d_1, d_2)

        s_y = [p for p in p_y if abs(p.x - split_x) < delta]
        
        for i in range(len(s_y)): #O(n) but hopefully with small coeff
            for j in range(i + 1, min(i+6, len(s_y))): #O(1) but quite big coeff
                dist = s_y[i].get_dist(s_y[j])
                if dist < delta:
                    delta = dist
        return delta
    
    # Brute force
    else:
        smallest_distance = -1
        for i in range(len(p_x)):
            for j in range(i + 1, len(p_x)):
                dist = p_x[i].get_dist(p_x[j])
                if smallest_distance == -1:
                    smallest_distance = dist
                elif dist < smallest_distance:
                    smallest_distance = dist

        return smallest_distance

def split_list(p_x, p_y):
    n = len(p_x)
    half = n//2
    l_x = p_x[:half]
    r_x = p_x[half:]
    l_y = []
    r_y = []
    split_x = r_x[0].x
    for p in p_y: #O(n)
        if p.x<split_x:
            l_y.append(p)
        else:
            r_y.append(p)
    return l_x,l_y,r_x,r_y, split_x

def main():
    tstart=time.time()
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
    sys.stderr.write(f"Time: {time.time()-tstart}\n")


if __name__ == "__main__":
    main()