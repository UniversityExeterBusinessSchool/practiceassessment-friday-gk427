Copy and insert your code here

# Question 1 - Data Processing and Loops
# You are given a string representing customer reviews. Use a for loop to process the text and count occurrences of specific keywords.
# Your allocated keywords are determined by the first and last digit of your SID.
# Count and store occurrences of each keyword in a dictionary called keyword_counts.
 
customer_reviews = """The product is well-designed and user-friendly. However, I experienced some issues with durability. The customer service was helpful, 
but I expected a faster response. The quality of the materials used is excellent. Overall, the purchase was satisfactory."""

# Keywords dictionary
keywords = {
    0: 'user-friendly',
    1: 'helpful',
    2: 'durability',
    3: 'response',
    4: 'satisfactory',
    5: 'quality',
    6: 'service',
    7: 'issues',
    8: 'purchase',
    9: 'materials'
}

# Write your code to process the text and count keyword occurrences

keyword_count = {} 

allocated_key = [7,8]

for i in allocated_key:
    start_loc = customer_reviews.find(keywords[i])
    end_loc = start_loc + len(keywords[i])
    keyword_count[start_loc] = end_loc
    
print(keyword_count)

#OUTPUT {76: 82, 230: 238}



# Question 2 - Business Metrics
# Scenario - You work in an online retail company as a business analyst. Your manager wants weekly reports on financial performance, including:
# Gross Profit Margin, Inventory Turnover, Customer Retention Rate (CRR), and Break-even Analysis. Implement Python functions 
# that take relevant values as inputs and return the computed metric. Use the first two and last two digits of your ID number as input values.

# Insert first two digits of ID number here:74
# Insert last two digits of ID number here:38

# Write your function for Gross Profit Margin
def calc_gross_profit_margin(revenue, cost_of_goods_sold):
    if cost_of_goods_sold != 0:
        gross_profit_margin = (revenue-cost_of_goods_sold)/(revenue)*100            #added if condition to give zero if the argument is zero
    else:
        gross_profit_margin = 0
        
    return gross_profit_margin
# Write your function for Inventory Turnover
def calc_inventory_turnover(cost_of_goods_sold, average_inventory):
    if average_inventory != 0:
        inventory_turnover = (cost_of_goods_sold)/(average_inventory)
    else:
        inventory_turnover = 0
        
    return inventory_turnover
# Write your function for Customer Retention Rate (CRR)
def calc_customer_retention_rate(retained_customers, starting_customers):
    if starting_customers != 0:
        customer_retention_rate = (retained_customers)/(starting_customers) * 100
    else:
        customer_retention_rate = 0

    return customer_retention_rate
# Write your function for Break-even Analysis
def calc_breakeven_analysis(fixed_cost, contribution_margin_per_unit):
    if contribution_margin_per_unit != 0:
        breakeven_analysis = (fixed_cost)/(contribution_margin_per_unit)
    else:
        breakeven_analysis = 0

    return breakeven_analysis
# Call your functions here

value1 = 74   #input value from first two digits of SID
value2 = 38   #input value from last two digits of SID

print(f'Gross Profit Margin for the input value is {calc_gross_profit_margin(value1,value2):.2f} %')
print(f'Inventory Turnover for the input value is {calc_inventory_turnover(value1,value2):.2f} units')
print(f'Customer Retention Rate for the input value is {calc_customer_retention_rate(value1,value2):.2f} %')
print(f'Break-Even Anaysis for the input value is {calc_breakeven_analysis(value1,value2):.2f} units')

#OUTPUT 
Gross Profit Margin for the input value is 48.65 %
Inventory Turnover for the input value is 1.95 units
Customer Retention Rate for the input value is 194.74 %
Break-Even Anaysis for the input value is 1.95 units





# Question 3 - Forecasting and Regression
# A logistics company has gathered data on delivery costs and shipment volumes. The table below provides different costs and their corresponding shipment volumes.
# Develop a linear regression model and determine:
# 1. The optimal delivery cost that maximizes profit
# 2. The expected shipment volume when the cost is set at £68

"""
Delivery Cost (£)    Shipment Volume (Units)
-------------------------------------------
25                  500
30                  480
35                  450
40                  420
45                  400
50                  370
55                  340
60                  310
65                  290
70                  250
"""

# Write your regression model code here

import numpy as np
from sklearn.linear_model import LinearRegression

#storing the data in varibles as arrays
cost = np.array([25,30,35,40,45,50,55,60,65,70]).reshape(-1,1)    #to convert the array into a 1d array with one column and multiple rows 
volume = np.array([500,480,450,420,400,370,340,310,290,250])

#calling the regression function and implementing calculation
model = LinearRegression()
model.fit(cost,volume)

#to find the optimal delivery cost

slope = model.coef_[0]            #to store the slope
intercept = model.intercept_      #to store the y intercept


optimal_cost = -intercept/(2*slope)     #adding formula for finding the optimal cost

#to find the expected shipment volume when price is £68

predicted_volume = model.predict(np.array([[68]]))[0]      #using predict function to predict value from the array and using [0] to extract only the first value

#printing the final outputs
print(f'Optimal Delivery Cost is {optimal_cost:.2f}£')
print(f'Expected Shipment Volume at price £68 is {predicted_volume:.2f} units')

#OUTPUT
Optimal Delivery Cost is 58.29£
Expected Shipment Volume at price £68 is 267.94 units

# Question 4 - Debugging and Data Visualization

import random as rand           #calling module random and giving alias as rand
import matplotlib.pyplot as plt     # corrected spelling of matplotlib.pyplot

# Generate 100 random numbers between 1 and student ID number
your_ID=input("Enter your Student ID: ")
max_value = int(your_ID)
random_numbers = [rand.randint(1, max_value) for i in range(100)]     #changed random to rand , changed starting index to 1, corrected syntax for list comprehension

# Plotting the numbers in a histogram
plt.hist(random_numbers, bins=10, edgecolor='blue', alpha=0.7, color='red')    #changed histogram to hist, bin-->bins, 
plt.title("Histogram of 100 Random Numbers")               #changed = sign and added braces
plt.xlabel("Value Range")                              #changed = sign and added braces
plt.ylabel("Frequency")                          #changed = sign and added braces
plt.grid(True)                   #changed the quotation marks
plt.show()        #plt.show() doest require an argument

