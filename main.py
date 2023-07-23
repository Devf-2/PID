import matplotlib.pyplot as plt
import numpy as np
from PID import PID
from DynamicModel import MassSpringDamper


model_x = []
P_hist, D_hist, I_hist, F_hist = [], [], [], []
deltaT = 0.001
T = 20
F = 0
t = np.arange(0, T, deltaT)

reg = PID(15, 7, 0.006, deltaT, -1, 1)
model = MassSpringDamper(1, 1, 1, deltaT=deltaT)
x_des = np.ones( len(t))



for i in range(len(t)):
    model_x.append(model.update(F))
    F = -reg.update(model_x[-1], x_des[i])
    P_hist.append(reg._P)
    D_hist.append(reg._D)
    I_hist.append(reg._I)
    F_hist.append(F)
    
fig, (ax1, ax2, ax3) = plt.subplots(ncols=3, figsize=[10, 7])

ax1.plot(t, model_x, label="real x")
ax1.plot(t, x_des, label="x desired")

ax2.plot(t, P_hist, label="P")
ax2.plot(t, D_hist, label="D")
ax2.plot(t, I_hist, label="I")

ax3.plot(t, F_hist, label="F")

ax1.legend()
ax1.plot()
ax2.legend()
ax2.plot()
ax3.legend()
ax3.plot()

plt.show()
#grtg



