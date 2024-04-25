import time
import json
from statistics import mean
from assets import GradingAssistant, rubric


def main():
    time_start = time.time()

    rubric_data = rubric("assets/sep_of_proteins_2_3.json")
    assistant = GradingAssistant(rubric_data)
    assistant.iterate_over_dictionary(assistant.rubric_dict)
    assistant.summarize()
    
    time_end = time.time()
    duration = round((time_end - time_start)/60, 1)
    print(f'\n{duration} minutes')
    
    with open('time_log.json', mode='r', encoding='utf-8') as time_file:
        time_log: list = json.load(time_file)
        time_log.append(duration)
    with open('time_log.json', mode='w', encoding='utf-8') as time_file:
        json.dump(time_log, time_file, indent=4)

    print(f'Avg time: {round(mean(time_log), 1)} minutes')
    # assistant.debug()
    
if __name__ == "__main__":
    main()
