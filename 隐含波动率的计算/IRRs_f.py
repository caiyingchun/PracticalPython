import scipy as sp

def npv_f(rate, cashflows):
    total = 0.0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate)**i
    return total

def IRRs_f(cash_flows):
    n=1000
    r=range(1,n)
    epsilon=abs(sp.mean(cash_flows)*0.01)
    irr=[]
    npv=[]
    for i in r:
        npv.append(0)
    lag_sign=sp.sign(npv_f(r[0]*1.0/n*1.0,cash_flows))
    for i in range(1,n-1):
        interest=r[i]*1.0/n*1.0
        npv[i]=npv_f(interest,cash_flows)
        s=sp.sign(npv[i])
        if s*lag_sign<0:
            lag_sign=s
            irr.append(interest)
    return irr

if __name__ == '__main__':
    cashflows = [55, -50, -50, -50, 100]
    result = IRRs_f(cashflows)
    print result