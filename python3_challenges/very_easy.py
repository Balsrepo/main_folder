# All titles of the challenges are commented on top of the functions
# Functions can be called and return statements can be replace with print statement 


#Return the sum of two numbers
def sum_of_2_nums(a,b):
    return a+b 

#Return the Next Number from the Integer Passed
def return_next_number(num):
    return num+1

#Convert Minutes into Seconds
def mins_to_secs(mins):
    return mins*60

#Area of Triangle #where b: base h: height
def area_of_traingle(b,h):
    return (b*h)/2

#Convert Hours into Seconds
def hours_into_secs(hours):
    return 3600*hours # i.e. 1 hour is equal to 3600 seconds

#Maximum Edge of a Triangle
def max_edge_of_traingle(a,b):
    return (a+b)-1

#Return the Remainder from Two Numbers
def remainder_from_two_numbers(num1,num2):
    return num1%num2

#Return the First Element in a List
#Duplicate
##Return the Last Element in a List ##just replace return statement input_list[0] with input_list[-1]
def first_element_in_a_list(input_list):
    return input_list[0] #

#To the Power of ____
def power_of_(num,power):
    return num**power

#The Farm Problem
#chicken= 2 legs, cows= 4 legs, pigs= 4 legs
def farm_problem(no_of_chicken,no_of_cows,no_of_pigs):
    return (no_of_chicken*2) + (no_of_cows*4) + (no_of_pigs*4)

#String to Integer and Vice versa
def string_to_integer(inp):
    return int(inp) # or str(inpt) #for integer to string

#Is the Number Less than or Equal to Zero
def less_than_or_equal_to_zero(num):
    return True if num<=0 else False

#Find the Largest Number in a List
def largest_number_in_a_list(input_list):
    ## can also be used for minimum number in a list if return and if statements are replaced
    return max(input_list) ## min(input_list)
    ## using for loop 
    # maximum = 0
    # for i in input_list:
    #     if i > maximum: ## if i < maximum:
    #         maximum = i
    # return maximum

#Concatenating two Integer Lists
def concatenation(list1,list2):
    return list1+list2

#Convert Hours and Minutes into Seconds
def hours_and_minutes_to_seconds(hours,minutes):
    return (hours*3600) + (minutes*60)

#Profitable Gamble
def profitable_gamble(prob,prize,pay):
    return True if (prob*prize)>pay else False

#Check if an Integer is Divisible by Five
#Duplicate
##Multiple of 100
##replace 5 with 100 to check if given number is multiple by 100
def check_if_divisible_by_five(num):
    return num%5==0 #return statement used without if else statement

#Difference of Max and Min Numbers in a List
#Duplicate
#Maximum Difference
def difference_of_max_and_min(input_list):
    return max(input_list) - min(input_list)

#Testing K ^ K == N ## ^ exponentiation symbol 
def ktok(k,n):
    return (k**k)==n

#Compare Strings by Count of Characters
