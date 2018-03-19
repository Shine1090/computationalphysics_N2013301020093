
# 作业三 
====

孙博阳  
201728000807100  

-----

* ### 编写程序。从键盘输入圆半径r，输入圆柱高h，求圆周长、圆面积、圆球表面积、圆球体积、圆柱体积，并输出结果。

代码及运行结果：


```python
from math import pi

#输入半径和高
r=float(input('输入半径:'))
h=float(input('输入圆柱的高:'))

#计算周长、面积、球表面积、球体积、圆柱体积
c=2*pi*r
s=pi*r**2
s_ball=4*s
v_ball=s_ball*r/3
v_column=s*h

#输出
print('周长: ',c,'\n面积: ',s,'\n球表面积: ',s_ball,'\n球体积: ',v_ball,'\n圆柱体积: ',v_column)
```

    输入半径:2.2
    输入圆柱的高:5
    周长:  13.823007675795091 
    面积:  15.205308443374602 
    球表面积:  60.821233773498406 
    球体积:  44.6022381005655 
    圆柱体积:  76.02654221687301
    

* ### 编写程序。从键盘输入华氏温度，要求输出摄氏温度。公式为：c=5/9*(F-32)

代码及运行结果：


```python
F=int(input('输入华氏温度（℉）: ')) #输入华氏温度
print('对应摄氏温度为:',5/9*(F-32),'℃') #计算并输出摄氏温度
```

    输入华氏温度（℉）: 54
    对应摄氏温度为: 12.222222222222223 ℃
    

* ### 练习使用Python帮助。查看random模块内容；查看该模块中randrange函数的说明。

代码及运行结果：


```python
import random
dir(random)
```




    ['BPF',
     'LOG4',
     'NV_MAGICCONST',
     'RECIP_BPF',
     'Random',
     'SG_MAGICCONST',
     'SystemRandom',
     'TWOPI',
     '_BuiltinMethodType',
     '_MethodType',
     '_Sequence',
     '_Set',
     '__all__',
     '__builtins__',
     '__cached__',
     '__doc__',
     '__file__',
     '__loader__',
     '__name__',
     '__package__',
     '__spec__',
     '_acos',
     '_bisect',
     '_ceil',
     '_cos',
     '_e',
     '_exp',
     '_inst',
     '_itertools',
     '_log',
     '_pi',
     '_random',
     '_sha512',
     '_sin',
     '_sqrt',
     '_test',
     '_test_generator',
     '_urandom',
     '_warn',
     'betavariate',
     'choice',
     'choices',
     'expovariate',
     'gammavariate',
     'gauss',
     'getrandbits',
     'getstate',
     'lognormvariate',
     'normalvariate',
     'paretovariate',
     'randint',
     'random',
     'randrange',
     'sample',
     'seed',
     'setstate',
     'shuffle',
     'triangular',
     'uniform',
     'vonmisesvariate',
     'weibullvariate']




```python
help(random.randrange)
```

    Help on method randrange in module random:
    
    randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.
    
    
