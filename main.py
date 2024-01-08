# ask the user to pick if they want to enter trainer mode or just user mode

def choice():
    #python3 for some reason doesn't work on my end of network
    user = raw_input("Would you like to enter trainer mode or user mode?") 
    
    if user == "trainer":
        print("trainer")
    elif user == "user":
        print("users")
    else:
        print("invalid")
        choice()



if __name__ == '__main__':
    choice()