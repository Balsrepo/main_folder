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

#Return the List of Sublists
def list_of_sublists(list_of_lists):
    pass

#Return the Index of All Capital Letters

#Remove Every Vowel from a String

#Snail Race

#Count Letters in a Word Search