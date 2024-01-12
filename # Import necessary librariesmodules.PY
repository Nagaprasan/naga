# Import necessary libraries/modules

# Define the question bank with at least three questions
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. Rome", "C. Madrid"],
        "correct_answer": "A"
    },
    # Add more questions with similar structure
]

# Initialize variables for tracking the user's score
correct_answers = 0
total_questions = len(questions)

# Function to display the quiz questions and handle user input
def run_quiz():
    global correct_answers
    
    print("Welcome to the Quiz Game!\n")
    
    # Iterate through each question in the question bank
    for idx, question in enumerate(questions, 1):
        print(f"Question {idx}: {question['question']}")
        
        # Display multiple-choice options
        for option in question['options']:
            print(option)
        
        # Get user input and validate it
        user_answer = get_user_input()
        
        # Check if the user's answer is correct and provide feedback
        if user_answer.upper() == question['correct_answer']:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Incorrect. The correct answer is {question['correct_answer']}\n")
    
    # Display the final score
    print(f"Quiz completed! Your final score is: {correct_answers}/{total_questions}")

# Function to get user input with appropriate validation
def get_user_input():
    while True:
        user_input = input("Enter the letter corresponding to your answer: ").upper()
        
        # Validate user input (assuming options are represented by letters)
        if user_input.isalpha() and user_input in ["A", "B", "C"]:
            return user_input
        else:
            print("Invalid input. Please enter a valid letter (A, B, or C).\n")

# Main function to execute the quiz
def main():
    run_quiz()

# Entry point of the script
if __name__ == "__main__":
    main()
