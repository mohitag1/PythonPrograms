#8)Python program to delete an element from a list by index
listofIntegers=[23,25,27,28,29,76]
indexToDel=4
print("Original List before deletion is",listofIntegers)

del(listofIntegers[indexToDel])

print("New List after deletion of %dth index is %s" %(indexToDel,listofIntegers))
