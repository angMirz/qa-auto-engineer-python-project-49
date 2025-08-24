import random

DESCRIPTION = "What is the result of the expression?"

OPERATIONS = ["+", "-", "*"]


def get_question_and_answer():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    operation = random.choice(OPERATIONS)

    question = f"{number1} {operation} {number2}"

    match operation:
        case "+":
            correct_answer = number1 + number2
        case "-":
            correct_answer = number1 - number2
        case "*":
            correct_answer = number1 * number2

    return question, str(correct_answer)