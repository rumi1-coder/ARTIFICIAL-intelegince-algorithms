import numpy as np
import matplotlib.pyplot as plt

# Define the differential equation
def pendulum(theta, t):
    g = 9.81
    L = 1
    return [theta[1], -(g/L)*np.sin(theta[0])]

# Define the initial conditions
theta0 = [0, 3]

# Set up the time interval
t0 = 0
tmax = 20
dt = 0.01
t = np.arange(t0, tmax, dt)

# Implement the Runge-Kutta method
def rk4_step(f, y, t, dt):
    k1 = dt*f(y, t)
    k2 = dt*f(y + 0.5*k1, t + 0.5*dt)
    k3 = dt*f(y + 0.5*k2, t + 0.5*dt)
    k4 = dt*f(y + k3, t + dt)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6

y = np.zeros((len(t), 2))
y[0] = theta0
for i in range(len(t)-1):
    y[i+1] = rk4_step(pendulum, y[i], t[i], dt)

# Plot the results
plt.plot(t, y[:, 0])
plt.xlabel('Time (s)')
plt.ylabel('Angular displacement (rad)')
plt.show()