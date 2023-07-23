import matplotlib.pyplot as plt
import numpy as np

#this class will help us when working with the PID regulator

class PID:
    def __init__(self, kP, kD, kI, deltaT, upper_bound, lower_bound):
        self.kP = kP
        self.kD = kD
        self.kI = kI
        self.deltaT = deltaT
        self.prev_err = None
        self._P = 0
        self._D = 0
        self._I = 0
        self.upper_bound = upper_bound
        self.lower_bound = lower_bound

    def update(self, x, xdes):
        err = x - xdes
        self._P = self.kP * err
        if self.prev_err is not None:
            self._D = self.kD * (err - self.prev_err) / self.deltaT
        self._I += self.kI * err
        self.prev_err = err
        outp = self._P + self._D + self._I
        return outp
    
    def _constrain(self, x):
        if x > self.upper_bound:
            x = self.upper_bound
        elif x < self.lower_bound:
            x = self.lower_bound
        return x
