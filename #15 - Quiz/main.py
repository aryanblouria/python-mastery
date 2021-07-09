from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []
for ques in question_data:
    t = ques["text"]
    a = ques["answer"]
    q = Question(t, a)
    question_bank.append(q)

qb = QuizBrain(question_bank)

while qb.still_has_questions():
    qb.next_question()
print("You have completed the quiz!")
print(f"Your final score is {qb.score}/{qb.ques_no}")





