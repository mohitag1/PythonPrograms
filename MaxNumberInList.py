#7)Python program to find the largest number in a list without using built-in functions
max=0
listofIntegers=[23,25,26,13,16,29,28]
for i in listofIntegers:
    if(i>max):
        max=i

print("Max number of list %s is %d" %(listofIntegers,max))
    

