s="Hi there Sam!"
print(s.split())

s="The diameter of {planet} is {diameter} kilometers."
print(s.format(planet="Earth",diameter=12742))

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':
[1,2,3,'hello']}]}]}
s=d['k1'][3]['tricky'][3]['target'][3]
print(s)

import numpy as np
s=np.zeros(10)
print(s)
s=np.ones(10)*5
print(s)
s=np.arange(20,35,2)
print(s)
s=np.arange(0,9).reshape(3,3)
print(s)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
s=np.concatenate((a,b),axis=0)
print(s)

import pandas as pd
data = ['a','b','c']
df = pd.DataFrame(data,columns=['Name'])
print(df)

import pandas as pd
sdate='2023-01-01'
edate='2023-02-10'
s=pd.date_range(sdate,edate,freq='d')
print(s)

import pandas as pd
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]]
df=pd.DataFrame(lists,columns=['index','name','age'])
print(df)
