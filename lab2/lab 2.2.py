import numpy as np
from scipy import optimize
from scipy.optimize import minimize
print("--------Gauss_method--------------------------------------------------------")
def getApprox(x,y,n):
    sumx = 0.0
    sumy = 0.0
    sumx2 = 0.0
    sumxy = 0.0
    for i in range(n):
        sumx+=x[i]
        sumy+=y[i]
        sumx2+=x[i]*x[i]
        sumxy+=y[i]*x[i]
    a=(n*sumxy-(sumy*sumx))/(n*sumx2-sumx*sumx)
    b=(sumy-a*sumx)/n
    return (a,b)
a = np.random.random(1)[0]
b = np.random.random(1)[0]
y = []
x = []
xk = 0.0
for k in range(100):
    xk = k / 100.0
    x.append(xk)
    y.append(a*xk+b+(np.random.normal(loc=0.5, scale=0.15, size=1)[0]))
(a1,b1)=getApprox(x,y,100)
print(a1,b1)
print("------brute_method---------------------------------------------------------------")

def f1(z, *params):
    a,b= z
    x,y=params
    sum = 0.0
    for i in range(100):
        sum+=(a*x[i]+b-y[i])**2
    return sum

def aaaf(z, *params):
    a,b= z
    x,y=params
    sum = 0.0
    for i in range(100):
        sum+=((a/(1.0+b*x[i]))-y[i])**2
    return sum
params = x,y
rranges = (slice(-4, 4, 0.25), slice(-4, 4, 0.25))
resbrute = optimize.brute(f1, rranges, args=params, full_output=True,
                          finish=optimize.fmin)
print(resbrute[0])
print("----Nelder-Mead_method-----------------------------------------------------------------")
x0 = [0,0]
res = minimize(f1, x0, args=params, method='nelder-mead',
    options={'xtol': 1e-8, 'disp': False})

print(res.x)


print("------brute--f2-------------------------------------------------------------")
params = x,y
rranges = (slice(-4, 4, 0.25), slice(-4, 4, 0.25))
resbrute = optimize.brute(aaaf, rranges, args=params, full_output=True,
                          finish=optimize.fmin)
print(resbrute[0])
print("----nelder-mead------f2-----------------------------------------------------------")
x0 = [0,0]
res = minimize(aaaf, x0, args=params, method='nelder-mead',
    options={'xtol': 1e-8, 'disp': False})

print(res.x)
