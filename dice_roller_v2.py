import random
import re
import typing


class DiceRoller:

    @staticmethod
    def roll_parser(user_input:str) -> typing.List[int]:
        replaced = user_input.replace("+","d").replace("-","d")
        numbers = replaced.split("/")[0].split("d")
        numbers = [int(i) for i in numbers]
        
        if len(numbers) == 2: #if there is no modifier
            numbers.append(0)

        if "-" in user_input: #checking if modifier is a negative
            numbers[-1] = 0 - numbers[-1]
        
        if "/" in user_input: #checking advantage or disadvantage
            adv_or_disadv = user_input.split("/")[1]
            how_many = len(adv_or_disadv)
            numbers.append(how_many)
            if "a" in adv_or_disadv:
                numbers.append(1)
            if "d" in adv_or_disadv:
                numbers.append(-1)
        else:
            numbers.extend([0,0])

        return numbers

    @staticmethod
    def roller(numbers:typing.List[int], dice_roll_count:int) -> int:
        sides = numbers[1]
        how_many = numbers[3]
        adv_status = numbers[4]
        roll_count = 0
        rolls = []
        #3 cases
        #no advantage or disadvantage
        if adv_status == 0:
            roll = random.randint(1,sides)
            print(f"Roll #{dice_roll_count+1} : {roll}")
            return roll
        #advantage or disadvantage
        else:
            while roll_count < how_many+1:
                roll = random.randint(1,sides)
                rolls.append(roll)
                roll_count += 1
            if adv_status > 0: #advantage
                print(f"Roll #{dice_roll_count+1} : {max(rolls)} (Your rolls were {rolls})")
                return max(rolls)
            else: #disadvantage
                print(f"Roll #{dice_roll_count+1} : {min(rolls)} (Your rolls were {rolls})")
                return min(rolls)

    def start(self):
        pattern = re.compile("(\d{1,3}d\d{1,3})((\+|-)\d{1,3})?(\/(a+|d+))?")
        while True:
            roll = input("What is your roll?(enter 'x' to quit): ")
            if roll == "x":
                break
            elif not bool(pattern.match(roll)):
                print("""
                Wrong format.
                Input format "xdy".
                Optional modifier + or - a number (xdy+z).
                /a for advantage, /d for disadvantage (xdy+z/a).
                /aa for double advantage so on and so forth.
                """)
                print("")
            else:
                numbers = self.roll_parser(roll)
                how_many_dice = numbers[0]
                modifier = numbers[2]
                roll_count = 0
                rolls = []
                while roll_count < how_many_dice:
                    roll = self.roller(numbers,roll_count)
                    rolls.append(roll)
                    roll_count += 1
                rolls.append(modifier)
                if modifier != 0:
                    print(f"Your modifier is : {modifier}")
                total = sum(rolls)
                print(f"Your final roll is : {total}")
                print("")

d = DiceRoller()

d.start()