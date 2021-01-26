
#FizBuzz Problem: 

# No input 
# Test Case: Grab numbers through the whole range to test. Example, 15, etc 
# I: 3
# O: Fizz

# I: 5
# O: Buzz

# I: 3 , 5
# O: Fizzbuzz 

#Thought/Pseudo:  Be a little shorter with pseudo 

#Create a function (no parameters)
#Iterate through range 1-20
#Check if number is divisible 3 
#output “fizz”

#Check if number is divisible 5
#output “buzz”

#Check if number is divisible 3 and 5 
#output fizzbuzz 

#If none above
#output num 

#Code 

Def fizzbuzz():
	for num in range(1, 21):

		if num % 3 == 0 and num % 5 == 0 :
			print(“fizzbuzz”)

		elif num % 3 == 0:
			print(“fizz”)

		elif num % 5 == 0:
			print(“buzz”)

		else:
			print(num)

#Note: Need to put more granular conditional to account for numbers like 15, etc. 
