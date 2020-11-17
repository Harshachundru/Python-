import random
colors = ["green", "orange", "red", "blue", "black", "white", "purple"]

while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("Guess the color:")

    while True:
        if color == guess:
            break
        else:
            guess = input("Your wrong!, guess again:")
            
    print("You guessed the color and it is :",color)

    play_again= input("Let's play again? type 'no' to quit:")
    if play_again.lower()== 'no':
         break

print("It was fun thanks for playing")
        
     

