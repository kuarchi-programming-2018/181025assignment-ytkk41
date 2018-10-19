from turtle import *

def rose_window_recursion(points, ratio, depth):
    rectangle(points)
    new_points = deviding_points(points, ratio)
    if depth == 0:
        up()
        setpos(-200, -200)
    else:
        rose_window_recursion(new_points, ratio, depth - 1)

def deviding(p0, p1, r):
    return p0 * (1-r) + p1 * r

def rectangle(points):
    [[x0, y0], [x1, y1], [x2, y2], [x3, y3]] = points
    up()
    setpos(x0, y0)
    down()
    setpos(x1, y1)
    setpos(x2, y2)
    setpos(x3, y3)
    setpos(x0, y0)

def deviding_point(p0, p1, ratio):
    [x0, y0] = p0
    [x1, y1] = p1
    xr = deviding(x0, x1, ratio)
    yr = deviding(y0, y1, ratio)
    return [xr, yr]

def deviding_points(points, ratio):
    [p0, p1, p2, p3] = points
    pr0 = deviding_point(p0, p1, ratio)
    pr1 = deviding_point(p1, p2, ratio)
    pr2 = deviding_point(p2, p3, ratio)
    pr3 = deviding_point(p3, p0, ratio)
    return [pr0, pr1, pr2, pr3]