    #----------------YOUR AGE-------------------
try:
    if __name__ == '__main__':


        present_date = 2021

        user_date = int(input("Enter your date of birth = "))

        if user_date>present_date:
            print("You are not born yet")
        elif present_date-user_date>120:
            print("You are either to old or enter wrong input")
        elif user_date==present_date:
            print("Welcome to this world")

        else:
            print(f"You are now {present_date-user_date} years old")
            print(f"In {user_date+100} you will complete century")

        calc = str(input("Do you want to calculate your age at specific year? \ny/n = "))

        if calc=='y':
            a=int(input(f"Enter the year = "))
            print(f"You will become {a-user_date} in {a}")

        elif calc=='n':
            exit()
except Exception as e:
    print("Wrong input",e)


