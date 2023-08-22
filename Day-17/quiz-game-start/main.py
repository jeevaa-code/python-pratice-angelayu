from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []
for i in question_data:
    texts = i["text"]
    answers = i["answer"]
    question = Question(texts,answers)
    question_bank.append(question)


quiz = QuizzBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print("you have completed the quiz ")
print(f"your final score was {quiz.score}/{quiz.question_number} ")


