import json
import random

def get_list_from_json(json_file_name):
    with open(json_file_name) as selected_json_file:
        names = json.load(selected_json_file)
    return names
        
def draw(name_lists, total_prize_no):
    count = 1
    selected_list = []
    while(total_prize_no >= 1):
        selected_index = random.randint(1, len(name_lists)) - 1
        if selected_index in selected_list:
            continue
        else:
            try:
                selected_list.append(selected_index)
                print(f"{count}: {name_lists[selected_index]}")
                total_prize_no -= 1
                count += 1
            except ValueError as e:
                print(f"{selected_index}")

def console_request():
    is_break = False
    while not is_break:
        print("-----------------------------------\n")
        print("1. Malays\n")
        print("2. Non-Malays\n")
        list_input = int(input("Which Category List You Want to Roll: "))
        max_selection = int(input("\nHow many people want to roll: "))
        if list_input == 1:
            print("--------------------")
            draw(get_list_from_json('malay-name-list.json'), max_selection)
        elif list_input == 2:
            print("--------------------")
            draw(get_list_from_json('name-list.json'), max_selection)
        else:
            print(f"Not supported input: {list_input}")
        continue_input = str(input("--------------------\nContinue?: (Y) or (N): "))
        is_break = False if continue_input.upper() == "Y" else True

def main():
    console_request()

if __name__ == "__main__":
    main()