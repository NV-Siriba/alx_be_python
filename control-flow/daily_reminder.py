task=input("Enter your task:")
priority=input("Priority (high/medium/low):")
timebound=input("Is it time-bound? (yes/no):")
match priority:
    case "high":
        #timebound if statement
        if priority=="high" and timebound=="yes":
            print( f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"reminder{task}is high priority but is not time bound")
    case "low":
        if priority=="low" and timebound=="no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note:{task} is a low priority level but time bound")
    case "medium":
        print("Medium priority task")
    case _:
        print ("unknown priority")
