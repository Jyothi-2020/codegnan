
'''
Data Analysis
-------------
->This is the process of inspecting,cleaning,transforming and modeling data to discover useful insights.
Types of DA
------------
1.Descriptive Analysis
---------------------
->Summarizing data

2.Diagnostic Analysis
-----------------------
->Understanding Causes

3.Predictive analysis
----------------------
->Forecasting future outcomes

4.Prescriptive Analysis
------------------------
->Suggesting actions based on data

Why DA
-------
->To improve decision making
->Detects Trends & Patterns

Numpy(array concept in python)
------------------------------
->numpy(short) is also known as numerical python(full)
->This python library for numerical computing.it provides support for multi-dimensional arrays and linear algebra opearations,making it
  essential for data analysis
  
Using numpy in DA
--------------------
->Improved Performance
->Simplifies complex operations
->Easy daya manipulation


import numpy as np
arr_1=np.array([1,2,3,4])
print(arr_1)

import numpy as np
arr_1=np.array([[1,2,3,4],[3,4,5,6]])
print(arr_1)


import numpy as np
arr_1=np.array([[1,2,3,4],[3,4,5,6],[7,8,9,5]])
print(arr_1)

import numpy as np
arr_1=np.array([[1,2,3],[3,5,6]])
print(arr_1)
print(arr_1.shape)

op:[[1 2 3]
    [3 5 6]]
     (2, 3)


import numpy as np
arr_1=np.array([[1,2,3],[3,5,6]])
print(arr_1)
print(arr_1.shape)
reshaped=arr_1.reshaped(3,2)
print(reshaped)

import numpy as np
arr_1=np.array([1,2,3,5,6])
print(arr_1[2])

import numpy as np
arr_1=np.array([10,20,30,40,50])
print(arr_1*3)

import numpy as np
arr_1=np.array([[1,3],[4,5]])
arr_2=np.array([[5,6],[6,7]])
print(np.dot(arr_1,arr_2))

import numpy as np
arr_1=np.array([10,20,30])
nrm_copy=arr_1.view()
arr_1[0]=100
print(nrm_copy)
print(arr_1)

op:[100  20  30]
    [100  20  30]

import numpy as np
arr_1=np.array([10,20,30])
copy_dee=arr_1.copy()
arr_1[1]=200
print(copy_dee)
print(arr_1)

op:[10 20 30]
   [ 10 200  30]

Pandas
------
->The Pandas is a powerful data maniplation and analysis library.
->where it provides data structure like series and data frames for efficient data handling.

Methods Series
---------------
mean()
sum()
max()
min()
apply()
map()

import pandas as pd
any_=pd.Series([2999,15999,52999,4999,1999],
               index=['Earbuds','smartphone','laptop','watch','footwear'])
print(any_)

op:Earbuds        2999
smartphone    15999
laptop        52999
watch          4999
footwear       1999
dtype: int64

Dataframe
----------'''

import pandas as pd
data={'product':['Earbuds','smartphone','laptop','watch','footwear'],
      'Brand':['Noise','samsung','HP','fastrack','Nike'],
      'price':[1999,19999,49999,2999,3999],
      'stock':[30,20,10,60,15]}
dip=pd.DataFrame(data)
print(dip)

'''op:      product     Brand  price  stock
0     Earbuds     Noise   1999     30
1  smartphone   samsung  19999     20
2      laptop        HP  49999     10
3       watch  fastrack   2999     60
4    footwear      Nike   3999     15'''








