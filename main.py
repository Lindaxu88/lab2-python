# Author: Yeman Xu ybx5148@psu.edu
# Collaborator: Jiahui Lan jzl6335@psu.edu
# Collaborator: Daniel Mikita djm6907@psu.edu
# Collaborator: Chenkuan Liao czl5899@psu.edu
# Section: 1
# Breakout: 8

def getLetterGrade(grade):
  if (grade >= 93.0):
    lettergrade = "A"
  elif (grade >= 90.0 and grade<93.0):
    lettergrade = "A-"
  elif (grade >=87.0 and grade<90.0):
    lettergrade = "B+"
  elif (grade >=83.0 and grade<87.0):
    lettergrade = "B"
  elif (grade >=80.0 and grade<83.0):
    lettergrade = "B-"
  elif (grade >=77.0 and grade<80.0):
    lettergrade = "C+"
  elif (grade >=70.0 and grade<77.0):
    lettergrade = "C"
  elif (grade >=60.0 and grade<70.0):
    lettergrade = "D"
  else:
    lettergrade = "F"
  return lettergrade

def run():
   letter = getLetterGrade (float(input("Enter your CMPSC 131 grade: ")))
   print(f"Your letter grade for CMPSC 131 is {letter}.")
if __name__ == "__main__":
  run()