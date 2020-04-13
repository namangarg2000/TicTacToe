def show_board():
    print(board)

def check():
    pass

def player1_input():
   player1 = int(input("Enter position for player 1"))
   return player1

def player2_input():
    player2=int(input("Enter position for player 2"))
    return player2


board=['1','2','3','4','5','6' ,'7' ,'8' ,'9' ]

if __name__=='__main__':

    choice=input("Start the game?(y/n)")
    if(choice=='Y' or choice=='y'):
        
        print("Game starting")

        while(choice=='Y' or choice=='y'):
            board=['1','2','3','4','5','6' ,'7' ,'8' ,'9' ]
            player1=player1_input()

            board[player1-1]='X'
            check()
            show_board()

            choice=input("Start a new game?(y/n)")


    else:
        #print("Game end")
        exit(0)