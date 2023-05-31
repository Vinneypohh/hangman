from typing import List
from random_word import RandomWords

def get_indexes_of_letter(
    char: str,
    wd: str
    ) -> List[int]:
    """Find all indexes of character in word

    Args:
        char (str): character
        wd (str): word

    Returns:
        List(int): list of indexes
    """
    return [i for i, ltr in enumerate(wd) if ltr == char]

def hangman(word:str) -> None:
    """Hangman game

    Args:
        word (str): word for player to guess
    """
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to hangman game!")
    print("Please enter # if you want to quit")

    while wrong < len(stages) - 1:
        msg = "Enter letter: "
        char = input(msg)
        if char == "#":
            win = True
            break

        indexes = get_indexes_of_letter(char, rletters)
        if indexes:
            for index in indexes:
                board[index] = char
                rletters[index] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        etap = wrong + 1
        print("\n".join(stages[0:etap]))
        if "__" not in board :
            print("Success, your word is:")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("You lost, your word is:")
        print(" ".join(word))


if __name__=="__main__":
    r = RandomWords()
    game_word = r.get_random_word()
    hangman(game_word)
