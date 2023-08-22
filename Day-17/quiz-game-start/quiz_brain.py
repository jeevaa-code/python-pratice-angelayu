class QuizzBrain:
    def __init__(self,question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        A = len(self.question_list)
        if self.question_number < A:
            return True
        else:
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        correct_answer = current_question.answer
        self.check_answer(user_answer,correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you are correct")

        else:
            print("you are wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"your current score is: {self.score}/{self.question_number} ")





