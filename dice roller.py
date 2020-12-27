#dnd dice roller
import random
import re

def roll_modifier(roll):
    modifier = None
    if "+" in roll:
        modifier = True
        return modifier
    elif "-" in roll:
        modifier = False
        return modifier
    else:
        return modifier

def mod_quantity(roll):
    quantity = 0
    if "+" in roll:
        quantity = int(roll.split("d")[1].split("+")[1])
        return quantity
    elif "-" in roll:
        quantity = int(roll.split("d")[1].split("-")[1])
        return quantity
    else:
        return quantity
        pass

def how_many_to_roll(roll):
    dice_num = int(roll.split("d")[0])
    return dice_num

def dice_type(roll):
    if "+" in roll:
        dice = int(roll.split("d")[1].split("+")[0])
        return dice
    elif "-" in roll:
        dice = int(roll.split("d")[1].split("-")[0])
        return dice
    else:
        dice = int(roll.split("d")[1])
        return dice
        pass

def check_input(prompt):
    while True:
        try:
            roll = str(input(prompt).lower())
            pattern = re.compile("((([0-9]){1,3})+d+(([0-9]){1,3}))|^x{1}$")
            result = bool(pattern.match(roll))
        except ValueError:
            print ("What the fuck did you input.")
        if result == True:
            break
        else:
            print ("Input format: 'xdy'. Enter 1 'x' to quit.")
            print("."*70)
    return roll

def roll_dice():
    print ("DnD dice roller")
    print ("To stop at any point input 'x'")
    print("."*70)
    while True:
        roll = check_input("Enter your roll(enter 'x' to quit): ")
        if roll == "x":
            print("Quitting script")
            print("."*70)
            break
        roll_total = 0
        roll_count = 0
        dice_count = how_many_to_roll(roll)
        dice_sides = dice_type(roll)
        add_subtract = roll_modifier(roll)
        how_much = mod_quantity(roll)
        while roll_count < dice_count:
            rolls = random.randint(1,dice_sides)
            print("Roll ",roll_count+1," is ",rolls)
            roll_total += rolls
            roll_count += 1
        if add_subtract == None:
            pass
        elif add_subtract == True:
            print("Your modifier is +",how_much)
            roll_total += how_much
        elif add_subtract == False:
            print("Your modifier is -",how_much)
            roll_total -= how_much
        else:
            pass
        print("Your roll is: ",roll_total)
        print("."*70)


roll_dice()