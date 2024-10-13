import os,random

def draw_graph(data):
    m = max(data)
    sp = 0
    for y in range(m+1,-1,-1):
        if y < 10: sp = 1
        print(" "*sp + str(y),end="")
        for x in range(len(data)):
            if data[x] == y:
                print("*",end="")
            else:
                print(" ",end="")
            
        print("")
        

os.system('cls' if os.name == 'nt' else 'clear')


draw_graph([1,3,9,8,7])