import random

DESCRIPTION = "What number is missing in the progression?"


def get_question_and_answer():
    length = random.randint(5, 10)
    start = random.randint(1, 50)
    step = random.randint(1, 5)

    progression = []
    for i in range(length):
        currentElement = start + i * step
        progression.append(currentElement)
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    
    question = ""
    for item in progression:
        question += str(item) + " "
    question = question.strip()

    return question, correct_answer
