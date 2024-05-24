# Study Scheduler

This Python script provides an interactive way to create a personalized study schedule based on the subjects you want to study, their respective priorities, and the amount of time you can dedicate to studying each day. It calculates how much time you should spend on each subject over a week.

## Features

- **Interactive Input**: Enter your subjects and set their priorities interactively.
- **Customizable Study Hours**: Define how many hours you plan to study each day.
- **Priority-Based Scheduling**: Allocate weekly study hours for each subject based on its priority.
- **Error Handling**: Ensures that inputs are valid with helpful error messages.

## Requirements

To run this script, you will need Python 3.x installed on your machine.

## Usage

1. Clone the repository or download the script to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using the command:
   ```
   python study_scheduler.py
   ```
5. Follow the on-screen prompts to input your subjects, their priorities, and your available daily study hours.

## Input Instructions

- **Subjects**: Enter the subjects separated by a comma. Example: Math, Physics, Chemistry.
- **Priorities**: Assign a priority to each subject (1 = lowest priority, 5 = highest priority).
- **Study Hours**: Input the average number of hours you plan to study each day. This should be a positive integer.

## Output

The script will calculate and display how many hours per week you should ideally spend on each subject based on the priorities you set and your available study time.

## Example

Here's an example of what the interaction might look like:

```
[Input] Please enter the subjects you want to include in your study cycle (separated by comma): Math, Physics, Chemistry
[~] Math (1 - 5): 5
[~] Physics (1 - 5): 3
[~] Chemistry (1 - 5): 2
[Input] How many hours on average do you plan to study every day? 4

[Info] Let's review your data until now.
[Info] Math -> Priority: 5
[Info] Physics -> Priority: 3
[Info] Chemistry -> Priority: 2

[Input] And you're planning to study 28 hours per week (4h/day), is that correct? (Y/n) Y

[Info] Final result:
Math -> 15h per week
Physics -> 9h per week
Chemistry -> 4h per week
```

Feel free to modify and adapt the script to better fit your scheduling needs!
