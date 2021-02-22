# # # # print("Starting to make a coffee")
# # # # print("Grinding coffee beans")
# # # # print("Boiling water")
# # # # print("Mixing boiled water with crushed coffee beans")
# # # # print("Pouring coffee into the cup")
# # # # print("Pouring some milk into the cup")
# # # # print("Coffee is ready!")
# # #
# # # count = int(input("Write how many cups of coffee you will need:\n"))
# # # print(f'''For {count} cups of coffee you will need:
# # # {200 * count} ml of water
# # # {50 * count} ml of milk
# # # {15 * count} g of coffee beans''')
# #
# # water = int(input('Write how many ml of water the coffee machine has:\n'))
# # milk = int(input('Write how many ml of milk the coffee machine has:\n'))
# # beans = int(input('Write how many grams of coffee beans the coffee machine has:\n'))
# # cups = int(input('Write how many cups of coffee you will need:\n'))
# # cap = []
# # cap.append(water // 200)
# # cap.append(milk // 50)
# # cap.append(beans // 15)
# # if min(cap) <= cups:
# #     print(f'No, I can make only {min(cap)} cups of coffee')
# # elif min(cap) == cups:
# #     print('Yes, I can make that amount of coffee')
# # elif min(cap) >= cups:
# #     print(f'Yes, I can make that amount of coffee (and even {min(cap) - cups} more than that)')
#
#
# def espresso():
#     global water, milk, beans, cups, cash
#     if water >= 250:
#         if beans >= 16:
#             if cups >= 1:
#                 water -= 250
#                 beans -= 16
#                 cash += 4
#                 cups -= 1
#                 print('I have enough resources, making you a coffee!\n')
#             else:
#                 print('Sorry, not enough cups!\n')
#         else:
#             print('Sorry, not enough beans!\n')
#     else:
#         print('Sorry, not enough water!\n')
#
#
# def latte():
#     global water, milk, beans, cups, cash
#     if water >= 350:
#         if milk >= 75:
#             if beans >= 20:
#                 if cups >= 1:
#                     water -= 350
#                     milk -= 75
#                     beans -= 20
#                     cash += 7
#                     cups -= 1
#                     print('I have enough resources, making you a coffee!\n')
#                 else:
#                     print('Sorry, not enough cups!\n')
#             else:
#                 print('Sorry, not enough beans!\n')
#         else:
#             print('Sorry, not enough milk!\n')
#     else:
#         print('Sorry, not enough water!\n')
#
#
# def cappuccino():
#     global water, milk, beans, cups, cash
#     if water >= 200:
#         if milk >= 100:
#             if beans >= 12:
#                 if cups >= 1:
#                     water -= 200
#                     milk -= 100
#                     beans -= 12
#                     cash += 6
#                     cups -= 1
#                     print('I have enough resources, making you a coffee!\n')
#                 else:
#                     print('Sorry, not enough cups!\n')
#             else:
#                 print('Sorry, not enough beans!\n')
#         else:
#             print('Sorry, not enough milk!\n')
#     else:
#         print('Sorry, not enough water!\n')
#
#
#
# def buy():
#     choice = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n"))
#     if choice == "1":
#         espresso()
#     elif choice == "2":
#         latte()
#     elif choice == "3":
#         cappuccino()
#     elif choice == "back":
#         return

def machine_state():
    print(f'''The coffee machine has:")
{water} of water
{milk} of milk
{beans} of coffee beans
{cups} of disposable cups
${cash} of money\n''')


def buy():
    choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if choice == '1':
        variations(choice, 250, 0, 16, 1, 4)
    elif choice == '2':
        variations(choice, 350, 75, 20, 1, 7)
    elif choice == '3':
        variations(choice, 200, 100, 12, 1, 6)
    elif choice == 'back':
        return print("")


def variations(choice, d_wat, d_milk, d_cof, d_cup, price):
    global water, milk, beans, cups, cash
    if choice in ('1', '2', '3'):
        if water < d_wat:
            print("Sorry, not enough water!\n")
        elif milk < d_milk:
            print("Sorry, not enough milk!\n")
        elif beans < d_cof:
            print("Sorry, not enough coffee!\n")
        elif cups < d_cup:
            print("Sorry, not enough cups!\n")
        else:
            print("I have enough resources, making you a coffee!\n")
            water -= d_wat
            milk -= d_milk
            beans -= d_cof
            cups -= d_cup
            cash += price


def fill():
    add_water = int(input("How much water do you want to add into the coffee machine?\n"))
    add_milk = int(input("How much milk do you want to add into the coffee machine?\n"))
    add_beans = int(input("How much coffee beans do you want to add into the coffee machine?\n"))
    add_cups = int(input("How many disposable cups do you want to add into the coffee machine?\n"))
    print("")
    global water, milk, beans, cups
    water += add_water
    milk += add_milk
    beans += add_beans
    cups += add_cups


def take():
    global cash
    print(f"I gave you ${cash}\n")
    cash = 0


def activity():
    while True:
        action = str(input('Write action (buy, fill, take, remaining, exit):\n'))
        if action == "buy":
            buy()
            continue
        elif action == "fill":
            fill()
            continue
        elif action == "take":
            take()
            continue
        elif action == "remaining":
            machine_state()
            continue
        elif action == "exit":
            break


water = 400
milk = 540
beans = 120
cups = 9
cash = 550

activity()
