# Purpose: Is to present user with restaurant menu choices and calculate total for their order, Pre-conditions: user has to select at least one menu item for a price to output, and Post-conditions: output a total bill for their food and a total bill after adding 20% tip
# CSC 1301 - Program 07
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section: Section 014 and CRN 84157

def main():


    print('\nWelcome to Dairy King\n')
    print('Please answer each questions with a y or n\n')
    GrilledCheese = input('Do you want a grilled cheese sandwich? ')
    print()
    Nachos = input('Do you want a serving of nachos? ')
    print()
    Chicken = input('Do you want a chicken sandwich? ')
    print()
    Hamburger = input('Do you want a Hamburger? ')
    print()
    if Hamburger == 'y':
        Cheeseburger = input('Do you want a cheese on that? ')
        print()
    HotDog = input('Do you want a hotdog? ')
    print()
    total_cost = 0

    dict = {'GrilledCheese':7, 'Nachos':5, 'Chicken':8,'Hamburger':8,'Cheeseburger':10,'HotDog':6}
    for item in dict:
        if GrilledCheese == 'y':
            total_cost += 7
        if Nachos == 'y':
            total_cost += 5
        if Chicken == 'y':
            total_cost += 8
        if Hamburger == 'y':
            total_cost += 8
            if Cheeseburger == 'y':
                total_cost += 2
        if HotDog == 'y':
            total_cost += 6
        print(f'The total for your food is ${total_cost:.2f}\n')
        tip = total_cost * .20
        total_cost_with_tip = total_cost + tip
        print(f'The total with 20% tip is ${total_cost_with_tip:.2f}\n')
        print('Thank you for your business!\n')
        break

main() 