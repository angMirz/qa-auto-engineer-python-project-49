import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def is_prime(n):

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def get_question_and_answer():
    number = random.randint(2, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"

    return question, correct_answer
