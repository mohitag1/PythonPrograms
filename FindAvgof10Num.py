# 10)Python program to find the average of 10 numbers using while loop
lisofNum=[23,24,25,26,28,29,30,31,12,13]
i=0
sum=0
while(i<len(lisofNum)):
    sum+=lisofNum[i]
    i+=1

print("Average is",sum/i)

