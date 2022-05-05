n = int(input("Enter total number of points"))
x = []
y = []
xy = []
x2 = []
i=0
def diff(a,b):
    Di = []
    for i in range(len(a)):
        d = a[i] - b[i]
        Di.append(d)
    return(Di)
for i in range(n):
    x_1= int(input("x= "))
    y_1 =int(input("y= "))
    xy_1 =  x_1 * y_1
    x.append(x_1)
    y.append(y_1)
    xy.append(xy_1)
    x2.append(x_1**2)
    
x_sum = sum(x)
y_sum = sum(y)
xy_sum = sum(xy)
x2_sum = sum(x2)
x_mean = x_sum/n
y_mean = y_sum/n
a = ((n * xy_sum)-(x_sum * y_sum))/(n * x2_sum - x_sum**2)
#b = (n * xy_sum) - (x_sum * y_sum)/ ((n * x2_sum) - (x_sum**2))
b = (y_sum - a * x_sum)/n
print("a",a,"b",b)
y_pred = []
for i in range(n):
    y_pred.append(a * x_1  + b)
Var = diff(y,y_pred)
print("Variation: ",Var)
    
def sum(lst):
    suma = 0
    for i in range(len(lst)):
        suma = suma + lst[i]
    return suma

