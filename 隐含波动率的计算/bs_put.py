from scipy import log,exp,sqrt,stats,sign

def bs_put(S,X,T,rf,sigma):
    d1 = (log(S/X)+(rf+sigma*sigma/2.)*T)/(sigma*sqrt(T))
    d2 = d1-sigma*sqrt(T)
    return X*exp(-rf*T)*stats.norm.cdf(-d2)-S*stats.norm.cdf(-d1)

if __name__ == '__main__':
    S=40; K=40; T=0.5; r=0.05; p=1.77
    diff=1; i=1; sigma_old=0.005
    sign_1=sign(p-bs_put(S,K,T,r,sigma_old)) 
    while(1):
        sigma=0.0001*(i+1)
        sign_2=sign(p-bs_put(S,K,T,r,sigma))
        i+=1
        if sign_1*sign_2<0:
            break
        else:
            sigma_old=sigma
            print('i, implied-vol, diff')
            print(i,(sigma_old+sigma)/2, diff)
