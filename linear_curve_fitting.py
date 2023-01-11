import numpy as np
from scipy.optimize import curve_fit,minimize
import matplotlib.pyplot as plt

#greate test data

A=10 #y=A+B*x
B=0.75
x_test=np.arange(0,40,1) #x-values
x_error=np.random.rand(1,len(x_test))-0.5 #adding noise to the the data
y_test=A+B*(x_test+x_error[0]) #y-values


#code for fitting the generated data

def G(x,A,B):#define a fit function
	return A+B*x

xx=x_test	
yy=y_test	

# bounded optimization using scipy.minimize
err = lambda p: np.mean((G(xx,*p)-yy)**2)
p_init = [0,0]
p_opt = minimize(err, p_init).x

print ('Original values:'+'A=',A,'and B=',B)
print ('Fitted vales:'+'A=',p_opt[0],'and B=',p_opt[1])




