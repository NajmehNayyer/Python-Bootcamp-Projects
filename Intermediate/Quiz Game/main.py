from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

# Add each question to the question bank
for question in question_data:
    text = question['text']
    answer = question['answer']
    question_bank.append(Question(text, answer))
 
quiz = QuizBrain(question_bank)

while quiz.still_has_questions: quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
