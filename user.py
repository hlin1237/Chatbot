import json

#string template
bot_template = "Bot : {0}"

def users_chat():
    while True:
        #get the user's questions or statement
        user = raw_input("user:")
        
        if user == "bye":
            print(bot_template.format("Have a good day"))
            break
        
        bot_response = check_match(user)
        print(bot_template.format(bot_response))
def check_match(message):
    return "I do not have enough data yet"
   