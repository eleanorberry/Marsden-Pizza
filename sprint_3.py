def get_integer(m, min, max):
    # Transferable function for integer inputs with max and min values as well as message
    number = True
    while number is True:
        # asks for number
        my_number = int(input(m))
        # checks that number is an integer
        '''if my_number.isnumeric() is False:
            print("Please enter an integer")
            continue'''
        if my_number < min:
            print("The value is too low")
            continue
        elif my_number > max:
            print("The value is too high")
            continue
        else:
            return my_number


''' Function gets user input and checks whether it is valid and
then returns if not it asks again telling the user what to do differently'''


def get_string(m, max, min):
    # Transferable function for string input with max and min number of characters as well as message
    get_name = True
    while get_name is True:
        name = input(m)
        # Changes user input into proper noun grammar structure
        proper_name = name.title()
        if len(name) > max:
            print("Sorry, you have entered an invalid input")
            print("Please enter a name with less than {} letters".format(max))
        # If the name has less than 2 letters
        elif len(name) < min:
            print("Sorry, you have entered an invalid input")
            print("Please try again and enter input with {} or more letters: ".format(min))
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
    # Request valid phone number from user returning the number
    cont = True
    while cont is True:
        phone = input("Please enter phone number (Please enter without spaces): ")
        phone_text = len(phone)
        if phone.isnumeric() is False:
            # checks whether integer or not + error message
            print("This doesn't look quite right, phone number not an integer")
            print("Please enter a number without letters or other characters")
        elif 6 > phone_text or phone_text > 15:
            # checks length
            print("This doesn't look quite right, phone number length not valid")
            print("Please enter a number in between 6 and 15 digits")
        else:
            message = "The phone number you have entered is {}".format(phone)
            print(message)
            # confirmation if not start again
            choice = get_entry_option_list("Please confirm Y/N: ", ["Y", "N"])
            if choice == "Y":
                print("Phone number accepted")
                return phone


def print_menu_indexes(m):
    # Print the menu with index numbers
    print("-" * 80)
    for i in range(0, len(m)):
        output = "{:<5}{:20}${:<10.2f}".format(i, m[i][0], m[i][1])
        print(output)


def print_info(i, c):
    # Function to print out details collected with validation if dictionary empty
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
    # Function that runs the delivery/ pickup option
    # All info collected in a dictionary
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
            address = get_string("What is your address?: ", 50, 5).title()
            d["Address"] = address
            c += 3
            order_choice = "delivery"
            choice = get_entry_option_list("Do you want to add any delivery instructions Y/N: ", ["Y", "N"])
            if choice == "Y":
                request = get_string("Please enter delivery message: ", 50, 5)
                d["Request"] = request
        d["Type"] = order_choice
        print("Thank you for your order {}, you have chosen to have your order as a {}".format(user_name, order_choice))
        print("Cost: {}".format(c))
        print(d)
        # confirmation to check that the user accept the input
        choice = get_entry_option_list("Do you confirm the details Y/N: ", ["Y", "N"])
        if choice == "Y":
            print("Customer Info collected")
            return d, c
        elif choice == "N":
            d.clear()
            if order_choice == "delivery":
                c = - 3
            # user control can start again or return
            choice = get_entry_option_list("Would you like to return to the main menu (1) or try again (2): ", ["1", "2"])
            if choice == "1":
                cont = False
            elif choice == "2":
                continue


def check_name_present(o, n):
    # Check if a name is already in the pizza list
    # o: order list
    # n: choice name
    for i in range(0, len(o)):
        if o[i][0] == n:
            message = "{} is already present at index number {}".format(n, i)
            print(message)
            return i
    return -1


def search(P, pizza):
    for i in range(0, len(L)):
        output = "{} {}".format(L[i][0], fruit)
        print(output)
        if L[i][0] == fruit:
            print("Your fruit choice is already in the list, sorry")
            return i


def print_order(o, e):
    # Print out the current pizza order
    # o: list (row column) of the the current customer order
    # e: integer greater than 0 :
    total = 0
    for i in range(0, len(o)):
        # x **** at $**** sub total = $*****
        sub_total = o[i][1]*o[i][2]
        total += sub_total
        # Quantity , Pizza , Cost , subtotal
        my_string = "{:^5}{:<20} at ${:<8.2f} = ${:<8.2f}".format(o[i][2], o[i][0], o[i][1], sub_total)
        print(my_string)
    total += e
    my_string = "{:^5}${:<8.2f}".format("Total cost: ", total)
    print(my_string)


def add_pizza(p, order, max):
    # Add a pizza to the customer order
    message = "Please choose an option: "
    choice = get_integer(message, 0, len(p))
    pizza_name = p[choice][0]
    price = p[choice][1]
    result = check_name_present(order, pizza_name)
    if result == -1:
        message = "How many {} would you like?  "
        amount_string = message.format(pizza_name)
        amount = get_integer(amount_string, 0, max)
        order_list = [pizza_name, price, amount]
        order.append(order_list)
        confirmation_message = "{} {} have been added to the order".format(amount, pizza_name)
        print(confirmation_message)
        return None
        #proceed as normal

    else:
        message = "You already have {} of the {} in the order".format(order[result][2], pizza_name)
        print(message)
        available_pizza = max - order[result][2]
        print(available_pizza)
        message = "You can order a maximum of {} more".format(max - order[result][2])
        print(message)
        message = "How many more {} would you like?  "
        amount_string = message.format(pizza_name)
        amount = get_integer(amount_string, 0, available_pizza)
        order[result][2] += amount
        print(order)



def main():
    # main function that runs the program
    # variables
    regular = 18.5
    gourmet = regular + 7
    max_pizza = 5
    # dictionary containing pizzas, prices, and number of pizzas
    order = []
    customer_info = {}
    cost = 0
    menu = [
        ["Margarita", regular],
        ["Pepperoni", regular],
        ["Hawaiian", regular]
    ]
    option = '''
    A: Review menu
    B: Choose method of collection
    C: See customer details
    D: Add Pizza
    E: Review Order
    Q: Quit
    '''
    menu_choice = ["A", "B", "C", "D", "E", "Q"]
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
        elif choice == "D":
            print_menu_indexes(menu)
            add_pizza(menu, order, max_pizza)
        elif choice == "E":
            print_order(order, cost)
        elif choice == "Q":
            print("Thank you")
            run = False


main()
