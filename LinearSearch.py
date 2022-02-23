#5)Python program to implement linear search

listIntegers=[5,6,7,8,9]

def LinearSearch(elemToSearch):
    flag=0
    for i in listIntegers:
        if(i == elemToSearch):
            flag=1
            break
        else:
            continue

    if(flag==1):
        print(elemToSearch,"found In",listIntegers)
    else:
        print(elemToSearch,"NOT found In",listIntegers)



LinearSearch(8)
LinearSearch(10)
      
