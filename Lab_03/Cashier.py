# Prolog
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section: CSC 1301 - crn 84157 - Section 014
'''
Purpose: 
calculate the change you are due when you buy an item in a store
Pre-conditions (input): 
money given to the cashier(cost of item)
Post-conditions (output): 
 change user get back from the cashier(dollars, quarters, dimes, nickels and 
pennies)
'''
def main():
    # Design and implementation
    # 1. Output a message to identify the program, and a blank line
    print("Conversion of change to dollars, quarters, dimes, nickels and pennies")
    print()
    # 2. Input amount of change from user
    cost = float(input("Cost of an item?: "))
    amt = float(input("Amount given to the cashier?: "))

    #For math module - import math
    import math

# 4. Output resulting change and given cost of an item
    # we are trying to find the change & then sorting the change based on dollars,quarters,dimes,nickels,& pennies
    change = amt - cost 
    dollars = int(change/1)
    quarters = int((change-dollars)/.25)
    dimes = int((change-dollars-quarters*.25)/.10)
    nickels = int((change-dollars-quarters*.25-dimes*.10)/.05)
    pennies = float((change-dollars-quarters*.25-dimes*.10-nickels*.05)/.01)
    
    #The print function is outputting each variable on the screen based on the previous math calculations for each variable
    print("Dollars = ",dollars, end=' ')
    print("Quarters = ",quarters, end=' ')
    print("Dimes = ",dimes, end=' ')
    print("Nickels = ",nickels, end=' ')
    print("Pennies = %.0f"% pennies, end=' ')
#print(cost , "cost is {:.2f} change".format(change))
main()
# end of program file

