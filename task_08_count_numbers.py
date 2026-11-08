num=int(input("Please Enter Number: "))
CountEven=0
CountOdd=0
Sum=0
for i in range(1,num+1):
   Sum+=i
   if i%2==0:
    CountEven+=1
   else:
    CountOdd+=1
print(f"Count of Even Numbers: {CountEven}")
print(f"Count of Odd Numbers: {CountOdd}") 
print(f"Sum of Numbers: {Sum}")
    
  