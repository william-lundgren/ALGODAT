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

class PointCloud:
    def __init__(self, points):
        self.N = len(points)
        self.points = sorted(points, key=lambda p: p.x) #sorted on x, O(nlogn)
        self.p_x = [i for i in range(self.N)] #point ids sorted on x
        self.p_y = sorted([i for i in range(self.N)], key = lambda i : self.points[self.p_x[i]].y) #point ids sorted on y
    
    def split_list(self, p_x, p_y):
        n = len(p_x)
        half = n//2
        l_x = p_x[:half]
        r_x = p_x[half:]
        l_y = [0]*half
        r_y = [0]*(n-half)
        il, ir = 0,0 
        for p in p_y: #Retain sorting for p_y and split correctly. Should be O(n) (but small coeff?)
            if p<p_x[0]+half:
                l_y[il] = p
                il += 1
            else:
                r_y[ir] = p
                ir += 1
        return l_x,l_y,r_x,r_y
 
    def closest_points(self):
        return self.closest(self.p_x, self.p_y, self.N)


    def closest(self, p_x, p_y, n):
        l_x, l_y, r_x, r_y  = self.split_list(p_x, p_y)

        if n >= 4:
            d_1 = self.closest(r_x, r_y, (n+.5)//2)
            d_2 = self.closest(l_x, l_y, (n)//2)
            delta = min(d_1, d_2)
            streck = self.points[r_x[0]].x

            # One could create s_y by doing: 
            # s_y = [p for p in p_y if abs(self.points[p].x - streck) < delta]
            # This checks more pairs than neccesary. Our method is only slightly quicker though, worth it? 
            # The difference is that (p >= s_xl and p <= s_xr) is quicker than (abs(self.points[p].x - streck) < delta))
            # Since p_x is sorted in x, we can look at the closest points and stop looking as soon as we are not close enough anymore. 
            # Lets frist find edge elemets of s, s_xl and s_xr, by walking in x (in both L and R) from streck
            s_xl = r_x[0]
            s_xr = r_x[0] #start at streck
            looking = True
            while looking:
                # sys.stderr.write(f"s_xl: {s_xl}\n")
                if s_xl <= p_x[0]: #stop if weve reached the edge
                    break
                point = self.points[p_x[s_xl-p_x[0]-1]] #look one step left
                if abs(point.x - streck) < delta:
                    s_xl -= 1 #take one step left
                else:
                    looking = False
            looking = True
            while looking:
                if s_xr >= p_x[-1]: #stop if weve reached the edge
                    break
                point = self.points[p_x[s_xr-p_x[0]+1]] #look one step right
                if abs(point.x - streck) < delta:
                    s_xr += 1 #take one step right
                else:
                    looking = False

            # We now want to create and sort s_y based on y. This can be done in O(n) as we have a "constant lookup-time in s_x."
            # We loop through p_y and simply check wheter or not p is within [s_xl, s_xr]
            s_y = []
            for p in p_y:
                if p >= s_xl and p <= s_xr:
                    s_y.append(p)
            #We now have s_y

            for i in range(len(s_y)): #O(n) but hopefully with small coeff
                for j in range(i + 1, min(i+6, len(s_y))): #O(1) but quite big coeff
                    dist = self.points[s_y[i]].get_dist(self.points[s_y[j]])
                    if dist < delta:
                        delta = dist
            return delta
        
        # Fuck it we hardcoding, i.e we have reached a base case and cannot recurse anymore
        else:
            small_path = -1
            for i in range(len(p_x)):
                for j in range(i + 1, len(p_x)):
                    dist = self.points[p_x[i]].get_dist(self.points[p_x[j]])
                    if small_path == -1:
                        small_path = dist
                    else:
                        if dist < small_path:
                            small_path = dist

            return small_path


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

    P = PointCloud(points)
    # TODO remember floating point stuff
    print("{:.6f}".format(P.closest_points(), 6))
    sys.stderr.write(f"Time: {time.time()-tstart}\n")


if __name__ == "__main__":
    main()