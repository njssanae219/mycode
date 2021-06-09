#!/usr/bin/env python3
points = 0

vio = input("Do you beat your kids?").lower()
if vio == "hell no": 
    points += 2
elif vio == "only a slap on their hand": 
    points += 1
else:
    points += 0

if points == 2:
   print("great, a happy family")
elif points == 1:
   print("")
else:
   print("stay away from your kids")

kids = int(input("How many children do you have?"))
if kids == 2:
    points += 2
elif kids == 1:
    points += 1
else:
    points += 0

if points == 2:
   print("An ideal number")
elif points == 1:
   print("Should consider more")
else:
   print("Too bad")

btime = int(input("In your house, bedtime is: "))
if btime <= 9:
    points += 2
elif btime >= 9:
    points += 1
else:
   points += 0

if points == 2:
    print("Great, a perfect time to tuck in your kids")
elif points == 1:
    print("Kids need plenty sleep")
else:
    print("Too late for kids")


