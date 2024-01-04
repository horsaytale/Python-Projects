# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas
NATO_data=pandas.read_csv("nato_phonetic_alphabet.csv")
NATO_dataframe = pandas.DataFrame(NATO_data)

#Loop through rows of a data frame
# for (index, row) in NATO_dataframe.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     print(index)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
new_dict={row.letter:row.code for index,row in NATO_dataframe.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#METHOD 1
# continue_on=True
# while continue_on:
#     answer=input("Enter a word: ").upper()
#     try:
#         lst=[new_dict[alphabet] for alphabet in answer]
#     except:
#         print("Sorry only letters in the alphabet please.")
#     else:
#         print(lst)
#         continue_on = False

#METHOD2
def generate_machine():
    answer=input("Enter a word: ").upper()
    try:
        lst=[new_dict[alphabet] for alphabet in answer]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        generate_machine()
    else:
        print(lst)

generate_machine()