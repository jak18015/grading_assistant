import json
import os
with open("assets/answer_dict.json", "r") as answer_file:
    answer_dict = json.load(answer_file)
with open("assets/score_dict.json", "r") as score_file:
    score_dict = json.load(score_file)

questions = list(score_dict.keys())
scores = list(score_dict.values())
answers = list(answer_dict.values())

for i in range(len(questions)):
    os.system('clear')
    print(questions[i])
    print(f'worth {scores[i]} points')
    print(f'answer: {answers[i]}')
    waiter = input('press enter to continue...')