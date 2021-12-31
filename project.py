# Write your code here
# Espresso sources
espresso_water = 250
espresso_coffee_beans = 16
coffee_cup = 1
espresso_cost = 4
# Latte sources
latte_water = 350
latte_milk = 75
latte_coffee_beans = 20
latte_cost = 7
coffee_cup = 1
# Cappuccino sources
cappuccino_water = 200
cappuccino_milk = 100
cappuccino_coffee_beans = 12
cappuccino_cost = 6

class CoffeeMachine():
    def __init__(self, water, milk, coffee_beans, disposable_cups, money):
        self.water_volume = water
        self.milk_volume = milk
        self.coffee_beans_volume = coffee_beans
        self.disposable_cups = disposable_cups
        self.money = money

    def action(self, status):
        self.status = status
        if self.status == "buy":
            self.buy()
        elif status == "fill":
            self.fill()
        elif status == "take":
            self.take()
        elif status == "remaining":
            self.remaining()
        elif status == "exit":
            pass

    def fill(self):
        self.water_volume += int(input("Write how many ml of water you want to add:\n"))
        self.milk_volume += int(input("Write how many ml of milk you want to add:\n"))
        self.coffee_beans_volume += int(input("Write how many grams of coffee beans you want to add:\n"))
        self.disposable_cups += int(input("Write how many disposable coffee cups you want to add:\n"))
        return self.water_volume, self.coffee_beans_volume, self.disposable_cups, self.milk_volume
    
    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0
        return self.money

    def remaining(self):
        print("The coffee machine has:")
        print(self.water_volume, "of water")
        print(self.milk_volume, "of milk")
        print(self.coffee_beans_volume, "of coffee beans")
        print(self.disposable_cups, "of disposable cups")
        print(f"${self.money} of money")

    def buy(self):
        coffee = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
        if coffee == "1":
            self.espresso_check()
        elif coffee == "2":
            self.latte_check()
        elif coffee == "3":
            self.cappuccino_check()
        elif coffee == "back":
            pass

    def espresso(self):
        # For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. It costs $4.
        self.water_volume -= espresso_water
        self.coffee_beans_volume -= espresso_coffee_beans
        self.disposable_cups -= coffee_cup
        self.money += espresso_cost
        return self.water_volume, self.coffee_beans_volume, self.disposable_cups, self.money


    def espresso_check(self):
        espresso_ch = [self.water_volume >= espresso_water, self.coffee_beans_volume >= espresso_coffee_beans, self.disposable_cups >= coffee_cup]
        if all(espresso_ch):
            print("I have enough resources, making you a coffee!")
            self.espresso()
        elif self.water_volume < espresso_water:
            print("Sorry, not enough water!")
        elif self.coffee_beans_volume < espresso_coffee_beans:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < coffee_cup:
            print("Sorry, not enough disposable cups!")

    def latte(self):
        # For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans. It costs $7.
        self.water_volume -= latte_water
        self.milk_volume -= latte_milk
        self.coffee_beans_volume -= latte_coffee_beans
        self.disposable_cups -= coffee_cup
        self.money += latte_cost
        return self.water_volume, self.coffee_beans_volume, self.disposable_cups, self.money, self.milk_volume


    def latte_check(self):
        latte_ch = [self.water_volume >= latte_water, self.coffee_beans_volume >= latte_coffee_beans, self.milk_volume >= latte_milk, self.disposable_cups >= coffee_cup]
        if all(latte_ch):
            print("I have enough resources, making you a coffee!")
            self.latte()
        elif self.water_volume < latte_water:
            print("Sorry, not enough water!")
        elif self.milk_volume < latte_milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans_volume < latte_coffee_beans:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < coffee_cup:
            print("Sorry, not enough disposable cups!")

    def cappuccino(self):
        # for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee beans. It costs $6.
        self.water_volume -= cappuccino_water
        self.milk_volume -= cappuccino_milk
        self.coffee_beans_volume -= cappuccino_coffee_beans
        self.disposable_cups -= coffee_cup
        self.money += cappuccino_cost
        return self.water_volume, self.coffee_beans_volume, self.disposable_cups, self.money, self.milk_volume


    def cappuccino_check(self):
        cappuccino_ch = [self.water_volume >= cappuccino_water, self.coffee_beans_volume >= cappuccino_coffee_beans, self.milk_volume >= cappuccino_milk, self.disposable_cups >= coffee_cup]
        if all(cappuccino_ch):
            print("I have enough resources, making you a coffee!")
            self.cappuccino()
        elif self.water_volume < cappuccino_water:
            print("Sorry, not enough water!")
        elif self.milk_volume < cappuccino_milk:
            print("Sorry, not enough milk!")
        elif self.coffee_beans_volume < cappuccino_coffee_beans:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < self.coffee_cup:
            print("Sorry, not enough disposable cups!")
   
basic = CoffeeMachine(400, 540, 120, 9, 550)

def action():
    while True:
        question = input("Write action (buy, fill, take, remaining, exit):\n")
        if question == "buy":
            basic.action("buy")
        elif question == "fill":
            basic.action("fill")
        elif question == "take":
            basic.action("take")
        elif question == "remaining":
            basic.action("remaining")
        elif question == "exit":
            break

action()
