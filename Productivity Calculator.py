# user inputs on how they spent their day
sleep = int(input("Enter how many hours you slept today: "))
eat = int(input("Enter how many hours you spent eating today: "))
work = int(input("Enter how many hours you worked today: "))
exercising = int(input("Enter how many hours you exercised today: "))
electronics = int(input("Enter how many hours you used electronics today: "))
study = int(input("Enter how many hours you studied today: "))

# calculates productivity score or gives error message
if (sleep + eat + work + exercising + electronics + study) == 24:
    p_score = float(work + exercising + study)*1.2 - float(sleep + eat + electronics)

    # outputs whether the day was productive
    if (p_score >= 0):
        print("You had a productive day today")
    else:
        print("Today was not a productive day for you")
else:
    print("Hours in day must add up to 24")

