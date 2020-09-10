# Author: Yeman Xu ybx5148@psu.edu
# Collaborator: Jiahui Lan jzl6335@psu.edu
# Collaborator: Daniel Mikita djm6907@psu.edu
# Collaborator: Chenkuan Liao czl5899@psu.edu
# Section: 1
# Breakout: 8

def getlettergrade(numbergrade):
  if numbergrade >= 93.0:
    lettergrade = "A"
  elif numbergrade >= 90.0:
    lettergrade = "A-"
  elif 90 >= numbergrade >= 87.0:
    lettergrade = "B+"
  elif 87 > numbergrade >= 83.0:
   lettergrade = "B"
  elif 83 > numbergrade >= 80:
   lettergrade = "B-"
  elif 80 > numbergrade >= 77:
   lettergrade = "C+"
  elif 77 > numbergrade >= 70:
   lettergrade = "C"
  elif 70 > numbergrade >= 60:
   lettergrade = "D"
  elif 60 > numbergrade >= 0:
   lettergrade = "F"
  return lettergrade

def run():
 numbergrade = float(input("Enter your CMPSC 131 grade: "))
 print(f"Your letter grade for CMPSC 131 is {getlettergrade(numbergrade)}.")

if __name__ == "__main__":
  run()