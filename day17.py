# quiz game using classes and functions

class QuizQuestion:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer

def run_quiz(questions):
    score = 0
    for q in questions:
        print(q.question)
        for i, option in enumerate(q.options): # i is the index, option is the value, because enumerate gives us both
            print(f"{i + 1}. {option}")
        user_answer = int(input("Enter the number of your answer: ")) - 1
        if q.check_answer(user_answer):
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
        print("Your current score is:", score)
    print(f"Your final score is {score}/{len(questions)}")

if __name__ == "__main__":
    questions = [
        QuizQuestion("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], 2),
        QuizQuestion("What is 2 + 2?", ["3", "4", "5", "6"], 1),
        QuizQuestion("What is the largest ocean?", ["Atlantic", "Indian", "Arctic", "Pacific"], 3),
    ]
    run_quiz(questions)
