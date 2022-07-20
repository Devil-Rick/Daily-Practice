class Brain:
    question_no = 0
    score = 0

    def __init__(self, que_list):
        self.question_list = que_list  # [object , object , object]
        self.genre_name = ""
        self.genre_level = ""
        self.genre_question_set = ""

    def genre(self):
        user_category = input("Type the category: ")
        user_level = input("Difficulty ('easy' / 'hard'): ")
        for i in range(len(self.question_list)):
            if self.question_list[i].category == user_category:
                if user_level == "easy":
                    self.genre_name = self.question_list[i].category
                    self.genre_level = self.question_list[i].difficulty
                    self.genre_question_set = self.question_list[i].questionset
                    break
                elif user_level == "hard":
                    self.genre_name = self.question_list[i + 1].category
                    self.genre_level = self.question_list[i + 1].difficulty
                    self.genre_question_set = self.question_list[i + 1].questionset
                    break
                else:
                    return "Sorry invalid genre."

    def next_question(self):
        que = self.genre_question_set[self.question_no]
        self.question_no += 1
        user_answer = input(f"Q.{self.question_no}. {que.get('question')} (true/false): ").capitalize()
        self.check_answer(user_answer, que.get('correct_answer'))

    def still_has_questions(self):
        return self.question_no < len(self.genre_question_set)

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print("Congrats you have got the correct answer")
        else:
            print("Oops ...This time you got it wrong")
            print(f"The Correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_no}\n")
