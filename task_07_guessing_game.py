
import random
Secret_num=random.randint(1,10)
for i in range(5):
   num=int(input("Enter Your Guessing Number: "))
   if Secret_num==num:
       print(f"Congratulations! You guessed the number in {i+1}attempts.")
   elif i  == 5:
       print("Game Over !")
      
   else: 
       print("Please try again!")
      