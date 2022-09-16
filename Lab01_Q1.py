# Braulio Ojeda Valencia, Jashandeep Singh
# WORKLOAD: Jashandeep (a,c), Braulio (b,d)
# PURPOSE: This program is split into 3 parts. The first part (B) is pseudocode
# for modelling mercury's orbit about the sun. The second part (C) turns this 
# into code, and the third part (D) accounts for relativistic effects.
import numpy as np  # import numpy
import matplotlib.pyplot as plt  # import figure functions

# PART B
# Define gravitational constant, initial position and velocity components
# Initialize time array, as well as position and velocity components arrays
# Compute dt
# For 10,000 iterations (a 1 year duration), increment the position and 
# velocity arrays from the previous values using the Euler-Cromer method
# Plot velocity components as functions of time, plot orbit trajectory

# PART C
# Define gravitational constant, initial position and velocity components
G = 39.5 # [AU^3/(M_s*yr^2)] gravitational constant
x_0 = 0.47 # [AU] initial position, horizontal component
y_0 = 0.00 # [AU] initial position, vertical component
vx_0 = 0.00 # [AU/yr] initial velocity, horizontal component
vy_0 = 8.17 # [AU/yr] initial velocity, vertical component
# Initialize time array, as well as position and velocity components arrays
t = np.linspace(0,1,10000) # time array from 0 to 1yr, 10000 elements
N = len(t)  # number of time steps (length of time array)
x = np.empty(N) # array of horizontal positions (empty array of length N)
x[0] = x_0
y = np.empty(N) # array of vertical positions
y[0] = y_0
vx = np.empty(N) # array of horizontal velocities
vx[0] = vx_0
vy = np.empty(N) # array of vertical velocities
vy[0] = vy_0
# Compute dt
dt = t[1] - t[0] # [yr]
# For 10,000 iterations (a 1 year duration), increment the position and 
# velocity arrays from the previous values using the Euler-Cromer method
for i in range(N-1):
    x[i+1] = x[i] + dt*vx[i]
    y[i+1] = y[i] + dt*vy[i]
    r = np.sqrt(x[i+1]**2 + y[i+1]**2) # [AU] distance between sun and planet
    vx[i+1] = vx[i] - dt*G*x[i+1]/r**3
    vy[i+1] = vy[i] - dt*G*y[i+1]/r**3
# Plot velocity components as functions of time, plot orbit trajectory    
plt.figure() # horizontal velocity as a function of time
plt.plot(t, vx, label='vx versus t')
plt.ylabel('vx')
plt.xlabel('t')
plt.grid()
plt.legend()
plt.tight_layout()

plt.figure() # vertical velocity as a function of time
plt.plot(t, vy, label='vy versus t')
plt.ylabel('vy')
plt.xlabel('t')
plt.grid()
plt.legend()
plt.tight_layout()

plt.figure() # trajectory (vertical position as a function of horizontal one)
plt.plot(x, y, label='x versus y')
plt.ylabel('y')
plt.xlabel('x')
plt.grid()
plt.legend()
plt.tight_layout()

# PART D
# Define relativity constant
a = 0.01 # [AU^2]
# Re-initialize position and velocity components arrays
x = np.empty(N) # array of horizontal positions (empty array of length N)
x[0] = x_0
y = np.empty(N) # array of vertical positions
y[0] = y_0
vx = np.empty(N) # array of horizontal velocities
vx[0] = vx_0
vy = np.empty(N) # array of vertical velocities
vy[0] = vy_0
# For 10,000 iterations, increment the position and velocity arrays from the
# previous values using the Euler-Cromer method, now with relativistic fix
for i in range(N-1):
    x[i+1] = x[i] + dt*vx[i]
    y[i+1] = y[i] + dt*vy[i]
    r = np.sqrt(x[i+1]**2 + y[i+1]**2) # [AU] distance between sun and planet
    C = 1 + a/r**2 # correction term
    vx[i+1] = vx[i] - C*dt*G*x[i+1]/r**3
    vy[i+1] = vy[i] - C*dt*G*y[i+1]/r**3
# Plot orbit trajectory    
plt.figure()
plt.plot(x, y, label='x versus y (relativistic)')
plt.ylabel('y')
plt.xlabel('x')
plt.grid()
plt.legend()
plt.tight_layout()
