num = int(input("Enter number 1: "))

Max = num
Min = num
Sum = num
odd_Count = 0
even_Count = 0

if num % 2 == 0:
    even_Count += 1
else:
    odd_Count += 1

for i in range(2, 11):
    num = int(input(f"Enter number {i}: "))

    Sum += num

    if num > Max:
        Max = num

    if num < Min:
        Min = num

    if num % 2 == 0:
        even_Count += 1
    else:
        odd_Count += 1

avg = Sum / 10

print("Largest number:", Max)
print("Smallest number:", Min)
print("Total sum:", Sum)
print("Average:", avg)
print("Even numbers:", even_Count)
print("Odd numbers:", odd_Count)