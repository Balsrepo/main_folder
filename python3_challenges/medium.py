#FizzBuzz Interview Question

#List of Multiples
def list_of_multiples(num, no_of_multiples):
    return [num*i for i in range(1,no_of_multiples+1)]

#Calculate the Profit
# You work for a manufacturer and have been asked to calculate the total profit made on the sales of a product. 
# You are given a dictionary containing the cost price per unit (in dollars), 
# sell price per unit (in dollars), and the starting inventory.
# Return the total profit made, rounded to the nearest dollar. 
# Assume all of the inventory has been sold.
def calculate_profit(inp_dict):
    return inp_dict["inventory"]*(inp_dict["sell_price"] - inp_dict["cost_price"])


#How Many Solutions Does This Quadriatic Have?

#All Occurrences of an Element in a List
# Create a function that returns the indices of all occurrences of an item in the list.
def get_indices(inp_list, search_item):
    return [lambda search_item: if search_item in inp_list ]

print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))