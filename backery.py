# from pirog import make_pirog as mp
# import pirog as p

from pirog import *


make_pirog("big", 4)
make_cake( "small", 7)


def make_pirog(size_as_int, sugar):
    print("В пироге", size_as_int, "килограмм")
    print("Количества сахара", sugar)


make_pirog(7, 2)
make_pirog("big", 2)
