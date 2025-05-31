print("--- Personal Daily Reminder ---")

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

base_reminder = f"Reminder: '{task}' is a {priority} priority task"
time_sensitive_message = ""

match priority:
	case 'high':
		base_reminder = f"Urgent Reminder: '{task}' is a HIGH priority task"
	case 'medium':
		base_reminder = f"Heads Up: '{task}' is a medium priority task"
	case 'low':
		base_reminder = f"Note: '{task}' is a low priority task."
	case _:
		print("Invalid priority entered. Defaulting to 'medium'.")
		base_reminder = f"Heads Up: '{task}' is a medium priority task"

if time_bound == 'yes':
	time_sensitive_message = " that requires immediate attention today!"

elif time_bound == 'no' and priority == 'low':
	time_sensitive_message = " Consider completing it when you have free time."

elif time_bound == 'no':
	time_sensitive_message = " to complete today."

print(base_reminder + time_sensitive_message)
