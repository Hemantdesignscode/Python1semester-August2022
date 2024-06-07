# CSC 1301 - program_08
# Author : Hemant Kosaraju
# Email : hkosaraju2@student.gsu.edu
# Section : Section 014 & CRN 84157

''' FIRST FUNCTION '''
variable_range = int(input('Enter an integer: ')) # Put variable for input outside of the function then call it through the parameter as an input value which is type casted to an integer in this line

def makelist(variable_range):
    x = []
    for i in range(0, variable_range + 1):
        x.append(i) # The .append means to add the values within the range of the loop to the empty loop assigned to the variable
    print(x)

makelist(variable_range)

''' SECOND FUNCTION '''
first_paramter = int(input('Enter an integer: '))
second_paramter = int(input('Enter an integer: '))

def rocketcountdown(first_parameter, second_parameter):
    a = []
    for i in range(second_parameter + 1,  first_parameter + 1):
        a.append(i)
    a.reverse() # Used to reverse the order of the list 
    a.append( 'We have lift off!')
    print(a)

rocketcountdown(first_paramter, second_paramter)

''' THIRD FUNCTION '''
num1_range = int(input('Enter an integer: '))
num2_range = int(input('Enter an integer: '))

def doubleloop(num1_range, num2_range):
    variable_list = []
    for i in range(0, num1_range):
        for item in range(0, num2_range):
            variable_list.append(f'{str(i)}:{str(item)}') # Appended using f-string for colon placement
    print(variable_list)

doubleloop(num1_range, num2_range)