from generate_question import Question
from data import question_data as que_data
from data import category_list
from game import Brain

print("List of all categories")
print("\n".join(category_list))

que_bank = []
for i in que_data:
    que_set = Question(i['category'],
                       i['difficulty'],
                       i["set"])
    que_bank.append(que_set)

start = Brain(que_bank)
start.genre()

while start.still_has_questions():
    start.next_question()

print(f"Your Final Score is {start.score}/{start.question_no}")
