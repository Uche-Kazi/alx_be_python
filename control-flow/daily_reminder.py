print("--- Personal Daily Reminder ---")

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

time_sensitive_addon = ""
if time_bound == 'yes':
	time_sensitive_addon = " that requires immediate attention today!"
elif time_bound == 'no' and priority == 'low':
	time_sensitive_addon = " Consider completing it when you have free time."
elif time_bound == 'no':
	time_sensitive_addon = " to complete today."

match priority:
	case 'high':
		print(f"Urgent Reminder: '{task}' is a HIGH priority task{time_sensitive_addon}")
	case 'medium':
		print(f"Reminder: '{task}' is a medium priority task{time_sensitive_addon}")
	case 'low':
		print(f"Note: '{task}' is a low priority task.{time_sensitive_addon}")
		print("Invalid priority entered. Defaulting to 'medium'.")
		print(f"Reminder: '{task}' is a medium priority task{time_sensitive_addon}")