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

#=================================
#Alt Method:

def missing_number(nums, max_num):
    sorted_nums = sorted(nums)
    #[1,2,3,4,5,6,7,9,10]
    
    count=0
    
    for i, num in enumerate(sorted_nums):
       
        if sorted_nums[count+1] - sorted_nums[i] == 1:
            count += 1
        else:
            return nums[i] + 1
               
print(missing_number([2, 1, 4, 3, 6, 5, 7, 10, 9], 10))

#=========================
#Solution:


   # 1st solution: Initial solution: keep track of what you've
    #               seen in a separate list

    seen = [False] * max_num

    for n in nums:
        seen[n - 1] = True
        
# The False value is the one we haven't seen

    return seen.index(False) + 1
