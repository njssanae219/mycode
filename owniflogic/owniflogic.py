#!/usr/bin/env python3
while True:
  viopoints = 0
  vio = input("Do you beat your kids?").lower()
  if vio == "no":
      viopoints += 2
      print("great, what a happy family")
  elif vio == "yes":
      viopoints += 1
      print("not a solution to teach your kids")
  else:
      viopoints += 0
      print("stay away from your kids")
  
  kidspoints = 0
  kids = int(input("How many children do you have?\n"))
  if kids == 2:
      kidspoints += 2
      print("an ideal number")
  elif kids == 1:
      kidspoints += 1
      print("should consider more")
  else:
    kidspoints += 0
    print("too bad")
  
  btimepoints = 0
  btime = int(input("in your house, bedtime is: \n"))
  if btime <= 9:
      btimepoints += 2
      print("great, a perfect time to tuck in your kids")
  elif btime > 9:
      btimepoints += 1
      print("kids need plenty sleep")
  else:
      btimepoints += 0
      print("too late for kids")
  
  phonepoints = 0
  phone = int(input("how many times a day do you let your kids to use cell phone? \n"))
  if phone <= 5:
      phonepoints += 2
      print("you are doing good")
  elif phone > 6:
      phonepoints += 1
      print("spend some time with your kids")
  else:
      phonepoints += 0
      print("take away the cell phone")
  
  toypoints = 0
  toy = int(input("how many toys do you let your kids pick out in a toy store? \n"))
  if toy >= 10:
      toypoints += 2
      print("you are awesome parent")
  elif toy <=2:
      toypoints += 1
      print("make some more money")
  else:
      toypoints += 0
      print("terrible terrible terrible parent")
  
  total_points = viopoints + kidspoints + btimepoints + phonepoints + toypoints  
  if total_points > 8:
      print("you are the best parent ever")
  elif total_points > 5:
      print("you are an average parent")
  else:
      print("damn, you're messed up")
  break
