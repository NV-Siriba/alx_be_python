task=input("Enter your task:")
prioty=input("Priority (high/medium/low):")
time=input("Is it time-bound? (yes/no):")
match prioty:
    case "high":
        if prioty=="high" and time=="yes":
            print( f"Reminder: {task} is a high priority task that requires immediate attention today!")
        else:
            print(f"reminder{task}is high priority but is not time bound")
    case "low":
        if prioty=="low" and time=="no":
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note:{task} is a low priority level but time bound")
    case "medium":
        print("Medium prioty task")
    case _:
        print ("unknown priority")