from assets import Grade, rubric



def main():
    rubric_data = rubric("assets/rubric.json")
    grade = Grade(rubric_data)
    grade.grade()
    grade.grade_printout()
if __name__ == "__main__":
    main()