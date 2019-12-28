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

# Return the List of Sublists
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


#ATM PIN Code Validation
def isValidPIN(input_pin):
    length = len(input_pin)
    if length==4 or length==6 and input_pin.isdigit():
        return True
    else:
        return False

#Total Volume
# Given a list of boxes, create a function that returns the total volume of all those boxes combined together. 
# A box is represented by a list with three elements: length, width and height.
# For instance, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1]) 
# should return 266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.
def total_volume(lists):
    test=1
    for i in lists:
        test = test * i
    return volume

print(total_volume([1,2,3]))