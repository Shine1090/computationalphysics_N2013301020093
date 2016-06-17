# -*-coding:utf-8 -*-
import math
from visual import *

'''
用来在给定初始条件的情况下计算落点
'''

theta0=0
phi0=0
v0=0
v_wind=0
phi_wind=0
a=1
zgoal=0
x=[]
y=[]
z=[]
vx=[]
vy=[]
vz=[]

def ro(z):
    #rou = 
    return rou

def calculate(theta0,phi0,v0,v_wind,phi_wind,z0):
	
    global zgoal,vx,vy,vz,x,y,z
    vh0=v0*math.cos(theta0)
    vz=[v0*math.sin(theta0),]
    vx=[vh0*math.cos(phi0),]
    vy=[vh0*math.sin(phi0),]
    vwx=v_wind*math.cos(phi_wind)
    vwy=v_wind*math.sin(phi_wind)
    rou=1
    dt=0.01/v0
    x=[0,]
    y=[0,]
    z=[z0,]
    G=10

    while True:
        vrx=vx[-1]-vwx
        vry=vy[-1]-vwy
        vr_sq=vrx**2+vry**2+vz[-1]**2
        '''
        fx=-1.*a*rou*math.sqrt(vr_sq)*vrx
        fy=-1.*a*rou*math.sqrt(vr_sq)*vry
        fz=-1.*a*rou*math.sqrt(vr_sq)*vz[-1]-G
        '''
        fx=0
        fy=0
        fz=-G
        dvx=fx*dt
        dvy=fy*dt
        dvz=fz*dt
        vx.append(vx[-1]+dvx)
        vy.append(vy[-1]+dvy)
        vz.append(vz[-1]+dvz)
        x.append(x[-1]+vx[-1]*dt)
        y.append(y[-1]+vy[-1]*dt)
        z.append(z[-1]+vz[-1]*dt)
        if z[-1]<zgoal:
            break

def read():
    global zgoal,vx,vy,vz,x,y,z
    '''
    theta0=float(raw_input('输入发射仰角：'))*math.pi/180
    phi0=float(raw_input('输入发射方位角：'))*math.pi/180
    phi_wind=float(raw_input('输入风向方位角：'))*math.pi/180
    v0=float(raw_input('输入发射初速度：'))
    v_wind=float(raw_input('输入风速：'))
    z0=float(raw_input('输入发射位置初始高度：'))
    zgoal=float(raw_input('输入目标落点高度：'))
    '''
    theta0=70*math.pi/180
    phi0=30*math.pi/180
    phi_wind=-40*math.pi/180
    v0=200.
    v_wind=100.
    z0=2000.
    zgoal=10.
    
    calculate(theta0,phi0,v0,v_wind,phi_wind,z0)

def show():
    global x,y,z
    floor=box(position=(0,0,0),length=abs(x[-1])*2.5, height=0.5, width=abs(y[-1])*2.5, color=color.yellow)
    ball = sphere (pos=(0,z[0],0), radius=15, color=color.blue)
    ball.trail = curve(color=color.red)
    for i in range(len(x)):
        rate(500000)
        ball.pos.x=x[i]
        ball.pos.y=y[i]
        ball.pos.z=z[i]
        ball.trail.append(pos=ball.pos)

read()
show()

