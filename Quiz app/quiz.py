import sys

Quiz_Data = [
    {
        "question": "What is the correct file extension for Python files?",
        "options": ["A) .pt", "B) .pyt", "C) .py", "D) .python"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation (power) in Python?",
        "options": ["A) ^", "B) **", "C) %", "D) //"],
        "answer": "B"
    },
    {
        "question": "How do you insert comments in Python code?",
        "options": ["A) //", "B) <!--", "C) /*", "D) #"],
        "answer": "D"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A) List", "B) Dictionary", "C) Tuple", "D) Set"],
        "answer": "C"
    }
]

def run_quiz():
    print("=== Python CLI Quiz app ===")
    print("Type 'exit/ at any prompt to quiz.\n")

    score = 0
    total_questions = len(Quiz_Data)

    for idx, item in enumerate(Quiz_Data, start=1):
        print(f"Question {idx} of {total_questions}:")
        print(item["question"])


# PRint option
        for option in item["options"]:
            print(f" {option}")

        # Get any validate user answer
        while True:
            user_choice = input("\nYour answer (A, B, C, D): ").strip().upper()

            if user_choice == "EXIT":
                print("\nQuiz cancecelled. Goodbye!")
                sys.exit()

            if user_choice in ['A', 'B', 'C', 'D']:
                break
            print("Invalid choice! ")
            # check if answer is correct
        if user_choice == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect! The right answer was {item['answer']}.\n")

        print("-" * 40)

    # Calculate final results
    percentage = (score / total_questions) * 100
    print("\n===  Final Results ===")
    print(f"Your Score: {score} / {total_questions}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print(" Outstanding job!")
    elif percentage >= 50:
        print(" Good effort! Keep practicing.")
    else:
        print(" Better luck next time!")

if __name__ == "__main__":
    run_quiz()