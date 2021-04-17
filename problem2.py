#title
print(" ")
print("   ********Distance Caluclator********")
print("")

#travel log
print("           ****Travel Log****")
print(" ")

#Finding how many days
total = 0
days = 0

while total <= 100 :
  amount = int(input("How far did you drive for the day? "))
  total = total + amount
  days = days + 1


print(" ")
print("           ****summary****")

#summary
print("It took", days, "days to pass 100km drivin")