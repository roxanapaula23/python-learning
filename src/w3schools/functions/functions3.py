

import math


def average(list):
    return sum(list)/len(list)


list = [10, 25, 45, 55, 65]
average = average(list)

print("Average of the list:", round(average, 2))


def my_pi():
    x = math.pi
    print(x)


my_pi()


def area_of_square(side_of_square):
    area = side_of_square * side_of_square
    return area


side_of_square = 5
area = area_of_square(side_of_square)
