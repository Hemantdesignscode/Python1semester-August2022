# Author: Hemant Kosaraju
# Email: hkosaraju2@student.gsu.edu
# Section: Section 014 & CRN 84157

''' Purpose : Is to get the terms and definitions of the words in the dictionary
and use a def function to look up the word, another def function to add the word
, and finally a last def function to remove a word.''' 

''' Pre-condition: The user selecting one of three inputs and the word has to exist within the dictionary.  
Post-condition: The words searched in look up should be outputted with definition. 
The words added with their definition should be outputted with other words and definitions in the dictionary with the use of for statement. 
The words removed from the dictionary should be outputted and informed to the user that it has been removed along with optionally printing
the available words in the dictionary for the user and printing the list of keys:values after the user has selected one to remove.   '''

# Used a def main function along with; a def lookup_word, a def add_word_to_dict, and a def delete_in_dict

import unittest # importing a module called unittest

def lookup_word(my_dict): # This is the first def function for looking up a word/term
  Look_up = input('\nEnter the word you want to look up: ') # This is the Look_up variable, assigned to get user input to look up the definition for the word/term
  if Look_up in my_dict: # Checking if the user input(Look_up) is included in the dictionary called my_dict 
    print(f'\n{Look_up}: {my_dict[Look_up]}') # This statement prints a formatted string (f-string) to output the word/term along with the value(definition) the word/term is assigned with
  else: # This tells the interpreter what to do if the user input(Look_up) is not included within the dictionary called my_dict
    print(f'\nThis word does not exist within the database.') # prints the formatted string (f-string) if the else: statement is being executed
  print('\nThanks for using MyDictionary.\n') # Prints at the end of the whole statement whether the if or else statement is executed


def add_word_to_dict(my_dict): # This is the second def function for adding a word/term along with its definition to the existing dictionary called my_dict
  Add_word = input('\nEnter the word you want to add: ') # This is the Add_word variable, assigned to get user input for another new word/term
  Please_Define = input('\nPlease add a definition for it: ') # This is the Please_Define variable, assigned to get the user input for the definition corresponding to the user input for Add_word
  my_dict[Add_word] = Please_Define # This is adding the key(word) and the value(definition) to the existing my_dict dictionary
  print('\nHere is all the words I have: ') # This statement prints the string "Here is all the words I have: "
  for item in my_dict: # This is a for-in statement which is saying for every item in my_dict execute the body of the for loop until the amount of iterations have been met
    print(f'\n{item}: {my_dict[item]}.\n') # This is the body of the loop which is going to output the words and definitions in the my_dict dictionary including the new word and definition that have been added, using a formatted string and print statement


def delete_in_dict(my_dict): # This is the last def function for removing 
  for item in my_dict: # This is a for loop that iterates all the keys and values in the my_dict dictionary
    print(f'{item}: {my_dict[item]}') # This is the body of the for loop that presents the user to see which words can be selected to remove from the list
  word_you_remove = input('\nEnter the word you want to remove: ') # This is the word_you_remove variable, assigned to get the user input for the word/term the user would like to remove
  if word_you_remove in my_dict: # This if statement checks to see if the word being removed is within my_dict dictionary
    del my_dict[word_you_remove] # This is the body of the if statement and the word user inputs would be deleted using del keyword
    print(f'\n{word_you_remove} - was removed from the dictionary.\n') # Prints the word informing the user that the word/term was removed
  print('Remaining words are: ') # prints the statement informing the user what the remaining words are 
  for item in my_dict: # Another for statement to print which words are remaining after the removal of the user inputted word/term
    print(f'{item}: {my_dict[item]}') # prints the remaining words after the user inputted word/term is taken out
  else: # This is an else statement if the word_you_remove is not within the dictionary my_dict, then this statement executes 
    print('\nuh typo ? I don\'t have this word in my database.\n') # This statement is printed when the else statement executes

def main(): # This is def main() function

# initial dictionnary
  my_dict = {
    "Variable":
    "a quantity or function that may assume any given value or set of values.",
    "Array":
    "an arrangement of a series of terms according to value, as from largest to smallest.",
    "Function":
    "a set of ordered pairs in which none of the first elements of the pairs appears twice."
  }
# your code here 
  print('\t *** dictionary *** \n') # This statement prints: *** dictionary ***
  print('Welcome to My Dictionary! What can I do for you? \n') # This statement prints: Welcome to My Dictionary! What can I do for you? 

  print('  1. Search for a word') # This statement prints/outputs: 1. Search for a word
  print('  2. Add a new word') # This statement prints/outputs: 2. Add a new word
  print('  3. Remove a word') # This statement prints/outputs: 3. Remove a word

  num_choice = int(input('\nPlease type your choice number: ')) # This variable called num_choice is the user input type-casted as an integer

  
  if num_choice == 1: # If statement saying if the user input for num_choice is 1 then next line
    lookup_word(my_dict) # Calls the function def lookup_word and the body of the function executes
  
  if num_choice == 2: # If statement saying if the user input for num_choice is 2 then next line
    add_word_to_dict(my_dict) # Calls the function def add_word_to_dict and the body of the function executes
  
  if num_choice == 3: # If statement saying if the user input for num_choice is 3 then next line
    delete_in_dict(my_dict) # Calls the function def delete_in_dict and the body of the function executes
  

# Testing code
class TestDictFunctions(unittest.TestCase):

  def test_search_word_success(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = test_dict["Variable"]
    expected = lookup_word(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_search_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = "N/A"
    expected = lookup_word(test_dict, "Array")
    self.assertEqual(actual, expected)

  def test_add_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Array":
      "an arrangement of a series of terms according to value, as from largest to smallest.",
    }
    expected = add_word_to_dict(
      test_dict, "Array",
      "an arrangement of a series of terms according to value, as from largest to smallest."
    )

    self.assertEqual(actual, expected)

  def test_add_word_duplicate(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    actual = {
      "Variable":
      "a quantity or function that may assume any given value or set of values.",
      "Variable(2)": "temporary value assignment"
    }
    expected = add_word_to_dict(test_dict, "Variable",
                                "temporary value assignment")
    self.assertEqual(actual, expected)

  def test_delete_word_sucess(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = {}
    actual = delete_in_dict(test_dict, "Variable")
    self.assertEqual(actual, expected)

  def test_delete_word_no_result(self):
    test_dict = {
      "Variable":
      "a quantity or function that may assume any given value or set of values."
    }
    expected = test_dict
    actual = delete_in_dict(test_dict, "Array")
    self.assertEqual(actual, expected)


#uncomment to run tests
# unittest.main()

main()
