import numpy as np
from numpy import random

x = random.normal(size=(20, 20))

y=np.random.randint(10000,size=(20))
y=y.astype('i')
print(y.dtype)

xt=x.transpose()
theta=xt @ x
theta=np.linalg.inv(theta) @ xt
theta=theta @ y

print(theta)