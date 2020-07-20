def threeNumberSum(array, targetSum):
    # Array needs to be sorted so that the smaller numbers will be on the
	# left and the larger numbers on the right.
	array.sort()
	#Will need an array for the triplets
	triplets = []
	#Loop through the array
	for i in range(len(array) - 2):
		#The current number will be placed at the beginning of the array
	#The left pointer will be set at the number after the current
	    left = i + 1
	#The right pointer will be set at the end of the array
	    right = len(array) - 1
	#Now we want to find 3 numbers in the array that equal the target
	#sum
	    while left < right:
		#We set the current sum equal to the current number plus the
	#left pointer,and the right pointer
	        currentSum = array[i] + array[left] + array[right]
	#If the current sum equals the target sum, then we append the
	#current number, the left and the right pointer to the triplets
	#array
	        if currentSum == targetSum:
	            triplets.append([array[i], array[left], array[right]])
	#Then increment the left pointer and decrement the right
	#pointer to find another triple
	            left += 1
	            right -= 1
	        elif currentSum < targetSum:
	#If the current sum is less than the target sum, increment
		#the left pointer.
	            left += 1
	#If the current sum is greater than the target sum,
	#decrement the right pointer
	        elif currentSum > targetSum:
	            right -= 1
	return triplets
