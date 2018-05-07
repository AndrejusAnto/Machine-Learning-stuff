from random import randint
# test data
xt = [0,1,2,3,4,5,6,7,8,9]
yt = [1,5,9,15,20,24,31,37,42,45]


w = randint(1,3)
b = randint(1,5)
print ("w", w, "b", b)

step = 1

def yprediction(xin , yin):
    byp = {}
    ypred= []
    for x in xin:
        y = (w*step) * x + b
        ypred.append(y)
    byp[(w,b)] = ypred
    print(byp)

    msel = {}    
    for k, v in byp.items():
        loss = [] 
        for lis, yr in zip(yin, v):
            los = (int(lis)-int(yr))**2
            loss.append(los)
            mse = sum(loss)/(len(loss))
        msel[k] = mse
    print(msel)
    # minv1 = min(msel, key=msel.get)        
    # print("formulė y = {}x + {}, MSE {}".format(minv1[0], minv1[1], msel[minv1]))

yprediction(xt, yt)
