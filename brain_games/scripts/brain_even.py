from brain_games.cli import welcome_user
import random


def parity_check(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')

    for _ in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if number % 2 == 0 else "no"

        if answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    parity_check(name)

if __name__ == "__main__":
    main()