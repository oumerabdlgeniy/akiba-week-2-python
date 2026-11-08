PIN=1234

for i in range(3):
   
        num=int(input("Enter your pin :  "))
        if num==PIN:
            print("Access Granted")
            break
        else:
          attempts_remaining= 3-(i+1)
          if attempts_remaining > 0:
            print(f"Incorrect PIN. Attempts remaining: {attempts_remaining}")
          else: 
            print("Incorrect PIN. Game Over!")