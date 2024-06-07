# CSC 1301 - Program 09
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section: Section 014 & CRN 84157

dict = {'0':1,'1':0, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9,
'a':10, 'b':11, 'c':12, 'd':13, 'e':14, 'f':15}

# example = 'ffaaff'
example = input('\nEnter Hexadecimal: ')

def get_red(example):
    return int(example[0:2], 16)

def get_green(example):
    return int(example[2:4], 16)

def get_blue(example):
    return int(example[4:6], 16)

def id_protanopia(red): 
    if red < 64:
        return True
    else:
        return False

def id_deuteranopia(green):
    if green < 64:
        return True
    else:
        return False

def id_tritanopia(blue, red, green):
    if  blue > 0:
        if red > 230:
            if green > 220:
                return False
            else: 
                return True

def run_test():
    red = get_red(example)
    print(red)
    green = get_green(example)
    print(green)
    blue = get_blue(example)
    print(blue)
    print(id_protanopia(red))
    print(id_deuteranopia(green))
    print(id_tritanopia(blue, red, green))

run_test()