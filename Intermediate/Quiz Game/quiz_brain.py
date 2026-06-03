import random as rnd

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        rnd.shuffle(question_list)
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Check if there are questions left in the list."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Move the question to the next question."""
        # Get the question base on its index
        current_q = self.question_list[self.question_number]
        # Add 1 to the current question number
        self.question_number += 1
        print("\n")
        # Ask the question
        user_ans = input(f"Q.{self.question_number}: {current_q.text} (Ture/False)?: ")
        # Check the answer
        self.check_answer(user_ans, current_q.answer)

    def check_answer(self, user_ans, correct_answer):
        """Check if the user answered the correct answer and increase the score."""
        # Correct answer
        if user_ans.lower() == correct_answer.lower():
            self.score += 1; print("You got it right!")

        # Incorrect answer
        else: print("That's wrong!")

        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")



class Question:

    def __init__ (self, text, answer):
        self.text = text
        self.answer = answer
