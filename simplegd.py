yin = input("Iveskite y reiksme viena po kitos per kableli: ").split(",")
xin = input("Iveskite x reiksme viena po kitos per kableli: ").split(",")

step = 1

def yprediction():
    byp = {}
    for w in range(len(yin)):
        for b in range(len(yin)):
            ypred= []
            for x in xin:
                y = (w*step)*int(x) + int(b)
                ypred.append(y)
            byp[(w,b)] = ypred

    msel = {}    
    for k, v in byp.items():
        loss = [] 
        for lis, yr in zip(v, yin):
            los = (int(lis)-int(yr))**2
            loss.append(los)
            mse = sum(loss)/(len(loss))
        msel[k] = mse
    
    minv1 = min(msel, key=msel.get)        
    print("formulė y = {}x + {}, MSE {}".format(minv1[0], minv1[1], msel[minv1]))

yprediction() 

# y = 1,5,9,15,20,24,31,37,42,45
# x = 0,1,2,3,4,5,6,7,8,9
