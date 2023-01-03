number = 4
count = 1
print("guess a number between 1 and 10 ")
guess = int(input())
while guess != number:
    count = count + 1
    print("incorrect")
    number = 4
    print("guess a number between 1 and 10")
    guess = int(input())
print("correct")
print("guesses = ", count )
