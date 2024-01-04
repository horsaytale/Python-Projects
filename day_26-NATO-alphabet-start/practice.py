import pandas

nato_data=pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dataframe=pandas.DataFrame(nato_data)
print(nato_data)
new_dict={details.letter:details.code for index,details in nato_dataframe.iterrows()}

print(new_dict)
is_on=True

# while is_on:
#     user_input=input("Enter a word: ").upper()
#     try:
#         new_list=[new_dict[alphabet] for alphabet in user_input]
#     except KeyError:
#         print("Sorry, please input the appropriate word.")
#     else:
#         print(new_list)
#         is_on=False

#METHOD-2
def generate_words():
    user_input = input("Enter a word: ").upper()
    try:
        lst=[new_dict[alphabet] for alphabet in user_input]
    except:
        print("Sorry, please input the right values.")
        generate_words()
    else:
        print(lst)

generate_words()