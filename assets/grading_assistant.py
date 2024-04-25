class GradingAssistant:
    def __init__(self, rubric_dict):
        self.criteria = list(rubric_dict.keys())
        self.points_poss = list(rubric_dict.values())
        self.grade_values = []
        self.critiques = []

    def grade(self):
        print("\n\n\n")
        for criterion, points_possible in zip(self.criteria,
                                             self.points_poss):
            self._print_criterion(criterion, points_possible)
            points = self._get_valid_points(points_possible)
            critique = self._get_critiques(points, points_possible)
            self.grade_values.append(points)
            self.critiques.append(critique)

        return self.grade_values

    def _print_criterion(self, criterion, points_possible):
        print(f"{criterion} ({points_possible} points)")

    def _get_valid_points(self, points_possible):
        while True:
            try:
                points: float = float(input(f"0-{points_possible} points: "))
                if 0 <= points <= points_possible:
                    return points
            except ValueError:
                print("Error: Invalid input, try again...\n")

    def _get_critiques(self, points, points_possible):
        if points < points_possible:
            return input("Reason: ")
        return ""    

    def summarize(self):
        print("\n\n\nGRADE SUMMARY\n")
        for i, (criterion, grade, critique) in enumerate(
                zip(self.criteria, self.grade_values, self.critiques)):
            points_possible = self.points_poss[i]
            if not critique:
                print(f"{criterion}\n   {grade}/{points_possible}")
            elif critique:
                print(f"{criterion}\n   {grade}/{points_possible}: {critique}")
            else:
                ValueError

        final_score = sum(self.grade_values)
        total_points = sum(self.points_poss)

        if total_points == 0:
            print("Error: Total points is zero")
        else:
            print(f"\nFinal score:\n{final_score}/{total_points}"
                  f"({final_score/total_points:.2%})")
