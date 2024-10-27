# PROJECT 1
# PYTHON PROGRAMMING INTERNSHIP - MOTION CUT
# AUTHOR: KARAN DIUNDI

# We will be using a list of dictionaries to define the quiz questions, options, and correct answers.
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"],
        "answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Hamlet'?",
        "options": ["A) Mark Twain", "B) Charles Dickens", "C) William Shakespeare", "D) J.K. Rowling"],
        "answer": "C"
    }
]

# Defining the function to run the quiz.
def run_quiz(questions):
    score = 0  # Initialize the score.
    total_questions = len(questions)  # Get the total number of questions.

    # Iterate over the list of dictionaries (each representing a quiz question).
    for q in questions:
        print("\n" + q["question"])  # Display the question.
        
        # Iterate over the options (nested list) and print each option.
        for option in q["options"]:
            print(option)
        
        # Get the user's answer as input and convert it to uppercase for validation.
        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        # Validate the user's input to ensure it is one of the allowed options.
        while user_answer not in ["A", "B", "C", "D"]:
            user_answer = input("Invalid choice. Please enter A, B, C, or D: ").upper()

        # Check if the user's answer matches the correct answer.
        if user_answer == q["answer"]:
            print("Correct!")
            score += 1  # Increment the score if the answer is correct.
        else:
            print(f"Wrong! The correct answer is {q['answer']}")  # Display the correct answer if wrong.

    # Display the final score at the end of the quiz.
    print(f"\nQuiz Complete! You scored {score}/{total_questions}")

# Run the quiz by calling the run_quiz function and passing the quiz questions.
run_quiz(quiz_questions)
