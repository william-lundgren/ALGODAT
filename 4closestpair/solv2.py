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
 


p_x = [0,1,2,3,4,5,6]
p_y = [2,5,1,3,6,4,0]

P = PointCloud([Point(p_x[i],p_y[i]) for i in range(len(p_x))])

# p_yx = [7,2,0,3,5,1,4,6]

print(P.p_x, P.p_y)
print(P.split_list(p_x,p_y))