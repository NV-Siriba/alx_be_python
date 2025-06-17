task=input("Enter your task:")
priority=input("Priority (high/medium/low):")
time=input("Is it time-bound? (yes/no):")
match priority:
    case "high":
       reminder=f"Reminder:{task} is a high priority task!"
       if time=="yes":
           reminder=f"Reminder: {task} is a high priority task that requires immediate attention today!"
       print(reminder)
    case "low":
        if priority=="low" and time=="no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note:{task} is a low priority level but time bound")
    case "medium":
        print("Medium prioty task")
    case _:
        print ("unknown priority")