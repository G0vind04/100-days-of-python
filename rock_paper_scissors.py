rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("hello")
user=int(input("enter 0 for rock,1 for paper,2 for scissor"))
if user==0:
    print(rock)
elif user==1:
    print(paper)
elif user==2:
    print(scissors)
else:
    print("give valid input")

list1=[0,1,2]
output=random.choice(list1)

if output==0:
    print("CPU chose rock")
    print(rock)
elif output==1:
    print("CPU chose paper")
    print(paper)
else:
    print("CPU chose scissors")
    print(scissors)


if user==0 and output==2:
    print("YOU WIN!!")
elif user==1 and output==0:
    print("YOU WIN!!")
elif user==2 and output==0:
    print("YOU LOST. BETTER LUCK NEXT TIME ;)")
elif user==0 and output==1:
    print("YOU LOST. BETTER LUCK NEXT TIME ;)")
elif user==1 and output==2:
    print("YOU LOST. BETTER LUCK NEXT TIME ;)")
elif user==2 and output==1:
    print("YOU WIN!!")

if user==0 and output==0:
    print("Match Drawn.")
elif user==1 and output==1:
    print("Match Drawn.")
elif user==2 and output==2:
    print("Match Drawn.")

elif user>3 and output>3:
    print("invalid inputs")
    
