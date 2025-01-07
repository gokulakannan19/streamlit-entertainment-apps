import random

def put_flames(name1, name2):
    if name1 == name2:
        message = "Both names are equal"
        return message
    else:
        name1 = list(name1.lower())
        name2 = list(name2.lower())
        for char in name1:
            if char in name2:
                name1.remove(char)
                name2.remove(char)
        char_count = len(name1) + len(name2)
        result = cyclic_elimination(char_count)
        return result[0]


def cyclic_elimination(count):
    flames_list = ["Friends", "Love", "Affectionate", "Marrage",
                   "Enemy", "Sister"]

    while len(flames_list) > 1:
        elimination_index = (count - 1) % len(flames_list)
        flames_list = flames_list[elimination_index+1:] + flames_list[:elimination_index]

    return flames_list

## ---------------------------------------------------------------

## ROCK PAPER SCISSOR

def rock_paper_scissor(user_choice):
    message = ""
    input_list = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(input_list)

    match user_choice:
        case "Rock":
            if computer_choice == "Scissor":
                message = "user"
            elif computer_choice == "Paper":
                message = "computer"
            else:
                message = "draw"

        case "Paper":
            if computer_choice == "Rock":
                message = "user"
            elif computer_choice == "Scissor":
                message = "computer"
            else:
                message = "draw"

        case "Scissor":
            if computer_choice == "Paper":
                message = "user"
            elif computer_choice == "Rock":
                message = "computer"
            else:
                message = "draw"

        case "Exit":
            message = "Game over"

    return computer_choice, message

def add_score(score):
    return score + 1