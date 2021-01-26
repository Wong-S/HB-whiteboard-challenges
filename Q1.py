#Missing Number Problem:
Given a list of numbers return the missing number from the list. All positive integers. 

Test cases:
I : [1,3,5,4], 5
O: 2

I: [] 
O: none 

#Thought/Pseudo

#Create a function with two parameters (List, max_num)
# Given the max_num, 
#Create a new lst based on the max number 
#Compare that new lst to the input lst. 

List comprehension methods instead of creating an empty lst. 

#original_list = [ ]
#for i in range(1, max_num + 1):
 #original_list.append(i)

#for num in List:
	#if num in original_list:
		#pop()

Return the num in List 

#Code 
Def missing_num(num_lst , max_num):
	Comparison_lst = [ ]
	For i in range(1, max_num + 1):
		comparision_lst.append(i)

	For num in num_lst:
		If num not in comparison_lst:
			Return num 
