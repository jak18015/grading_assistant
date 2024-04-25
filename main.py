from assets import GradingAssistant, rubric


def main():
    rubric_data = rubric("assets/rubric.json")
    grade = GradingAssistant(rubric_data)
    grade.grade()
    grade.summarize()

    
if __name__ == "__main__":
    main()
