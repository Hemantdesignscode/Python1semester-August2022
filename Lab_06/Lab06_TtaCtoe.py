# CSC 1301 - Python Lab 6
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section & CRN: Section 014 and CRN 84157


def main():
    
    Row0 = (input("Row0>"))

    Row1 = (input("Row1>"))

    Row2 = (input("Row2>"))

    if Row0[0] == Row1[1] == Row2[2] == 'X':
        print('X IS GOOD IN DIAGONAL')
    
    elif Row0[2] == Row1[1] == Row2[0] == 'X':
        print('X IS GOOD IN DIAGONAL')

    elif Row0[0] == Row1[1] == Row2[2] == 'O':
        print('O IS GOOD IN DIAGONAL')
    
    elif Row0[2] == Row1[1] == Row2[0] == 'O':
        print('O IS GOOD IN DIAGONAL')

    elif Row0[0] == Row0[1] == Row0[2] == 'X':
        print('X IS GOOD IN HORIZONTAL')
    
    elif Row1[0] == Row1[1] == Row1[2] == 'X':
        print('X IS GOOD IN HORIZONTAL')
    
    elif Row2[0] == Row2[1] == Row2[2] == 'X':
        print('X IS GOOD IN HORIZONTAL')
    
    elif Row0[0] == Row0[1] == Row0[2] == 'O':
        print('O IS GOOD IN HORIZONTAL')
    
    elif Row1[0] == Row1[1] == Row1[2] == 'O':
        print('O IS GOOD IN HORIZONTAL')
    
    elif Row2[0] == Row2[1] == Row2[2] == 'O':
        print('O IS GOOD IN HORIZONTAL')
    
    elif Row0[0] == Row1[0] == Row2[0] == 'X':
        print('X IS GOOD IN VERTICAL')
    
    elif Row0[1] == Row1[1] == Row2[1] == 'X':
        print('X IS GOOD IN VERTICAL')

    elif Row0[2] == Row1[2] == Row2[2] == 'X':
        print('X IS GOOD IN VERTICAL')
    
    elif Row0[0] == Row1[0] == Row2[0] == 'O':
        print('O IS GOOD IN VERTICAL')
    
    elif Row0[1] == Row1[1] == Row2[1] == 'O':
        print('O IS GOOD IN VERTICAL')

    elif Row0[2] == Row1[2] == Row2[2] == 'O':
        print('O IS GOOD IN VERTICAL')
        
    else: 
        print('THIS IS TIE')

main()