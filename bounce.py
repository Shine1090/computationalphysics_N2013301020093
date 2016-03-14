import os
import time
x=0
y=0
xx=1
yy=1
ball=('      ########      ','   ##############   ',' ################## ','####################','####################',' ################## ','   ##############   ','      ########      ')
while True:
    print '='*70
    for i in range(1,y):
        print ' '*68,'='
    for i in range(0,8):
        print ' '*x,
        print ball[i],
        print ' '*(47-x)+'='
    for i in range(1,26-y):
        print ' '*68,'='
    print '='*70
    time.sleep(.2)
    x+=xx
    y+=yy
    if(x==47):
        xx=-1
    elif(x==0):
        xx=1
    if(y==25):
        yy=-1
    elif(y==0):
        yy=1
    os.system('cls')
