
# Prompt for a Single Task:
# Ask the user to input a task description and save it into a task variable
# Prompt for the task’s priority (high, medium, low) and save it into a priority variable
# In a time_bound variable, Ask if the task is time-bound (yes or no)
# Process the Task Based on Priority and Time Sensitivity:
# Use a Match Case statement to react differently based on the task’s priority.
# Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
# Provide a Customized Reminder:
# Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
# A message should be ‘that requires immediate attention today!’

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task.")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a medium priority task that requires moderate attention!")
        else:
            print(f"Reminder: '{task}' is a medium priority task.")
    case 'low':
        if time_bound == 'yes':
            print(f"Reminder: '{task}' has low priority but is  time bound")
        else:
            print(f"Reminder: '{task} has low priority and is not time bound'")
    