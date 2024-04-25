class Grade:
    def __init__(self, rubric):
        self.rubric = rubric
        self.criteria = list(rubric.keys())
        self.pt_poss = list(rubric.values())
        self.grade_values = []
        self.critiques = []

    def grader(self):
        for crit, pt_poss in zip(self.criteria, self.pt_poss):
            print(f"{crit} ({pt_poss} points)")
            points = self._get_valid_points(pt_poss)
            critiques = self._get_critiques(points, pt_poss)
            self.grade_values.append(points)
            self.critiques.append(critiques)
        return self.grade_values

    def grade_printout(self):
        for crit, points, critiques in zip(self.criteria,
                                           self.grade_values,
                                           self.critiques):
            self._print_criteria(crit, points, critiques)
        self._print_final_score()

    def _get_valid_points(self, pt_poss):
        while True:
            points = int(input(f"Enter num of points btw 0 and {pt_poss}: "))
            if 0 <= points <= pt_poss:
                return points

    def _get_critiques(self, points, pt_poss):
        if points < pt_poss:
            return input("Reason for missing points: ")
        return ""

    def _print_criteria(self, crit, points, critiques):
        if critiques:
            print(f"{crit}\n{points}/{self.pt_poss}: {critiques}")
        else:
            print(f"{crit}\n{points}/{self.pt_poss}")

    def _print_final_score(self):
        tot_points = sum(self.grade_values)
        tot_poss = sum(self.pt_poss)
        print(f"Final score:\n{tot_points}/{tot_poss}")


