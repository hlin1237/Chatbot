import json
import re
from user import read_json_file

bot_template = "Bot : {0}"

def trainer_chat():
    while True:
        question = raw_input("Trainer: ")
        if question.lower() == "bye":
            print(bot_template.format("Thank you for teaching me"))
            break
        
        
        matches = check_matches(question, 'dictionary.json')
        best_matches_list = best_matches(question, 'dictionary.json')
        if not matches:
            if not best_matches_list:
                choice = raw_input("Bot: The question '%s' doesn't exist. Would you like to input an answer? (yes/no): " % question)

                if choice.lower() == "yes":
                    answer = raw_input("Trainer: Enter the response for the question: ")
                    write_json_file(question, answer, 'dictionary.json')
                elif choice.lower() == "no":
                    print("Bot: Okay, moving on.")
        else:
            choice = raw_input(bot_template.format("It seems like an response was found, would you like to add?"))
            if choice == "yes":
                answer = raw_input("Trainer: Enter the response for the question: ")
                write_json_file(question, answer, 'dictionary.json')
            elif choice.lower() == "no":
                print("Bot: Okay, moving on.")
        

# Edited the dictionary.json file
def write_json_file(question, answer, file_path):
    # Read existing data from the JSON file
    data_file = read_json_file(file_path)

    # Get the existing values for the key or an empty list if the key doesn't exist
    values = data_file.get(question.lower(), [])

    # Add the new answer to the list of values
    values.append(answer)

    # Update the data with the new values
    data_file[question.lower()] = values

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        json.dump(data_file, file, indent=2)


def check_matches(message, file_path):
    data_file = read_json_file(file_path)

    # Check if the question existed in the database or not
    for key in data_file:
        if message.lower() == key.lower():
            return True

    return False

def best_matches(message, file_path):
    
    pattern = re.escape(message) + ".*"
    data_file = read_json_file(file_path)

    # Find all keys that match the pattern
    matches = [key for key in data_file if re.match(pattern, key, re.IGNORECASE)]

    return matches