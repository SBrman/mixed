import random 

def play(switch):
    doors = [0, 1, 0]
    random.shuffle(doors)
    prize_door = [door for door, prize in enumerate(doors) if prize].pop()

    options = [0, 1, 2] 
    choice = random.choice(options)

    not_choice = options.copy()
    not_choice.remove(choice)
    
    reveal = [door for door in not_choice if door != prize_door].pop()
    
    if switch:
        not_choice.remove(reveal)
        choice = not_choice.pop() 
    
    return True if doors[choice] else False


if __name__ == "__main__":
    win = 0
    RUNS = 1000000
    for i in range(RUNS):
        if play(1):
            win += 1
    print((win / RUNS) * 100)
