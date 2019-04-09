import numpy as np
import cv2
import turtle

NORTH = 0 #北方
EAST = 1 #东方
SOUTH = 2 #南方
WEST = 3 #西方

def turnLeft(d, x, y):
    if d == NORTH:
        x -= 1
        d = WEST
    elif d == EAST:
        y -= 1
        d = NORTH
    elif d == SOUTH:
        x += 1
        d = EAST
    elif d == WEST:
        y += 1
        d = SOUTH
    return d, x, y

def turnRight(d, x, y):
    if d == NORTH:
        x += 1
        d = EAST
    elif d == EAST:
        y += 1
        d = SOUTH
    elif d == SOUTH:
        x -= 1
        d = WEST
    elif d == WEST:
        y -= 1
        d = NORTH
    return d, x, y


world = np.ones([500,500,1], dtype=np.uint8)

world[:,:,0] = np.ones([500, 500])*255

d,x,y = WEST,250,250

count = 0

while count < 15000:
    if world[x][y][0] == 255:
        d, x, y = turnRight(d, x, y)
    else:
        d, x, y = turnLeft(d, x, y)

    world[x][y][0] = 255-world[x][y][0]
    count += 1

cv2.imshow("logo", world)
cv2.imwrite('ant.png', world)
cv2.waitKey(0)
cv2.destroyAllWindows()