total = int(input("Total classes till now: "))
attended = int(input("Classes attended: "))
if(total>=attended):
    goal = 80
    count = 0
    percentage = (attended/total)*100
    print("Percentage: ",round(percentage),"%")
    if (round(percentage) == goal):
        print("--->It's exactly ", goal, "%, don't miss your classes ^^")
    if(round(percentage)<goal):
        while(round(percentage)<goal):
            total = total + 1
            attended = attended + 1
            percentage = (attended / total) * 100
            count = count + 1
        print("--->You need to attend ",count,"classes   (",count//4,"Days and ",count%4,"Classes)")
    if(round(percentage)>goal):
        while(round(percentage)>goal):
            total = total + 1
            percentage = (attended / total) * 100
            if(round(percentage)>goal):
                count = count + 1
        print("--->You can skip ",count," classes   (",count//4,"Days and ",count%4,"Classes)")
else:
    print("---Invalid Input---\nLogic left the chat...")
