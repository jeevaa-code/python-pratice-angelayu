class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_question(self):
        number = len(self.question_list)
        if self.question_number < number:
            return True

    def nextquestion(self, question_list):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True/list)?:  ")
        correct_answer = current_question.answer
        self.check_answer(answer, correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("your answer is correct")
            self.score += 1
        else:
            print("That is wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"The current score is {self.score}/{self.question_number}")
