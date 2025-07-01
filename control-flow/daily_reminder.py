task=input("Enter your task:")
priority=input("Priority (high/medium/low):")
time_bound=input("Is it time-bound? (yes/no):")
match priority:
    case "high":
       Reminder=f"Reminder:{task} is a high priority task!"
       if time_bound=="yes":
           Reminder=f"Reminder: {task} is a high priority task that requires immediate attention today!"
       print(Reminder)
    case "low":
        if priority=="low" and time_bound=="no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note:{task} is a low priority level but time bound")
    case "medium":
        print("Medium priority task")
    case _:
        print ("unknown priority")
