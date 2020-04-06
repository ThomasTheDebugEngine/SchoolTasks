input_str = input("input main string: ")
pos_arr = input("input pos array: ")
neg_arr = input("input negative array: ")


def user_prompt():
    print("input here : ")
    user_input = str(input())
    is_valid_input(user_input)


def is_valid_input(inp_str):  # TODO add more cases for checking (easier in nested fashion)
    if len(inp_str) >= 1:
        find_unique(inp_str)
    else:
        print("String is invalid please try again")


def find_unique(clean_string):
    char_arr = []
    occur_arr = []

    clean_string = clean_string + " "  # for the loop to be able to index last element

    for i in range(0, len(clean_string) - 1):
        if clean_string[i] != clean_string[i+1]:
            char_arr.append(clean_string[i])

    occur_count = 1
    for c in range(0, len(clean_string) - 1):
        if clean_string[c] == clean_string[c+1]:
            occur_count = occur_count + 1
        else:
            occur_arr.append(occur_count)
            occur_count = 1

    combine_arrays(char_arr, occur_arr)


def combine_arrays(char_arr, occur_arr):
    combo_arr = []
    result = ""

    if len(char_arr) != len(occur_arr):
        print("ERROR: array has been corrupted")
        return 0
    else:
        for c in range(0, len(char_arr)):
            combo_arr.append(char_arr[c])
            combo_arr.append(occur_arr[c])

    for char in combo_arr:
        result = result + str(char)

    print(result)


user_prompt()
