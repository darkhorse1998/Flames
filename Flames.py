
import string

print("Welcome! Let's play FLAMES!")
store = string.ascii_lowercase
#print(store)

total_remain = 0

#function to remove spaces among different parts of the name
def remove_spaces(name): 
    name = name.replace(" ", "")
    return name

#function to make the names in lowercase
def make_lower_case(name):
    name = name.lower()
    return name

#function to calculate the length of the string
def string_length(name):
    return len(name)

#function to convert string to array format
"""def name_split(name):
    name = list(name)"""

name_1 = input("\nEnter the first name:  ")
name_2 = input("\nEnter the second name:  ")

name_1 = remove_spaces(name_1)
name_2 = remove_spaces(name_2)
#print(name_1, name_2)

name_1 = make_lower_case(name_1)
name_2 = make_lower_case(name_2)
#print(name_1, name_2)

l1 = string_length(name_1)
l2 = string_length(name_2)
#print(l1,l2)

for i in range(0,26):
    if store[i] in name_1:
        count_1 = name_1.count(store[i])
    else:
        count_1 = 0

    if store[i] in name_2:
        count_2 = name_2.count(store[i])
    else:
        count_2 = 0
    loop_count = abs(count_1 - count_2)
    total_remain +=loop_count
#print(total_remain)

test_word = "flames"*total_remain*100
#print(len(test_word))

collected = []
#print(len(collected))
last_index = 0
#print(test_word[last_index + total_remain - 1])


if(len(collected)<5):
    for i in range(0,5):
    #total_remain = len(test_word)%total_remain
        cut_out = test_word[last_index + total_remain - 1]
        collected.append(cut_out)
        #print(collected)
        last_index = test_word.find(cut_out)
        if cut_out in test_word:
            test_word = test_word.replace(cut_out, "")
        
        
#print(collected)
original = ["f","l","a","m","e","s"]
for i in range(0,6):
    if original[i] not in collected:
        #print(original[i])
        final_output = original[i]


#initial_level_completed


if final_output == "f":
    print("It's FRIENDSHIP!")
elif final_output == "l":
    print("It's LOVE!")
elif final_output == "a":
    print("It's AFFECTION!")
elif final_output == "m":
    print("It's MARRIAGE!")
elif final_output == "e":
    print("It's ENMITY")
elif final_output == "s":
    print("It's SIBLINGS")

    
input("Press Enter to EXIT")

















    


