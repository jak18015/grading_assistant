import json
from grade_copy import Grade


def main():
    with open("rubric.json", encoding="utf-8") as rubric_file:
        rubric = json.load(rubric_file)

    grade = Grade(rubric)
    grade.grade()
    grade.grade_printout()


if __name__ == "__main__":
    main()