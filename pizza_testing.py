def get_integer(m, min ,max):
    number = True
    while number is True:
        my_number = int(input(m))
        my_integer = my_number.isnumeric
        if my_integer is False:
            print("Please enter an integer")
            continue
        if my_integer < min:
            print("The value is too low")
            continue
        elif my_integer > max:
            print("The value is too high")
            continue
        else:
            return my_integer


''' Function gets user name input and checks whether it is valid and
then returns if not it asks again telling the user what to do differently'''


def get_string(m, max, min):
    get_name = True
    while get_name is True:
        name = input(m)
        # Changes user input into proper noun grammar structure
        proper_name = name.title()
        if len(name) > max:
            print("Sorry, you have entered an invalid input")
            print(" ")
            print("Please enter a name with less than {} letters".format(max))
            print(" ")
        # If the name has less than 2 letters
        elif len(name) < min:
            print("Sorry, you have entered an invalid input")
            print(" ")
            print("Please try again and enter input with {} or more letters: ".format(min))
            print(" ")
        else:
            # if get here everything is right
            return proper_name


# Function gets user input to questions makes sure that it is acceptable
# then returns if not it asks again telling the user what to do differently
# first taking the specified message 'm' and the list of possible inputs 's'
def get_specific_input(m, s):
    get_input = True
    while get_input is True:
        # Asks for input
        user_input = input(m)
        # Strips user input
        user_input = user_input.strip()
        # Changes user input into upper case
        user_input = user_input.upper()
        # If user input isn't either ... print message
        if user_input not in s:
            print("You have not entered the appropriate input, please try again.")
            continue
        else:
            get_input = False
        # if get this far we should get what I want
        return user_input


def get_entry_option_list(m, o, u=True):
    # Request and return a valid entry using a list of options
    # m is string message, o is list of options, u is a boolean
    cont = True
    while cont is True:
        choice = input(m)
        if u:
            choice = choice.upper()
        if choice not in o:
            print("Please choose from these options: {}".format(o))
        else:
            return choice


def get_phone_number():
    # Request valid phone number from user returning the number in proper format
    cont = True
    while cont is True:
        phone = input("Please enter phone number (Please enter without spaces): ")
        phone_text = len(phone)
        if 6 < phone_text or phone_text > 15:
            message = "The phone number you have entered is {}".format(phone)
            print(message)
            choice = get_entry_option_list("Please confirm Y/N: ", ["Y", "N"])
            if choice == "Y":
                print("Phone number accepted")
                return phone
        else:
            print("This doesn't look quite right, phone number length not valid")
            print("Please enter a number in between 6 and 15 digits")


def print_menu_indexes(m):
    print("-" * 80)
    for i in range(0, len(m)):
        output = "{} {} {}".format(i, m[i][0], m[i][1])
        print(output)


def print_info(i, c):
    print("Cost: {}".format(c))
    print("-" * 80)
    if len(i) == 0:
        print("Sorry you haven't entered your personal information. ")
        print("Please complete this by choosing option 'B' to fill out the appropriate information")
    else:
        print("Customer Information:")
        for item, info in i.items():
            print("{}: {}".format(item, info))
        return


def delivery_pickup(d, c):
    cont = True
    while cont is True:
        if len(d) > 0:
            print("It looks like you've already filled out the information")
            print(d)
            choice = get_entry_option_list("Do you want to redo the details Y/N: ", ["Y", "N"])
            if choice == "N":
                print("You have kept the same information")
                print(d)
                cont = False
            elif choice == "Y":
                d.clear()
        delivery_pickup_m = "Please enter 'D' for delivery or 'P' for pick-up? (Delivery is an extra $3 charge): "
        delivery_pickup_s = ["D", "P"]
        user_input = get_specific_input(delivery_pickup_m, delivery_pickup_s)
        user_name = get_string("What is the user's name?: ", 25, 2).title()
        d["Name"] = user_name
        if user_input == "P":
            order_choice = "pick-up"
            return
        elif user_input == "D":
            phone_number = get_phone_number()
            d["Phone number"] = phone_number
            address = get_string("What is your address?: ", 100, 5).title()
            d["Address"] = address
            c += 3
            order_choice = "delivery"
        d["Type"] = order_choice
        print("Thank you for your order {}, you have chosen to have your order as a {}".format(user_name, order_choice))
        print("Cost: {}".format(c))
        print(d)
        choice = get_entry_option_list("Do you confirm the details Y/N: ", ["Y", "N"])
        if choice == "Y":
            print("Customer Info collected")
            return d, c
        elif choice == "N":
            d.clear()
            if order_choice == "delivery":
                c = - 3
            choice = get_entry_option_list("Would you like to return to the main menu (1) or try again (2): ", ["1", "2"])
            if choice == "1":
                cont = False
            elif choice == "2":
                continue


def main():
    customer_info = {}
    cost = 0
    menu = [
        ["Margarita", 18.50],
        ["Pepperoni", 18.50],
        ["Hawaiian", 18.50]
    ]
    option = '''
    A: Review menu
    B: Choose method of collection
    C: See customer details
    Q: Quit
    '''
    menu_choice = ["A", "B", "C", "Q"]
    menu_m = "Please enter an option: "
    run = True
    print("Starting new order")
    while run is True:
        print("-" * 80)
        print(option)
        print("-" * 80)
        choice = get_specific_input(menu_m, menu_choice)
        choice = choice.upper()
        if choice == "A":
            print_menu_indexes(menu)
        elif choice == "B":
            delivery_pickup(customer_info, cost)
        elif choice == "C":
            print_info(customer_info, cost)
        elif choice == "Q":
            print("Thank you")
            run = False


main()
