import random
choice: dict[str,str] ={'Rock' : '🪨',
                        'Paper' : '📃' ,
                        'Scissor': '✂️'}
player_score = 0
computer_score = 0
while True:
    print(f"\n------🏁 Your Score: {player_score} Vs Computer Score: {computer_score}------🏁")
    player_choice: str = input('Choose Rock(🪨), Paper(📃) or Scissor(✂️): ').strip().capitalize()

    if player_choice not in choice:
        print(f"'{player_choice}' is an invalid choice 🚫. Please select from the given options only!!.")
        continue
    computer_choice: str = random.choice(tuple(choice))
    print('\nResults')
    print("--------------->")
    print(f"You called:               {choice[player_choice]} {player_choice} ")
    print(f"Computer callled:         {choice[computer_choice]} {computer_choice} ")
    print("---------------->")

    if player_choice == computer_choice:
        print("It's a tie")
        computer_score +=1
    elif player_choice == 'Scissor' and computer_choice == 'Rock':
        print('Computer wins 💻!')
        computer_score +=1
    elif player_choice == 'Rock' and computer_choice == 'Paper':
        print('Computer wins 💻!')
        computer_score +=1
    elif player_choice == 'Paper' and computer_choice == 'Scissor':
        print('Computer wins 💻!')
        computer_score +=1
    else:
        print("You win 🚀!!")
        player_score +=1
    print("===============================")
