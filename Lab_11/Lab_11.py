# CSC 1301 - Program 11
# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section: Section 014 and CRN 84157

import random

numbers_to_write_to_file = int(input("How many numbers are needed to write to the file: "))

test_file_write = open("test.txt", "w")

test_file_write.write("===========")
test_file_write.write(f"\n\nHow many numbers are needed to write to the file: {numbers_to_write_to_file} \n\n")

random.seed(1)

for _ in range(numbers_to_write_to_file):

    test_file_write.write(str(f"{random.randint(1,100)} "))
    

test_file_write.write("\n\n*****************************\n\n")

test_file_write.close()

prime_read = open("prime.txt", "w+")

random.seed(1)

def prime(numbers_to_write_to_file):
    if numbers_to_write_to_file > 1:
        for _ in range(2, int(numbers_to_write_to_file/2) + 1):
            if (numbers_to_write_to_file % _) == 0:
                return False
        else: 
            return True
    else:
        return False


prime_or_not = [random.randint(1,100) for _ in range(numbers_to_write_to_file)]

for _ in prime_or_not:
    if prime(_) == True:
        prime_read.write(str(_) + ' ')

prime_read.write("\n")

count = 0
for _ in prime_or_not:
    if prime(_) == True:
        count += 1
prime_read.write(f"\n{count} prime numbers found in this file")

prime_read.write("\n\n===========")

        
prime_read.close()