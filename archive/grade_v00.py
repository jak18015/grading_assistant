class Grade:
    def __init__(self, rubric):
        self.rubric = rubric
        self.criteria = list(self.rubric.keys())
        self.points_possible = list(self.rubric.values())
        self.grade_values: list = []
        self.critiques: list = []
        self.points = ''
        self.critique = ''

    def grader(self):
        print("\n")
        for x in range(len(self.criteria)):
            print(f"{self.criteria[x]} ({self.points_possible[x]} points)")
            self.points = int(input(f"0-{self.points_possible[x]} pts: "))
            while not 0 <= self.points <= self.points_possible[x]:
                if self.criteria[x] == 'Other:':
                    break
                self.points = int(input("try again."))
            if self.points < self.points_possible[x]:
                self.critique = input("reason for missing points: ")
            self.critiques.append(self.critique)
            self.grade_values.append(self.points)
        return self.grade_values

    def grade_printout(self):
        print("\n\n\nGRADE PRINTOUT\n")
        for x in range(len(self.criteria)):
            if not self.critiques[x] == "":
                print(
                    f"{self.criteria[x]}\n"
                    + f"    "
                    + f"{self.grade_values[x]}/{self.points_possible[x]}:"
                    + f"    "
                    + f"{self.critiques[x]}"
                )
            else:
                print(
                    f"{self.criteria[x]}\n"
                    + f"    "
                    + f"{self.grade_values[x]}/{self.points_possible[x]}"
                )
        print("Final score: ")
        print(f"{sum(self.grade_values)} / {sum(self.points_possible)}")

