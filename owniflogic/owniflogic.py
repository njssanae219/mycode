#!/usr/bin/env python3
viopoints = 0
vio = input("Do you beat your kids?\n").lower()
if vio == "hell no": 
    points += 2
    print("great, what a happy family")
elif vio == "only a slap on their hand": 
    points += 1
    print("not a solution to teach your kids")
else:
    points += 0
    print("stay away from your kids")

kidspoints = 0
kids = int(input("How many children do you have?\n"))
if kids == 2:
    points += 2
    print("an ideal number")
elif kids == 1:
    points += 1
    print("should consider more")
else:
    points += 0
    print("too bad")

btimepoints = 0
btime = int(input("in your house, bedtime is: \n"))
if btime <= 9:
    points += 2
    print("great, a perfect time to tuck in your kids")
elif btime >= 9:
    points += 1
    print("kids need plenty sleep")
else:
   points += 0
   print("too late for kids)




