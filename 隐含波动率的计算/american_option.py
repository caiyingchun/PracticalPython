from math import exp,sqrt
import numpy as np

def binomialCallAmerican(s,x,T,r,sigma,n=100):
    deltaT = T/n
    u = exp(sigma * sqrt(deltaT))
    d = 1.0 / u
    a = exp(r * deltaT)
    p = (a - d) / (u - d)
    v = [[0.0 for j in np.arange(i + 1)] for i in np.arange(n + 1)]
    for j in np.arange(n+1):
        v[n][j] = max(s * u**j * d**(n - j) - x, 0.0)
    for i in np.arange(n-1, -1, -1):
        for j in np.arange(i + 1):
            v1=exp(-r*deltaT)*(p*v[i+1][j+1]+(1.0-p)*v[i+1][j])
            v2=max(v[i][j]-x,0) # early exercise 
            v[i][j]=max(v1,v2)
    return v[0][0]

def implied_vol_American_call(s,x,T,r,c):
    implied_vol=1.0;min_value=1000
    for i in range(1000):
        sigma=0.001*(i+1)
        c2=binomialCallAmerican(s,x,T,r,sigma)
        abs_diff=abs(c2-c)
        if abs_diff<min_value:
            min_value=abs_diff;implied_vol=sigma;k=i
    return implied_vol

if __name__ == '__main__':
    result1 = binomialCallAmerican(150, 150, 2./12.,0.003,0.2)
    result2 = implied_vol_American_call(150, 150, 2./12.,0.003,4.91)
    print result1
    print result2