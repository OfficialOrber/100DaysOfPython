from data import question_data
from questions_model import Question
from quiz_brain import QuizBrain

# Setup question bank
question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

# Start quiz question bank
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
