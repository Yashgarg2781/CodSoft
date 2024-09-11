import random
rock="🪨"
paper="📃"
scissor="✂️"
game_images=[rock,paper,scissor]
user_choice=int(input("Enter your choice : Type 0 for rock ,1 for paper and 2 for scissor. "))
if user_choice>=3 or user_choice<0:
    print("Invalid input. You loose..")
else:
     print(f"User choose: {game_images[user_choice]}")
     computer_choice=random.randint(0,2)
     print(f"Computer choose: {game_images[computer_choice]}")
     if user_choice==computer_choice:
         print("The game is draw.")
     elif user_choice==2 and computer_choice==0:
         print("Computer wins.")
     elif user_choice==0 and computer_choice==2:
         print("User wins.")
     elif user_choice>computer_choice:
         print("User wins.")
     elif user_choice<computer_choice:
         print("Computer wins.")