# -*- coding: utf-8 -*-

from pylab import *
import pickle

#本程序是用来计算物体在流体中下落的速度随时间的变化
#流体产生的阻力近似认为是和物体的速度成正比： f=av

t_total=0
dt=0
t=[0,]
d=[0,]
v=[]
g=0
n=0
m=0
a=0

def initialize():
    global t_total,dt,v,n,g,m,a
    print '输入总时间(不要太大，否则可能看到的结果就是两条直线)：'
    t_total=float(raw_input())
    print '输入初速度(向上为负)：'
    v=[float(raw_input()),]
    print '输入重力加速度：'
    g=float(raw_input())
    print '输入f=av中的阻力系数a:'
    a=float(raw_input())
    print '输入物体质量：'
    m=float(raw_input())
    print '输入时间步长(建议不要大于', m/a/20.0, '否则运算结果可能出现较大偏差)'
    dt=float(raw_input())
    n=int(t_total/dt)

def calculate():
    global dt,v,n,g,t,d,m,a
    for i in range(1,n+1):
        t.append(dt*i)
        dv=(g-a*v[-1]/m)*dt
        d.append(d[-1]+(v[-1]+dv/2)*dt)
        v.append(v[-1]+dv)
    

def output():
    global v,t,d,n
    for i in range(0,n+1):
        print t[i],'  ',v[i],'  ',d[i]
    
initialize()
calculate()
output()

plot(t,v,'--')
plot(t,d,'-')
#scatter(t,d)
show()
savefig('output.jpg')

