import math

def main():
    while True:
        # Input the subjects
        subjects_input = input("[Input] Please enter the subjects you want to include in your study cycle (separated by comma): ")
        subjects = [subject.strip() for subject in subjects_input.split(',') if subject.strip()]

        # Check if the list of subjects is empty after cleaning
        if not subjects:
            print("[Error] No valid subjects entered. Please try again.")
            continue

        print("[Info] 1 = lowest priority, 5 = highest priority")
        
        # Collect priorities for each subject
        priority_map = {}
        for subject in subjects:
            while True:
                try:
                    priority = int(input(f"[~] {subject} (1 - 5): "))
                    if 1 <= priority <= 5:
                        priority_map[subject] = priority
                        break
                    else:
                        print("[Error] Priority must be between 1 and 5.")
                except ValueError:
                    print("[Error] Invalid input. Please enter a number between 1 and 5.")

        # Average daily study hours
        while True:
            try:
                daily_hours = int(input("[Input] How many hours on average do you plan to study every day? "))
                if daily_hours > 0:
                    break
                else:
                    print("[Error] Study hours must be a positive number.")
            except ValueError:
                print("[Error] Invalid input. Please enter a valid number.")

        weekly_hours = daily_hours * 7
        print("\n[Info] Let's review your data until now.")
        for subject, priority in priority_map.items():
            print(f"[Info] {subject} -> Priority: {priority}")

        # Confirmation to proceed
        confirm = input(f"[Input] And you're planning to study {weekly_hours} hours per week ({daily_hours}h/day), is that correct? (Y/n) ").lower()
        if confirm == 'n':
            print("[Info] Let's start over.")
            continue
        
        break

    # Calculate the total priority sum
    total_priority = sum(priority_map.values())
    hour_multiplier = weekly_hours / total_priority

    # Calculating weekly hours for each subject
    final_schedule = {subject: math.ceil(priority * hour_multiplier) for subject, priority in priority_map.items()}

    print('\n[Info] Final result:')
    for subject, hours in final_schedule.items():
        print(f'{subject} -> {hours}h per week')

if __name__ == '__main__':
    main()
