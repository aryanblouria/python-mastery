class QuizBrain:
    def __init__(self, ques_list):
        self.ques_no = 0
        self.ques_list = ques_list
        self.score = 0

    def next_question(self):
        curr_ques = self.ques_list[self.ques_no]
        self.ques_no += 1
        ua = input(f"Q.{self.ques_no}: {curr_ques.text} (True/False): ")
        self.check_ans(curr_ques, ua)

    def still_has_questions(self):
        return self.ques_no < len(self.ques_list)

    def check_ans(self, curr_ques, ua):
        if curr_ques.ans.lower() == ua.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {curr_ques.ans}")
        print(f"The current score is: {self.score}/{self.ques_no}")
        print("\n")