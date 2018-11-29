'''
    TODO:
            - dealising (remove w_k values for |k| > N/3)
            - runge-kutta 2 or 4
            - lower viscosity
            - check energy/enstrophy
            - dynamic time-step
'''


# coding: utf-8

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

mu = 1e-3
i = 1.0j

steps = 50000

h = 1
w = 1
dx = dy = 0.01
dt = 1e-2

nx, ny = int(w/dx) , int(h/dy)

kx = np.fft.fftfreq(nx,dx)
ky = np.fft.fftfreq(ny,dy)





ksqu = sum(np.meshgrid(kx*kx,ky*ky)).T
ksqu[0][0] = 1.

ky,kx = np.meshgrid(kx,ky)

w = np.random.rand(nx,ny)-0.5


wh = np.fft.fft2(w)
wh[0][0] = 0.



#print(wh)

uxh = i*ky*wh/ksqu
uyh = -i*kx*wh/ksqu

#print(uxh)
#print(kx)

ux = np.fft.ifft2(uxh)
uy = np.fft.ifft2(uyh)
print(np.amax(np.real(ux)))
print("Max von ux: " + str(np.amax(np.real(ux))))
print("Max von uy: " + str(np.amax(np.real(uy))))
print(dx/max((np.amax(np.real(ux)),np.amax(np.real(uy)))))
#print(ux)
#print(uy)

# plt.imshow(w)
# plt.colorbar()
start = w.copy()


# In[3]:

snapshots = [np.real(w)]


for n in range(steps):
    wh = wh + dt * ((-1)*mu*ksqu*wh - i*kx*(np.fft.fft2(ux*w)) - i*ky*(np.fft.fft2(uy*w)))
    wh[0][0] = 0.
    uxh = i*ky*wh/ksqu
    uyh = -i*kx*wh/ksqu
    ux = np.fft.ifft2(uxh)
    uy = np.fft.ifft2(uyh)
    w = np.fft.ifft2(wh)
    if(n%100 == 0):
        print np.amax(np.real(ux))
        snapshots.append(np.real(w)/np.amax(np.real(w)))



# In[4]:


# plt.imshow(np.real(w))
# plt.colorbar()
# plt.show()
# #print(np.real(w))
#
# plt.imshow(np.real(start-w))
#

fig, ax = plt.subplots(1,1,figsize = (9,9), tight_layout = True)
im = plt.imshow(snapshots[0])
plt.colorbar()
def animate(p):
    im.set_array(snapshots[p])

anim = FuncAnimation(fig,animate, interval = 80, frames = steps/100)

#anim.save('hmm.gif', writer= 'imagemagick')

#plt.imshow(snapshots[-1])
plt.show()
