import html


class QuizBrain:

    def __init__(self, q_list):
        # super().__init__()
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        if self.still_has_questions():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            q_text = html.unescape(self.current_question.text)
            return f"Q.{self.question_number}: {q_text} (True/False): "
            # self.get_question_text(q_text)
            # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
            # self.check_answer(user_answer)
        else:
            return "Thanks for playing!"

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
            # print("You got it right!")
        else:
            # print("That's wrong.")
            return False

        # print(f"Your current score is: {self.score}/{self.question_number}")
        # print("\n")
