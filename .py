# Instruct a user to input an integer greater than 5 and less than or equal to 10 and store the input as an integer value in a variable.
# Otherwise, output the message 'You did not enter a value between 5 and 10'
# If the input number is greater than 5 and less than or equal to 10, your code will use a 'for' loop in order that will:
# Output the integers from 0 up to the input value
# Within the 'for' loop, if 10 times the current value of the loop variable exceeds a value of 70, use a break statement to terminate the 'for' loop





inval=int(input('Input an integer greater than 5 and less than or equal to 10: '))
# your code goes here
# In order to ensure an exact match with the answer checker, please use the following
# code in the event that the user enters an invalid value:
#     print('You did not enter a value between 5 and 20')
sum = 0
if inval > 5 and inval <= 1:
    True
for x in range(0, inval):
	if x > 70:
		print(x)													
	break