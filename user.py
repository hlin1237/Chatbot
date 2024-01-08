import json
import random
from trainer import best_matches

#string template
bot_template = "Bot : {0}"

def users_chat():
    while True:
        #get the user's questions or statement
        user = raw_input("user:")
        
        if user == "bye":
            print(bot_template.format("Have a good day"))
            break
        
        bot_response = check_match(user ,'dictionary.json')
        print(bot_template.format(bot_response))
 
#Function to read a JSON file and return its content as a python data structure
def read_json_file(file_path):
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
    
# Function to check for a match in the JSON file and return a random response
def check_match(message, file_path):
    data_file = read_json_file(file_path)
    
    for key in data_file:
        if message.lower() == key.lower():
            return random.choice(data_file[key])
    
    new_key = best_matches(message, file_path)
    
    if new_key:
        one_key = random.choice(new_key)
        return random.choice(data_file[one_key])
        
        
    return random.choice(data_file["default"])
            
        




