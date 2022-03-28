#qpy:qpyapp
# switch sides
# undo redo
# unwin rewin


print("hello")

def print_m1(m):
    for i in range(6):
        print(m[i])
        
def print_m(m):
    print(" 0 1 2 3 4 5 6")
    for i in range(6):
        print("|",end='')
        for j in range(7):
            if m[i][j] == 0:
                print(' |',end='')
            else:            
                print('%d|'%m[i][j],end='')
        print('')

def drop(m,n,p):
    for i in range(6):
        j = 5-i
        if m[j][n] == 0:
            m[j][n] = p
            return m
    raise ValueError
     
def input_n():
    x = None
    while x not in [0,1,2,3,4,5,6]:
        try:
            x = input()
           
            if x in ["u","r","s"]:
                print("urs")
                return x
            x = int(x)   
        except ValueError as e:
            x = None
    return x

def on_win(n,m):
    print("%s wins!"%n)
    print_m(m)
    x=input()
    
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
                    print("win %d"%player)
                    on_win(p[player],m)
                    return w, player
    return 0, None
                    
                
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

for i in range(3):
    moves=[]
    redo_list=[]
    p = [" "," "]
    p[0] = "Carmen"
    p[1] = "Nick"
    m = m_init()
    player=0
    last=7
    n=0
    while n < (7*6):
        print(player)
        print_m(m)
        print("%s:" % p[player])
        x = input_n()
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
        else:
            try:
                print(x)
                m = drop(m,x,player+1)
                moves.append(x)
                redo_list=[]
                n += 1
                player=(n)%2
            except ValueError as e:
                pass
          
        print(moves)
        x,pp = win(m)
        if x:
            break
          
        
