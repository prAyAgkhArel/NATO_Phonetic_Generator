# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

dataframe = pandas.read_csv("nato_phonetic_alphabet.csv")
print(f"Dataframe:\n {dataframe}")
dict_of_dataframe = {row.letter:row.code for (index, row) in dataframe.iterrows()}
print(f"Dictionary of dataframe: \n{dict_of_dataframe}")

def generate_phonetic_code():
    user_input = input("Enter a word.\n").upper()

    try:
        code_list = [dict_of_dataframe[letter] for letter in user_input]
    except KeyError:
        print("You are allowed to enter letters only.")
        generate_phonetic_code()
    else:
        print(code_list)

generate_phonetic_code()