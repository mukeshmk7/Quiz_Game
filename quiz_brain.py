class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.current_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        que = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q{self.question_number} : {que.text} - True/False ").lower()
        self.check_answer(user, que.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            print("you got it right")
            self.current_score += 1
        else:
            print("wrong")
        print(f"correct answer: {correct_answer}")
        print(f"your current score {self.current_score} / {self.question_number}")

