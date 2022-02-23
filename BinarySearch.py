#6)Python program to implement binary search


def binary_search(ListofIntegrs, eleToSrch):
	low = 0
	high = len(ListofIntegrs) - 1
	mid = 0

	while low <= high:

		mid = (high + low) // 2

		
		if ListofIntegrs[mid] < eleToSrch:
			low = mid + 1

		
		elif ListofIntegrs[mid] > eleToSrch:
			high = mid - 1

		
		else:
			return mid

	
	return -1



ListofIntegrs = [ 24, 30, 40, 50, 60 ]
eleToSrch = 60


result = binary_search(ListofIntegrs, eleToSrch)

if result != -1:
	print("Element %d is present at index %s" %(eleToSrch,str(result)))
else:
	print("Element is not present in array")
