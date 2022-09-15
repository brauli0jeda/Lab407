#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 07:57:33 2022

@author: jashansingh
"""
import numpy as np                         # import numpy
import matplotlib.pyplot as plt            # import matplotlib.pyplot

# Define all required constants 
solar_mass = 1            # solar mass (M_s)  2.0 *10**30 kg
big_G = 39.5              # universal graitational constant in AU^3M_s^-1yr^-2.
# Note that 1 AU = 1.496 * 10^11 m  
alpha = 0.01                               # in AU^2
mass_jupiter = 10^-3                       # in MS
orbit_r_jupiter = 5.2                      # in AU  
             
# define intital values of postion and velocity
xi,yi = 0.47,0.0     # initial postion of Mercury, units are AU
v_xi,v_yi = 0.0,8.17 # intital velocity components, units are AU/yr

# Initialize time array
time = np.linspace(0.0001, 1, 10000) 

# define time step 
t0 = 0                # time staring at 0
dt = 0.0001 # vaule of time increment = 0.0001

# Initialize a xf,yf,vxf and vyf array with same number of elements as 
# time_vaule array

xf = np.zeros(np.shape(time))  # final values of position in x-direction
yf = np.zeros(np.shape(time))  # final values of position in y-direction
vxf = np.zeros(np.shape(time)) # final values of velocity in x-direction
vyf = np.zeros(np.shape(time)) # final values of velocity in y-direction

# Define euler_cromer method function, and use equation from part 1a. 
# Use FOR loop for 10,000 itrations


########################## Question 1 C #######################################
################## PLEASE UNCOMMENT THIS SECTION TO SEE Q1C'S RESULT ##########

# def euler_cromer_1c(t,x,y,vx,vy):
#     """Returns xf, yf,vxf and vyf  after modyfing according to Euler-Cromer 
#     method."""
   
#     for i in range(len(time)):   
#         r = np.sqrt(x**2+y**2)   # distance between the planets
        
#         vxf[i] = vx              # Current velocity in y-dir & modify vyf array 
#         vx =  vx + (-(big_G * solar_mass*x)/r**3)* dt 
#         xf[i] = x                # Current position in x-dir & modify xf array 
#         x = x + vx*dt           # next x poisiton after one itration of i 
        
#         vyf[i]= vy               # Current velocity in y-dir & modify vyf array
#         vy =  vy + (-(big_G * solar_mass*y)/r**3)* dt 
#         yf[i] = y                # Current position in y-dir & modify xf array 
#         y = y + vy*dt            # next y poisiton after one itration of i
        
    
# euler_cromer_1c(t0,xi,yi,v_xi,v_yi)  
# velocity = np.sqrt(vxf**2+vyf**2) # velocity of the planet 
 
# # Plot x vs y and velocity vs time 

# """ x vs y Plot """
# plt.subplot(2,1,1)
# plt.plot(xf,yf,ls=':',c='r')
# plt.title('x Vs y Plot')
# plt.xlabel('x (AU)')
# plt.ylabel('y (AU)')

# """ Velocity Vs Time Plot """
# plt.subplot(2,1,2)
# plt.plot(time,velocity,ls=':',c='g')
# plt.title('Time Vs Velocity Plot')
# plt.xlabel('Time (yr)')
# plt.ylabel('Velocity (AU/yr)')
# plt.tight_layout()

########################## Question 1 D #######################################
################## PLEASE UNCOMMENT THIS SECTION TO SEE Q1D'S RESULT ##########

def euler_cromer_1d(t,x,y,vx,vy):
    """Returns xf, yf,vxf and vyf  after modyfing according to Euler-Cromer 
    method."""
   
    for i in range(len(time)):   
        r = np.sqrt(x**2+y**2)   # distance between the planets
        
        vxf[i] = vx              # Current velocity in y-dir & modify vyf array 
        vx =  vx + ((-(big_G * solar_mass*x)/r**3)*(1+(alpha/r**2))* dt)
        xf[i] = x                # Current position in x-dir & modify xf array 
        x = x + vx*dt           # next x poisiton after one itration of i 
        
        vyf[i]= vy               # Current velocity in y-dir & modify vyf array
        vy =  vy + ((-(big_G * solar_mass*y)/r**3)*(1+(alpha/r**2))* dt)
        yf[i] = y                # Current position in y-dir & modify xf array 
        y = y + vy*dt            # next y poisiton after one itration of i
euler_cromer_1d(t0,xi,yi,v_xi,v_yi)  
velocity = np.sqrt(vxf**2+vyf**2) # velocity of the planet 

""" x vs y Plot """
plt.subplot(2,1,1)
plt.plot(xf,yf,ls=':',c='blue')
plt.title('x Vs y Plot')
plt.xlabel('x (AU)')
plt.ylabel('y (AU)')

""" Velocity Vs Time Plot """
plt.subplot(2,1,2)
plt.plot(time,velocity,ls=':',c='b')
plt.title('Time Vs Velocity Plot')
plt.xlabel('Time (yr)')
plt.ylabel('Velocity (AU/yr)')
plt.tight_layout()
        



