
#Enter Wins
print("Enter your wins and losses for your team:")

for i in range(6):
    results = input("")



if wins >= 5 :
  print("You are placed in group 1.")

elif wins >= 3 and win <= 4 :
  print("You are placed in group 2.")

elif wins >= 1 and win <= 2 :
  print("You are placed in group 3.")

elif wins <= 1 :
  print("You were eliminated from the tournament.")