#!/usr/bin/python
#-*- coding: utf-8 -*-

u'''
Copyright (c) Telefonica I+D. All rights reserved.
Description: implement a circle class
'''


'''
    >>> cr = Circle(5.0)
    >>> cr.area
    78.53981633974483
    >>> cr.radius = 3
    AttributeError: cannot modify the radius of the circle
'''
import math

class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def __getattr__(self, name):
        if name == 'area':
            return math.pi * self.radius ** 2

    def __setattr__(self, name, value):
        if name == "radius" and not self.radius:
            super(Circle, self).__setattr__(name, value)
        else:
            raise AttributeError()

cr = Circle(5.0)
print cr.area

            




