from brain_games.cli import welcome_user
import random


def game_logic(game):
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(game.DESCRIPTION)

    for _ in range(3):
        question, correct_answer = game.get_question_and_answer()
        print(f"Question: {question}")
        answer = input("Your answer: ").strip().lower()

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
