import random
from Dice_simulator import dice_sim


def py2001():
    p1_score = 0
    p2_score = 0
    # main game loop
    turn_count = 1
    while True:
        # Version 1 commented out
        # input("press Enter to throw dice")
        # p1_throw = dice_sim.throw_dice("2D6")

        # Setting current throw back to 0
        p1_throw = 0
        p2_throw = 0

        # Player selecting dice
        player_dice = player_dice_selection()
        # Throwing and saving the throw result
        for die in player_dice:
            p1_throw += dice_sim.throw_dice(die)

        print(f"You've got {p1_throw}")
        p1_score += p1_throw
        if turn_count > 1:
            if p1_throw == 7:
                print("Dividing your score by 7")
                p1_score = p1_score // 7
            elif p1_throw == 11:
                print("Multiplying your score by 11")
                p1_score = p1_score * 11

        # Version 1 commented out
        # p2_throw = dice_sim.throw_dice("2D6")
        cpu_dice = cpu_dice_selection()
        for die in cpu_dice:
            p2_throw += dice_sim.throw_dice(die)

        print(f"CPU got {p2_throw}")
        p2_score += p2_throw
        if turn_count > 1:
            if p2_throw == 7:
                print("Dividing CPUs score by 7")
                p2_score = p2_score // 7
            elif p2_throw == 11:
                print("Multiplying CPUs score by 11")
                p2_score = p2_score * 11
        print(f"Your score: {p1_score}")
        print(f"CPUs score: {p2_score}")
        turn_count += 1
        if p1_score > 2001:
            print("You win!")
            return
        if p2_score > 2001:
            print("CPU win!")
            return


def player_dice_selection():
    available_dice = ("D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100")
    while True:
        die1 = input("Type your first die code: \n")
        if die1 not in available_dice:
            print("Choose a valid die type")
            continue
        break
    while True:
        die2 = input("Type your second die code: \n")
        if die2 not in available_dice:
            print("Choose a valid die type")
            continue
        break
    return die1, die2


def cpu_dice_selection():
    available_dice = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    random.shuffle(available_dice)
    return available_dice[0], available_dice[1]


py2001()
