from os import system,name

def clear():
    #for windows
    if name =='nt':
        _ = system('cls')
    #for linux
    else:
        _ = system('clear')


def show_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print(f"-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print(f"-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


def check(a):
    if(a[0]==a[1] and a[1]==a[2]):
        return True
    elif(a[3]==a[4] and a[4]==a[5]):
        return True
    elif(a[6]==a[7] and a[7]==a[8]):
        return True
    elif(a[0]==a[3] and a[3]==a[6]):
        return True    
    elif(a[1]==a[4] and a[4]==a[7]):
        return True
    elif (a[2]==a[5] and a[5]==a[8]):
        return True
    elif (a[0]==a[4] and a[4]==a[8]):
        return True
    elif (a[2]==a[4] and a[4]==a[6]):
        return True
    else:
        return False

def boardfull(a):
    for i in range(9):
        if((a[i]==1 or a[i]==2 or a[i]==3 or a[i]==4 or a[i]==5 or a[i]==6  or a[i]==7 or a[i]==8 or a[i]==9)):
            return False
            
    return True
            
def player1_input():
   player1 = int(input("Enter position for player 1:"))
   while(player1<1 or player1>9 ):
        player1=int(input("Enter a valid position"))

   return player1

def player2_input():
    player2=int(input("Enter position for player 2:"))
    while(player2<1 or player2>9 ):
        player2=int(input("Enter a valid position:"))
    return player2

if __name__=='__main__':

    choice=input("Start the game?(y/n)")
    if(choice=='Y' or choice=='y'):
        
        

        while(choice=='Y' or choice=='y'):
            print("Game starting")
            board=[1,2,3,4,5,6,7,8,9]
            show_board(board)
            while(True):

                player1=player1_input()
                board[player1-1]='X'
                #print('\n'*100)
                clear()
                show_board(board)
                if(check(board)):
                    print("------Player 1 wins------")
                    break

                elif(boardfull(board)):
                    print("------Draw------")
                    break
                   
                player2=player2_input()
                board[player2-1]='O'
                #print('\n'*100)
                clear()
                show_board(board)
                if(check(board)):
                    print("------Player 2 wins------")
                    break
                elif(boardfull(board)):
                    print("------Draw------")
                    break
                

            choice=input("Start a new game?(y/n)")
            if(choice=='y' or choice=='Y'):
                print('\n'*100)
        print("Game Ending")    

    else:
        exit(0)