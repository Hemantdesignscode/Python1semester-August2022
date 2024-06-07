# Prolog
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section: CSC 1301 - Section 14 - CRN 84157
'''
Purpose:
    Phone number breakdown
        Pre-conditions (input): 
    (Enter the 10-digit phone number)
        Post-conditions (output): 
    Breakdown of phone number (area code, prefix, line number)
'''
def main():
    # Design and implementation
    # 1. Output a message to identify the program, and a blank line
    print()
    print("Breakdown of phone number to area code, prefix, line number")
    print()
    # 2. Input the 10-digit phone number

    Phone_number = int(input("Enter Phone number? "))
    Phone_number = str(Phone_number)

    # 3. Breakdown the phone number

    area_code = (Phone_number[0:3])
    prefix = (Phone_number[3:6])
    line_number = (Phone_number[6:10])

    # 4. Output breakdown to area code, prefix, line number

    print()
    print("Phone number is converted to area code=",area_code,", prefix=",prefix,",")
    print("line number=",line_number)
    print()
main()
# end of program file