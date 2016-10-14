'''
Python Homework with Chipotle data
https://github.com/TheUpshot/chipotle
'''

'''
BASIC LEVEL
PART 1: Read in the file with csv.reader() and store it in an object called 'file_nested_list'.
Hint: This is a TSV file, and csv.reader() needs to be told how to handle it.
      https://docs.python.org/2/library/csv.html
'''

import csv

# specify that the delimiter is a tab character
# make 'file_nested_list' = list of rows



'''
BASIC LEVEL
PART 2: Separate 'file_nested_list' into the 'header' and the 'data'.
'''




'''
INTERMEDIATE LEVEL
PART 3: Calculate the average price of an order.
Hint: Examine the data to see if the 'quantity' column is relevant to this calculation.
Hint: Think carefully about the simplest way to do this!
'''

# count the number of unique order_id's
# note: you could assume this is 1834 since that's the maximum order_id, but it's best to check

# create a list of prices
# note: ignore the 'quantity' column because the 'item_price' takes quantity into account
# strip the dollar sign and trailing space

# calculate the average price of an order and round to 2 digits
# $18.81


'''
INTERMEDIATE LEVEL
PART 4: Create a list (or set) of all unique sodas and soft drinks that they sell.
Note: Just look for 'Canned Soda' and 'Canned Soft Drink', and ignore other drinks like 'Izze'.
'''

# if 'item_name' includes 'Canned', append 'choice_description' to 'sodas' list
sodas = []


# equivalent list comprehension (using an 'if' condition)


# create a set of unique sodas



'''
ADVANCED LEVEL
PART 5: Calculate the average number of toppings per burrito.
Note: Let's ignore the 'quantity' column to simplify this task.
Hint: Think carefully about the easiest way to count the number of toppings!
'''

# keep a running total of burritos and toppings


# calculate number of toppings by counting the commas and adding 1
# note: x += 1 is equivalent to x = x + 1


# calculate the average topping count and round to 2 digits
# 5.40


'''
ADVANCED LEVEL
PART 6: Create a dictionary in which the keys represent chip orders and
  the values represent the total number of orders.
Expected output: {'Chips and Roasted Chili-Corn Salsa': 18, ... }
Note: Please take the 'quantity' column into account!
Optional: Learn how to use 'defaultdict' to simplify your code.
'''

# start with an empty dictionary
chips = {}

# if chip order is not in dictionary, then add a new key/value pair
# if chip order is already in dictionary, then update the value for that key


# defaultdict saves you the trouble of checking whether a key already exists



'''
BONUS: Think of a question about this data that interests you, and then answer it!
'''
