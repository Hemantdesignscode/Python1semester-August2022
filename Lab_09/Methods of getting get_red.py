# Method 1
dict = {"0":1, "1":0, "2":2, "3":3, "4":4,"5":5, "6":6, "7":7, "8":8, "9":9
,"a":10, "b":11, "c":12, "d":13, "e":14, "f":15}

example = "ffaaff" # FF-red, AA-green, FF-Blue
# 15 * 16 + 15 = 240+15 = 255
# 10 * 16 + 10 = 170

def get_red(example):
    # str_red = example[0:2] # ff
    int_red = dict[example[0]]*16 + dict[example[1]] # 15
    return int_red

# Method 2
def get_red_version_2(example):
    return int(example[0:2], 16)

def run_test():
    # get_red(example)
    red = get_red(example)
    red2 = get_red_version_2(example)
    print(red)
    print(red2)

run_test()

