# Create an account to be a beta tester!
import time

email = str(input("Please, enter your google email: "))
if email:
    name = str(input("Enter your name (Highly required): "))
    if name:
        nameConfirmation = str(input("Please, confirm your name: "))
        if nameConfirmation == name:
            print("Success! 2 more steps left.")
            time.sleep(2)
            try:
                describeUser = str(input("Please describe yourself according to real life: "))
                age = int(input("Age: "))
                if age < 15:
                    print("Age under 15! Cannot be qualified for beta testing.")
                else:
                    print("Processing form...")
                    time.sleep(7)
                    print("You are qualified for beta testing!")
                    time.sleep(4)
                    print("Program closing in 8 seconds or you can exit the program.")
                    time.sleep(8)
                    quit("Program successfully quit.")
            except Exception as err:
                print("An error occured in the system during the survey, sorry for the inconvenience, please do the survey again.")
                time.sleep(6)
                print("Error: {err}")
        else:
            print("The name was wrong, please restart the survey.")
    else:
        print("Error occured, please start again.")
else:
    print("An error occured, please start the survey again.")