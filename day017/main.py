from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html

question_bank = []
for q in question_data:
    question_bank.append(Question(html.unescape(q["question"]), q["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.get_final_score()