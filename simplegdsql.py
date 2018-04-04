import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS xiry')

sql_command = """
CREATE TABLE xiry (x,y);"""

cursor.execute(sql_command)

xi = input("Iveskite x reiksme viena po kitos per kableli: ").split(",")
yi = input("Iveskite y reiksme viena po kitos per kableli: ").split(",")

step = 1

for x, y  in zip(xi, yi):
    format_str = """INSERT INTO xiry (x, y)
    VALUES ("{xr}", "{yr}");"""

    sql_command = format_str.format(xr=x, yr=y)
    cursor.execute(sql_command)

cursor.execute("SELECT * FROM xiry") 
print("fetchall:")
result = cursor.fetchall() 

xin = []
yin = []

for x1,y1 in result:
    xin.append(x1)
    yin.append(y1)
        
connection.commit()
connection.close()

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

# test data
# x = 0,1,2,3,4,5,6,7,8,9
# y = 1,5,9,15,20,24,31,37,42,45
