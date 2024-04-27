class GradingAssistant:
    def __init__(self, rubric_dict):
        self.rubric_dict = rubric_dict
        self.grade_values = dict({})
        self.critiques = dict({})
        self.depth = 2
    def iterate_over_dictionary(self, d):
        if not isinstance(d, dict):
            return None
        for key, value in d.items():
            if isinstance(key, dict):
                self.depth += 1
                self.iterate_over_dictionary(key)
            else:
               self.grader(key, value)

    def grader(self, header, dictionary):
        print(f'\n{header}')
        self.grade_values[header] = {}
        self.critiques[header] = {}
        for key, value in dictionary.items():
            self._print_criterion(key, value)
            points = self._get_valid_points(value)
            critique = self._get_critiques(points, value)
            self.grade_values[header][key] = points
            self.critiques[header][key] = critique

    def _print_criterion(self, criterion, points_possible):
        print(f"{criterion} ({points_possible} points)")

    def _get_valid_points(self, points_possible):
        while True:
            try:
                points = float(input(f"0-{points_possible} points: "))
                if isinstance(points, float) and 0 <= points <= points_possible:
                    if points % 1 == 0:
                        return int(points)
                    else:
                        return points
            except ValueError:
                print("Error: Invalid input, try again...\n")
            except TypeError:
                print("Error: Invalid input, try again...\n")

    def _get_critiques(self, points, points_possible):
        if points < points_possible:
            return input("Reason: ")
        return ""    

    def summarize(self):
        final_score: int = 0
        total_points: int = 0
        for keys_0 in self.rubric_dict:
            print(f'{keys_0}')
            for keys_1 in self.rubric_dict[keys_0]:
                print(f'    {keys_1}\n',
                      f'        ',
                      f'{self.grade_values[keys_0][keys_1]}',
                      f'/',
                      f'{self.rubric_dict[keys_0].get(keys_1)}',
                      f'{self.critiques[keys_0][keys_1]}'
                      )
                final_score += self.grade_values[keys_0].get(keys_1)
                total_points += int(self.rubric_dict[keys_0].get(keys_1))
        
        if final_score % 1 == 0:
            final_score = int(final_score)

        print(f'Final score:',
              f'{final_score}/{total_points} ({final_score/total_points:.2%})')

    def debug(self):
        final_score: float = 0
        total_points: int = 0
        for keys_0 in self.rubric_dict:
            for keys_1 in self.rubric_dict[keys_0]:
                print(f'{self.grade_values[keys_0].get(keys_1)}')
                print(f'type: {type(self.grade_values[keys_0].get(keys_1))}')