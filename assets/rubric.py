import json

def rubric(path):
    rubric_dict = {}
    with open(path, encoding="utf-8") as rubric_file:
        rubric_dict = json.load(rubric_file)
    return rubric_dict