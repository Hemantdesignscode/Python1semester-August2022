#Prolog
#Author: Hemant Kosaraju
#Email: hkosaraju2@student.gsu.edu
#Section: CSC 1301, Lab 02, CRN 84157

'''
  Purpose: 
      convert inches to feet, using fact that there are 12 inches in 1 foot
  Pre-conditions (input): 
      number of inches (floating point)
  Post-conditions (output): 
      number of feet, floating point with 2 decimals rounded
'''

def main():
# Design and implementation

#  1.  Output a message to identify the program, and a blank line
    print("Conversion of inches to feet")
    print()

#  2.  Input amount of inches from user

    inches = float(input("How many inches? "))

#  3.  Calculate number of feet
    # 12 inches in one foot
    feet = inches / 12 
    #This code should have been feet to inches not inches to feet 

#  4. Output resulting feet and given number of inches
    print()
    print(inches, "inches is {:.2f} feet".format(feet))

main()
# end of program file
'''
Syntax Errors

    1. At Line 24, there was an int in front of the inches. At line 34, there was a colon after the main() end function.

    2. Error for line 24 syntax error:
        int inches = float(input("How many inches? "))
            ^^^^^^
        SyntaxError: invalid syntax

    Error for line 34 syntax error:
        main():
              ^
        SyntaxError: invalid syntax

    3. I deleted the integer (int) before the inches, for line 24 to correct the syntax error
       I deleted the colon (:) after the main() end function, for line 34 to correct the syntax error 

Semantics(Logic) Error

    4. The semantics(logic) error is that feet equals inches by 12 instead of the inches being divided by 12, for example, if you have 36 inches you have to convert to feet you divide by 12 to get 3 feet if you multiply by 12 however, the answer will be 432 feet which is not correct 

    5. The semantics(logic) error is on line 28 of the program

    6. I fixed the semantics(logic) error by changing the multiplication operator * for feet = inches * 12, to a division operator / for feet = inches / 12
'''