#Get the Century
## All dates will be between 1000 and 2010
def get_century(year):
    # can be achieved without using nested if statements 
    # use math.ceil inbuilt function
    from math import ceil
    return str(ceil(year/100)) +" century"
    # if year == 1000:
    #     return "10th Century"
    # elif year in range(1000,1100):
    #     return "11th Century"
    # elif year in range(1100,1200):
    #     return "12th Century"
    # elif year in range(1200,1300):
    #     return "13th Century"
    # elif year in range(1300,1400):
    #     return "14th Century"
    # elif year in range(1400,1500):
    #     return "15th Century"
    # elif year in range(1500,1600):
    #     return "16th Century"
    # elif year in range(1600,1700):
    #     return "17th Century"
    # elif year in range(1600,1700):
    #     return "17th Century"
    # elif year in range(1700,1800):
    #     return "18th Century"
    # elif year in range(1800,1900):
    #     return "19th Century"
    # elif year in range(1900,2000):
    #     return "20th Century"
    # elif year in range(2000,2010):
    #     return "21st Century"
    # else:
    #     return "Invalid Year"


#Is the Number Symmetrical?
def check_symmetrical(num):
    temp1 = list(str(num))[::-1] #reverses the given number and converts
    temp2 = list(str(num)) #converts the given number into a list of strings
    return temp1==temp2  #can be acheived in one line : return list(str(num))[::-1] == list(str(num))

#Equality of 3 Values
def equality_of_3_values(a,b,c):
    eq,inp_list=0,[a,b,c]
    for i in inp_list:
        eq=inp_list.count(i)
    return eq
    
#Is the Word an Isogram?
def isogram(input_string):
    pass

#! Return the List of Sublists
# Write a function that takes three arguments (x, y, z) and returns a list containing x sublists (e.g. [[], [], []]), each containing y number of item z.
# x Number of sublists contained within the main list.
# y Number of items contained within each sublist.
# z Item contained within each sublist.
def list_of_sublists(x,y,z):
    import numpy as np
    arr = np.zeros([x,y])
    arr = arr.tolist()
    for i in range(x):
        for j in range(y):
            arr[i][j] = z
    return arr

#Remove Every Vowel from a String
def remove_vowel_from_string(input_string):
    vowels = """aeiouAEIOU""" # works also with capitalized letters
    removed_vowels = ""
    for i in input_string:
        if i not in vowels:
            removed_vowels = removed_vowels + i
    return removed_vowels

#Return the Index of All Capital Letters
def index_of_all_capital_letters(input_letters):
    indexes=[]
    for i in range(len(input_letters)):
        if input_letters[i].isupper():
            indexes.append(i)
    return indexes

#Snail Race


#Count Letters in a Word Search
def count_letters_in_word_search(input_list,word_to_count):
    import itertools
    return list(itertools.chain(*input_list)).count(word_to_count)
    #or we can use loops to create a flat list from all sublists and get the count from flat list


#ATM PIN Code Validation
def isValidPIN(input_pin):
    length = len(input_pin)
    if length==4 or length==6 and input_pin.isdigit():
        return True
    else:
        return False #can be written in one line return statement

#!Total Volume
# Given a list of boxes, create a function that returns the total volume of all those boxes combined together. 
# A box is represented by a list with three elements: length, width and height.
# For instance, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1]) 
# should return 266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.
def total_volume(*lists):

    def test(listss):
        test=1
        for i in listss:
            test = test * i
        return test

    volume = 0
    for i in lists:
        volume = volume + test(i)
    return volume


#Calculate the Median
def median(input_list):
    from math import ceil
    in_list=sorted(input_list)
    list_length = len(in_list) 
    middle = list_length/2
    if list_length%2==0:
        print(list_length%2)
        return (in_list[int(middle)] + in_list[int(middle)-1])/2
    else:
        return (in_list[ceil(middle)])
        

#Positive Count / Negative Sum
def post_count_and_negative_sum(input_list):
    pos_count , negative_sum = 0 , 0
    for i in input_list:
        if i > 0:
            pos_count = pos_count + 1
        else:
            negative_sum = negative_sum + i
    return pos_count, negative_sum
    

#Remove Duplicates from a List
def remove_dups(input_list):
    # return list(set(input_list)) #one line way to remove duplicates
    for i in input_list:
        if input_list.count(i) >= 2:
            input_list.remove(i)
    return input_list


#Count the Arguments
def count_arguments(*inps):
    return len(inps)

#Narcissistic Numbers
def narcissistic_numbers(inp):
    digits = str(inp)
    temp = 0 
    for i in digits:
        temp = int(i)**len(digits) + temp  
    return True if temp == inp else False

#!First and Last Index
# def first_last_index(inp_list,letter):
#     try:
#         return list(inp_list).index(letter)
#     except ValueError:
#         return None

# print(first_last_index("hello","d"))


#Sort Numbers in Descending Order
def sort_descending(numbers):
    pass