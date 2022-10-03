'''
Tic-Tac-Toe game with basics of python.
'''


from time import sleep
import random as r


#Welcoming user.
user = input("Enter your name : ")
print(f"Hey,{user} welcome to tictactoe game!")


#Initialisation stuff.
choices = list(range(1,10)) #All the choices 1-9.

Conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7),
              (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)] #Conditions for winning.

d = dict(zip(choices,"_"*9)) #Backend board for the game.

#Choosing whos X and O.
user_c = ''

while user_c not in ['X', 'O']:
    user_c = input("Choose X or O : ")
if user_c == 'X':
    comp_c = 'O'
elif user_c == 'O':
    comp_c = 'X'


#Printing board (Frontend board)
print(
f'''        ___________
       | 1 | 2 | 3 |
       |___________|
       | 4 | 5 | 6 |
       |___________|
       | 7 | 8 | 9 |
        -----------''')


#Real mechanism
user_choice = 0

def printer():
    print(
                f'''                    ___________
                    | {d[1]} | {d[2]} | {d[3]} |
                    |___________|
                    | {d[4]} | {d[5]} | {d[6]} |
                    |___________|
                    | {d[7]} | {d[8]} | {d[9]} |
                    -----------
            ''')


def check():
    for i in Conditions:
        if d[i[0]] == d[i[1]] == d[i[2]]: #Winner is found
            if d[i[0]] == comp_c: #Computer is winner
                print("Computer wins!")
                return True
                break
            elif d[i[0]] == user_c: #User is winner
                print(f"{user} wins!")
                return True
                break


while choices:


    user_choice = input("Enter your choice : ") #Taking user's input

    if user_choice.isnumeric(): #First checking of  user's input
        user_choice = int(user_choice)

        if user_choice in choices: #Second checking of user's input

            #Updating the board
            d[user_choice] = user_c
            choices.remove(user_choice)

            print(f"{user} playes {user_c} at {user_choice}")
            printer()
            if check():
                break

            sleep(3)

            comp_choice = r.choice(choices)
            d[comp_choice] = comp_c
            choices.remove(comp_choice)

            print(f"Computer playes {comp_c} at {comp_choice}")
            printer()
            if check():
                break




            #Handling the wrong inputs of user.
        else:
            print("Enter an appropriate choice between 1-9 which is available.")
    else:
        print("Enter an appropriate choice between 1-9.")


#Thanking the player for playing this game.
print(f"{user}, Thank You for playing in this game.")
