import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

GENERAL_KNOWLEDGE = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
        "answer": "C"
    },
    {
        "question": "Which language is mainly used for web page structure?",
        "options": ["A. HTML", "B. Python", "C. SQL", "D. Java"],
        "answer": "A"
    },
    {
        "question": "How many days are there in a leap year?",
        "options": ["A. 365", "B. 366", "C. 364", "D. 360"],
        "answer": "B"
    },
    {
        "question": "Which device is used to enter text into a computer?",
        "options": ["A. Monitor", "B. Printer", "C. Keyboard", "D. Speaker"],
        "answer": "C"
    }
]


def generate_math_questions(count=5):
    questions = []

    for _ in range(count):
        number1 = random.randint(1, 20)
        number2 = random.randint(1, 20)
        operator = random.choice(["+", "-", "*"])

        if operator == "+":
            answer = number1 + number2
        elif operator == "-":
            answer = number1 - number2
        else:
            answer = number1 * number2

        questions.append({
            "question": f"What is {number1} {operator} {number2}?",
            "answer": str(answer)
        })

    return questions


def ask_general_question(question, number, total):
    print("\n" + "=" * 55)
    print(f"Question {number}/{total}")
    print("=" * 55)

    print(question["question"])

    for option in question["options"]:
        print(option)

    start_time = time.time()

    while True:
        user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

        if user_answer in ["A", "B", "C", "D"]:
            break

        print(Fore.YELLOW + "Please enter A, B, C, or D.")

    elapsed_time = time.time() - start_time

    if elapsed_time > 15:
        print(Fore.YELLOW + "Time limit exceeded!")
        return False

    if user_answer == question["answer"]:
        print(Fore.GREEN + "Correct! ✓")
        return True

    print(
        Fore.RED
        + f"Wrong! The correct answer is {question['answer']}."
    )
    return False


def ask_math_question(question, number, total):
    print("\n" + "=" * 55)
    print(f"Question {number}/{total}")
    print("=" * 55)

    print(question["question"])

    start_time = time.time()
    user_answer = input("Your answer: ").strip()

    elapsed_time = time.time() - start_time

    if elapsed_time > 15:
        print(Fore.YELLOW + "Time limit exceeded!")
        return False

    if user_answer == question["answer"]:
        print(Fore.GREEN + "Correct! ✓")
        return True

    print(
        Fore.RED
        + f"Wrong! The correct answer is {question['answer']}."
    )
    return False


def save_score(score, total):
    try:
        with open("quiz_scores.txt", "a", encoding="utf-8") as file:
            current_time = time.strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            file.write(
                f"{current_time} - Score: {score}/{total}\n"
            )

        print(Fore.GREEN + "Score saved successfully.")

    except OSError as error:
        print(
            Fore.RED
            + f"Unable to save score: {error}"
        )


def show_result(score, total):
    percentage = (score / total) * 100

    print("\n" + "=" * 55)
    print("                 QUIZ RESULT")
    print("=" * 55)

    print(f"Score      : {score}/{total}")
    print(f"Percentage : {percentage:.1f}%")

    if percentage >= 80:
        print(Fore.GREEN + "Excellent performance! 🎉")
    elif percentage >= 50:
        print(Fore.YELLOW + "Good job! Keep practicing.")
    else:
        print(Fore.RED + "Keep practicing and try again.")


def start_quiz():
    print("\n" + "=" * 55)
    print("              PYTHON QUIZ GAME")
    print("=" * 55)

    print("\nChoose a category:")
    print("1. General Knowledge")
    print("2. Mathematics")

    while True:
        choice = input("\nEnter your choice (1/2): ").strip()

        if choice in ["1", "2"]:
            break

        print("Please choose 1 or 2.")

    score = 0

    if choice == "1":
        questions = GENERAL_KNOWLEDGE.copy()
        random.shuffle(questions)

        total = len(questions)

        for number, question in enumerate(
            questions,
            start=1
        ):
            if ask_general_question(
                question,
                number,
                total
            ):
                score += 1

    else:
        questions = generate_math_questions(5)
        total = len(questions)

        for number, question in enumerate(
            questions,
            start=1
        ):
            if ask_math_question(
                question,
                number,
                total
            ):
                score += 1

    show_result(score, total)
    save_score(score, total)


def main():
    while True:
        start_quiz()

        print("\nDo you want to play again?")

        choice = input(
            "Enter Y for Yes or N for No: "
        ).strip().upper()

        if choice != "Y":
            print("\nThank you for playing! 👋")
            break


if __name__ == "__main__":
    main()
