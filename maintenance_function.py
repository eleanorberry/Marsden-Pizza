menu = [
    ["Margarita", 18.50, "cheese"],
    ["Pepperoni", 18.50, "pepperoni"],
    ["Hawaiian", 18.50, "pineapple"]
]

def get_integer(m):
    my_integer=int(input(m))
    return my_integer

def get_string(m):
    my_string = input(m)
    return my_string

def print_with_indexes(L):
    for i in range(0, len(L)):
        output ="{} {} {} {}".format(i, L[i][0], L[i][1], L[i][2])
        print(output)

# add a new type of pizza to the list
def add_new_pizza(menu):
    print("Start adding new entry.")
    pizza_name = get_string("What is the name of the pizza you would like to add?: ")
    i = search(menu)
    print(i)
    if i:
        L[i][1] += amount
        print_with_indexes(menu)
    else:
        price = get_integer("What is the price of the pizza?: ")
        description = get_string("Please enter the description for the new pizza: ")
        new_list = [pizza_name, price, description]
        menu.append(new_list)

def search(menu):
    for i in range(0, len(menu)):
        output = "{} {}".format(menu[i][0], pizza_name)
        print(output)
        if menu[i][0] == pizza_name:
            print("The pizza you want to add is already in the list, sorry")
            return i

def remove_pizza(menu):
    print_with_indexes(menu)
    my_index = get_integer("Please enter the index number of the pizza you want to remove: ")
    w
    new_list = [name, hair_colour, age]
    L.append(new_list)

def update_pizza_name(menu):
    print_with_indexes(menu)
    my_index = get_integer("Please enter the index number of the pizza you want to update the name of: ")
    new_name = get_string("Please enter the new name: ")
    old_name = menu[my_index][0]
    menu[my_index][0] = new_name
    output_message = "{} has now been changed to {}.".format(old_name, new_name)
    print(output_message)

def update_price(menu):
    print_with_indexes(menu)
    my_index = get_integer("Please enter the index number to update the price of: ")
    new_price = get_string("Please enter the new price: ")
    name = menu[my_index][0]
    old_price = menu[my_index][1]
    menu[my_index][1] = new_price
    output_message = "{}'s price has been changed from {} to {}.".format(name, old_price, new_price)
    print(output_message)

def update_description(menu):
    print_with_indexes(menu)
    my_index = get_integer("Please enter the index number to update the description of: ")
    name = menu[my_index][0]
    new_description = get_string("Please enter the new description: ")
    old_description = menu[my_index][2]
    menu[my_index][2] = new_description
    output_message = "{} is no longer {} instead it is {}.".format(name, old_description, new_description)
    print(output_message)

def update_menu():
    option = '''
        A: Update Pizza name
        B: Update Pizza price
        C: Update Pizza description
        Q: Return to maintenance menu
        '''
    run = True
    while run == True:
        print(option)
        update_choice = get_string("Please select option: ")
        update_choice = update_choice.upper()
        if update_choice == "A":
            update_pizza_name(menu)
        if update_choice == "B":
            update_price(menu)
        if update_choice == "C":
            update_description(menu)
        elif update_choice == "Q":
            run = False
        else:
            print("User will be returned to the maintenance menu")
            run = False


def maintenance_function():
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if username == "marsdenpizza" and password == "marsdenpizza":
        print("Welcome to the maintenance menu")
        option = '''
        A: Add Pizza
        B: Remove Pizza
        C: Update Pizza
        D: Review Menu
        Q: Quit
        '''
        print("~" * 80)
        run = True
        while run == True:
            print(option)
            choice = get_string("Please select option: ")
            choice = choice.upper()
            print("~" * 80)
            if choice == "A":
                add_new_pizza(menu)
                print_with_indexes(menu)
            if choice == "B":
                add_new_pizza(menu)
            if choice == "C":
                update_menu()
            if choice == "D":
                print_with_indexes(menu)
            elif choice == "Q":
                print("Thank you")
                print("~" * 80)
                run = False
    else:
        print("Login failed")
        print("User will be returned to the main menu")
        run = False

maintenance_function()
