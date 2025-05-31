print("--- Personal Daily Reminder ---")

task = input("Enter your task: ").strip()
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

final_prefix = ""
core_message = ""
time_sensitive_addon = ""

match priority:
	case 'high':
	    final_prefix = "Urgent Reminder: "
	    core_message = f"'{task}' is a HIGH priority task"
	
	case 'medium':
	    final_prefix = "Reminder: "
	    core_message = f"'{task}' is a medium priority task"
		
	case 'low':
	    final_prefix = "Note: "
	    core_message = f"'{task}' is a low priority task."
		
	case _:
		print("Invalid priority entered. Defaulting to 'medium'.")
		final_prefix = "Reminder: " # Also use "Reminder:" for invalid default
		core_message = f"'{task}' is a medium priority task"
		
if time_bound == 'yes':
	time_sensitive_message = " that requires immediate attention today!"

elif time_bound == 'no' and priority == 'low':
	time_sensitive_message = " Consider completing it when you have free time."

elif time_bound == 'no':
    time_sensitive_addon = " to complete today."
	
print(f"{final_prefix}{core_message}{time_sensitive_addon}")