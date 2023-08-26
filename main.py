import random

# Слова для угадывания
words = ["python", "programming", "hangman", "developer", "computer", "фрукт", "овощь"]

# Выбор случайного слова
word_to_guess = random.choice(words)

# Состояние виселицы
hangman_stages = [
    """
     -----
         |
         |
         |
         |
    """,
    """
     -----
     O   |
         |
         |
         |
    """,
    """
     -----
     O   |
     |   |
         |
         |
    """,
    """
     -----
     O   |
    /|   |
         |
         |
    """,
    """
     -----
     O   |
    /|\\  |
         |
         |
    """,
    """
     -----
     O   |
    /|\\  |
    /    |
         |
    """,
    """
     -----
     O   |
    /|\\  |
    / \\  |
         |
    """
]

# Текущее состояние угадывания
current_guess = ["_"] * len(word_to_guess)

# Количество попыток
attempts = 6

def display_state():
    print(hangman_stages[attempts])
    print(" ".join(current_guess))

def play_game():
    global attempts
    while "_" in current_guess and attempts > 0:
        display_state()
        guess = input("Введите букву: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Введите одну букву!")
            continue
        if guess in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    current_guess[i] = guess
        else:
            attempts -= 1
            print("Неверная буква! Осталось попыток:", attempts)
    
    if "_" not in current_guess:
        print("Вы победили! Загаданное слово:", word_to_guess)
    else:
        print("Вы проиграли! Загаданное слово было:", word_to_guess)

if __name__ == "__main__":
    print("Добро пожаловать в игру Виселица!")
    play_game()
