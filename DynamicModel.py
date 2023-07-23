import matplotlib.pyplot as plt
import numpy as np


class MassSpringDamper:
    def __init__(self, k, c, m, x0 = 0, v0 = 0, deltaT = 0.01):
        self.k = k
        self.c = c
        self.m = m
        self.deltaT = deltaT
        self.x = x0
        self.v = v0

    def update(self, F):
        XNew = self.v * self.deltaT + self.x
        VNew = self.deltaT / self.m * (F - self.c * self.v - self.k * self.x) + self.v
        self.x = XNew
        self.v = VNew
        return self.x
