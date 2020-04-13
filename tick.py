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
        
        

        while(choice=='Y' or choice=='y'):
            print("Game starting")
            board=['1','2','3','4','5','6' ,'7' ,'8' ,'9' ]
            while(True):

                player1=player1_input()
                board[player1-1]='X'
                show_board()
                if(check()):
                    print("Player 1 wins")
                    break
                
                player2=player2_input()
                board[player2-1]='O'
                show_board()
                if(check()):
                    print("Player 2 wins")
                    break

            choice=input("Start a new game?(y/n)")
            

    else:
        print("Game Ending")
        exit(0)