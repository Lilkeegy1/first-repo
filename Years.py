start = int(input("In which year did you start 1st grade? "))
print("Assuming you didn't skip or repeat any grade: ")
if start+5 < 2026:  # If started before 2026
    print(f" - You started middle school (6th grade) in {start+5}")
else:  # Starts after 2026
    print(f" - You will start middle school (6th grade) in {start+5}")
if start+8 < 2026:  # Started before 2026
    print(f" - You started high school (9th grade) in {start+8}")
else:  # Starts after 2026
    print(f" - You will start high school (9th grade) in {start+8}")
if start+12 < 2026:  # Finished before 2026
    print(f" - You finished high school (and maybe start college) in {start+12}")
else:  # Finishes after 2026
    print(f" - You will finish high school (and maybe start college) in {start+12}")
