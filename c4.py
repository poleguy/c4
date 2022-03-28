#qpy:qpyapp

# Originally written by Carmen Dietz and Nicholas Dietz on a mobile phone.
# 



print("enter 1-7 to drop a piece")
print("enter u to undo previous moves")
print("enter r to redo previously undone moves")
print("enter s to swap sides... not implemented: you can just play the other person's turn.")
print("enter q to quit")

def print_m1(m):
    for i in range(6):
        print(m[i])
        
def print_m(m):
    print(" 1 2 3 4 5 6 7")
    for i in range(6):
        print("|",end='')
        for j in range(7):
            if m[i][j] == 0:
                print(' |',end='')
            else:            
                #print('%d|'%m[i][j],end='')
                CRED    = '\33[31m'
                CYELLOW    = '\33[33m'
                CREDBG    = '\33[41m'
                CGREENBG  = '\33[42m'
                CYELLOWBG = '\33[43m'
                CEND      = '\33[0m'

                if m[i][j] == 1:
                    print(CREDBG+'C'+CEND+'|',end='')
                    
                else:
                    print(CYELLOWBG+'N'+CEND+'|',end='')
        print('')

def drop(m,n,p):
    for i in range(6):
        j = 5-i
        if m[j][n] == 0:
            m[j][n] = p
            return m
    raise ValueError
     
def input_n():
    while True:
        x = input()
        if x in ["1","2","3","4","5","6","7"]:
            return int(x)-1
        elif x in ["u","r","s","c","q"]:
            # undo, redo, swap, clear, quit
            return x
        else:
            raise ValueError("invalid input")

def on_win(n,m):
    print("%s wins!"%n)
    
def win(m):
    ds = [[(0,5),(1,5),(2,5),(3,5),(4,5),(5,5),(6,5)],
    [(0,4),(1,4),(2,4),(3,4),(4,4),(5,4),(6,4)],
    [(0,3),(1,3),(2,3),(3,3),(4,3),(5,3),(6,3)],
    [(0,2),(1,2),(2,2),(3,2),(4,2),(5,2),(6,2)],
    [(0,1),(1,1),(2,1),(3,1),(4,1),(5,1),(6,1)],
    [(0,0),(1,0),(2,0),(3,0),(4,0),(5,0),(6,0)],
    [(5,0),(5,1),(5,2),(5,3),(5,4),(5,5)],
    [(4,0),(4,1),(4,2),(4,3),(4,4),(4,5)],
    [(3,0),(3,1),(3,2),(3,3),(3,4),(3,5)],
    [(2,0),(2,1),(2,2),(2,3),(2,4),(2,5)],
    [(1,0),(1,1),(1,2),(1,3),(1,4),(1,5)],
    [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5)],
    
    [(3,5),(4,4),(5,3),(6,2)],
    [(2,5),(3,4),(4,3),(5,2),(6,1)],
    [(1,5),(2,4),(3,3),(4,2),(5,1),(6,0)],
    [(0,5),(1,4),(2,3),(3,2),(4,1),(5,0)],
    [(0,4),(1,3),(2,2),(3,1),(4,0)],
    [(0,3),(1,2),(2,1),(3,0)],

       
    [(3,0),(4,1),(5,2),(6,3)],
    [(2,0),(3,1),(4,2),(5,3),(6,4)],
    [(1,0),(2,1),(3,2),(4,3),(5,4),(6,5)],
    [(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)],
    [(0,1),(1,2),(2,3),(3,4),(4,5)],
    [(0,2),(1,3),(2,4),(3,5)]]

    for player in [1,2]:
        count= 0 
        for d in ds:
            count = 0
            for p in d:
                #print("p0 %d" %p[0])
                v = m[p[1]][p[0]]
                #print(v)
                if v == player:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    w = 1
                    return player
    return 0
                    
                
    #print(m)
m = [[0,0,0,0,0,2,0],
     [0,0,0,0,0,1,0],
     [0,0,0,0,2,1,0],
     [0,0,0,0,2,1,0], 
     [0,0,0,1,2,2,0],
     [0,0,1,1,2,1,0]]
     
def undo(m,n):
    for i in range(6):
        if m[i][n] != 0:
            m[i][n] = 0
            return m

   
def m_init():  
    m = [[0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0], 
         [0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0]]
    return m

     
#win(m)

def main():
    try:
        moves=[]
        redo_list=[]
        p = [" "," "]
        p[0] = "Carmen"
        p[1] = "Nick"
        m = m_init()
        player=0
        last=7
        n=0
        print_err = False
        while True:
            print_m(m)
            if win(m) > 0:
                #print("win %d"%player)
                on_win(p[player-1],m)
            if print_err:
                print(error_msg)
                print_err = False
            print("%s's turn:" % p[player])
            try:
                x = input_n()
            except ValueError as e:
                print_err = True
                error_msg = "Invalid input, try again"
                continue
            print(x)
            if x == "u":
                try:#undo
                    last= moves.pop()
                    redo_list.append(last)
                    m = undo(m,last)
                    n-=1
                    player=(n)%2
       
                except IndexError as e:
                    pass
                print(redo_list)
            elif x == 'r':
                try:
                    last=redo_list.pop()
                    moves.append(last)
                    m = drop(m,last,player+1)
                    n-=1
                    player=(n)%2
       
                except IndexError as e:
                    pass
            elif x == 's':
                print('swap')
            elif x == 'c':
                print('clear')
                # undo all moves
                for i in range(len(moves)):
                    last= moves.pop()
                    redo_list.append(last)
                    m = undo(m,last)
                    n-=1
                    player=(n)%2
            elif x == 'q':
                print('Game has been put away.')
                return
            else:
                print(x)
                try:
                    m = drop(m,x,player+1)
                except ValueError as e:
                    print_err = True
                    error_msg = "Invalid move, try again"
                    continue
                moves.append(x)
                redo_list=[]
                n += 1
                player=(n)%2
              
            print(moves)
            if win(m) > 0:
                on_win(p[player-1],m)
     
            #if x:
            #    break
              
    except KeyboardInterrupt as e:
        print("\nMom put away the game.")
        return

if __name__ == '__main__':
    main()
