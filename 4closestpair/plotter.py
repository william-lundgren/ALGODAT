import sys
import matplotlib.pyplot as plt
import math

def main():
    input_lines = []
    for line in sys.stdin:
        if '' == line.rstrip():
            break
        input_lines.append(line.replace("\n", ""))

    N = input_lines.pop(0)
    points = []
    xs = []
    ys = []
    for line in input_lines:
        x, y = line.split()
        xs.append(int(x))
        ys.append(int(y))
    for i in range(len(xs)):
        for j in range(len(xs)):
            if j!= i:
                d = math.sqrt((xs[i]-xs[j])**2+(ys[i]-ys[j])**2)
                if  d < 7:
                    print(d)
    plt.scatter(xs,ys)
    plt.show()



if __name__ == "__main__":
    main()
