import numpy as np
import random as rand

A=10 #y=A+B*x
B=0.75
x_test=np.arange(0,40,1) #x-values
x_error=np.random.rand(1,len(x_test))-0.5 #adding noise to the the data
y_test=A+B*(x_test+x_error[0]) #y-values

ans=np.column_stack((x_test,y_test))
np.savetxt('test.dat', ans[1:],fmt='%2.3f')



