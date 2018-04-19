from bs_call import bs_call
def implied_vol_call(S,X,T,r,c):
    for i in range(200):
        sigma=0.005*(i+1)
        diff=c-bs_call(S,X,T,r,sigma)
        if abs(diff)<=0.01:
            return i,sigma,diff

if __name__ == '__main__':
    result = implied_vol_call(40, 40, 0.5, 0.05, 3.3)
    print result