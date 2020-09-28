# Zach Sheley

import random;

# rock-0 paper-1 scissors-2

def computer_choice():
  computerChoice = random.randint(0,2)
  print(f"Computer Choice: {computerChoice}")
  return computerChoice

def compare(user, computer):
  if user==computer:
    return("Tie")
  elif user==0 and computer==2 or user==1 and computer==0 or user==2 and computer==1:
    return("User")
  else:
    return("Computer")

def main():
  userChoice = int(input("Enter 0-Rock 1-Paper 2-Scissors "))
  print(f"Winner: {compare(userChoice, computer_choice())}")
  
if __name__== "__main__":
  main()
