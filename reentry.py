# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import math
cd = 2.2
cl = 0.0
A = 8.5
# print(D*math.sin(30*math.pi/180))
dt = 0.01
m = 16
g0 = 9.807

R = 6378000
v = []
p = []
h = []
s = []

d = []
def int_(a, b, c, d, e):
    v.append(a)
    p.append(b)
    h.append(c)
    s.append(d)
    b = e

# velocity = 7000 m/s , flight path angle = 30 degrees, height = 70000 mass = 5000 kg, cd = 0.7 , 150 m2.
int_(12000, -11*math.pi/180, 70000, 0, 0.1378)

#12.3
#print(v, p)
i = 0
T = 300
while h[i] > 0:
    g = g0*R*R/(R+h[i])**2
    #d = 1.22
    if h[i] < 11000:
        b = 0.0065
        T = T - b*(h[i-1] - h[i])
        d.append(1.225*math.exp(-g/287/T*h[i]))
    elif h[i] < 20000:
        b = 0
        T = T - b * (h[i - 1] - h[i])
        d.append(1.225 * math.exp(-g / 287 / T * h[i]))
        # d.append(1.225 * math.exp(-g/287/216.65 * h[i]))
    elif h[i] < 32000:
        b = -0.001
        T = T - b * (h[i - 1] - h[i])
        d.append(1.225 * math.exp(-g / 287 / T * h[i]))
        # d.append(1.225 * math.exp(-g/287/216.65 * h[i]))
    elif h[i] < 47000:
        b = -0.0028
        T = T - b * (h[i - 1] - h[i])
        d.append(1.225 * math.exp(-g / 287 / T * h[i]))
        # d.append(1.225 * math.exp(-g/287/228.65 * h[i]))
    elif h[i] < 51000:
        b = -0
        T = T - b * (h[i - 1] - h[i])
        d.append(1.225 * math.exp(-g / 287 / T * h[i]))
        # d.append(1.225 * math.exp(-g/287/228.65 * h[i]))
    elif h[i] < 71000:
        b = 0.0028
        T = T - b * (h[i - 1] - h[i])
        d.append(1.225 * math.exp(-g / 287 / T * h[i]))
        # d.append(1.225 * math.exp(-g/287/270.65 * h[i]))
    else:
        b = -0.002
        T = T - b * (h[i - 1] - h[i])
        d.append(1.225 * math.exp(-g / 287 / T * h[i]))
        # d.append(1.225 * math.exp(-g / 287 / 214.65 * h[i]))

    D = cd*float(d[i])*A*v[i]*v[i]/2
    L = cl*float(d[i])*A*v[i]*v[i]/2
    h.append(h[i] + v[i] * math.sin(p[i])*dt)
    s.append(s[i] + v[i] * math.cos(p[i]) * dt)
    # v.append(v[i] + (-D + m*g*math.sin(p[i]) - m*v[i]*v[i]/(R+h[i])*math.sin(p[i]))*dt/m)
    # p.append(p[i] + (-L + m*g*math.cos(p[i]) - m*v[i]*v[i]/(R+h[i])*math.cos(p[i]))*dt/m/v[i])
    # dv/dt = (v[i+1] - v[i])/dt   dt- discretized time interval.
    v.append(v[i] + (-D/m - 1 * g * math.sin(p[i]) ) * dt )
    p.append(p[i] + (L/m - g*math.cos(p[i]) )*dt/v[i])
    # + m * v[i] * v[i] / (R + h[i]) * math.sin(p[i]) * math.cos(p[i]) * math.cos(p[i])
    #+ m * v[i] * v[i] / (R + h[i]) * math.cos(p[i]) * math.cos(p[i]) * math.cos(p[i])
    i += 1
    print(h[i], 180*p[i]/math.pi, v[i], T)
d.append(1.225 * math.exp(-g / 287 / 288.15 * h[i]))
#print(h,'\n',i)
n = []
for t in p:
    n.append(t*180/math.pi)
#print(n)

print(len(h),len(d))

# plotting the points
plt.plot(s, h)

# naming the x axis
plt.xlabel('horizontal distance in m')
# naming the y axis
plt.ylabel('vertical distance in m')

# giving a title to my graph
plt.title('Ballistic Re-entry trajectory.')

# function to show the plot
plt.show()




