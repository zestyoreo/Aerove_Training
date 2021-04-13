import numpy as np
from numpy import random

x = random.normal(size=(20, 20))

a=random.rand((20))
a=a*100
y=a.astype('i')
print(y)

xt=x.transpose()
theta=xt @ x
theta=np.linalg.inv(theta) @ xt
theta=theta @ y

print(theta)