#3)Python program to find the product of a set of real numbers

listNum=[2,3.5,7.8,9]
product=1
for i in listNum:
    product*=i

print("Product of %s is %0.2f" %(listNum,product))
