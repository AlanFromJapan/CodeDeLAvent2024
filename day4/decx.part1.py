import io
import sys

filename = "input.txt"
llimit = -1
if len(sys.argv) < 2:
    print("INFO: no filename passed as param, defaulting to 'input.txt'")
else:
    print(f"INFO: 1st param is filename, will process '{sys.argv[1]}'")
    filename = str(sys.argv[1])

if len(sys.argv) >= 3:
    print(f"INFO: 2nd param is limit of lines to process, will process only the first {sys.argv[2]} lines")
    llimit = int(sys.argv[2])


debug = False
def dbg(s):    
    if debug:
        print(s, end="")

def tryCell(MX, x, y, word, direction):
    global MOUT
    if word == "":
        return True

    if x < 0 or y < 0:
        return False
    if y >= len(MX):
        return False
    if x >= len(MX[y]):
        return False



    if MX[y][x] != word[0]:
        return False
    else:
        r=False
        if direction == "right":
            r= tryCell(MX, x+1, y, word[1:], direction)
        if direction == "down":
            r= tryCell(MX, x, y+1, word[1:], direction)
        if direction == "diag":
            r= tryCell(MX, x+1, y+1, word[1:], direction)
        if direction == "diag2":
            r= tryCell(MX, x-1, y+1, word[1:], direction)
        if direction == "diag3":
            r= tryCell(MX, x+1, y-1, word[1:], direction)
        if direction == "diag4":
            r= tryCell(MX, x-1, y-1, word[1:], direction)    
        if direction == "left":
            r= tryCell(MX, x-1, y, word[1:], direction)
        if direction == "up":
            r= tryCell(MX, x, y-1, word[1:], direction)
        
        #mark
        if r:
            MOUT[y] = MOUT[y][:x] + word[0] + MOUT[y][x+1:]
        
        return r

def mxPrint(mx):
    if debug:
        for y in range(len(mx)):
            print(mx[y])

     

MX = []
MOUT=[]
lcount = 0
with io.open(filename, "r") as f:
    while True:
        l = f.readline()
        lcount = lcount +1

        if not l:
            #finished!
            break

        if llimit > 0 and lcount > llimit:
            break

        #process!
        l = l.strip()

        #edit me v v v v v  
        MX.append(l)

mxPrint(MX)
total = 0
for y in range(len(MX)):
    MOUT.append('.' * len(MX[y]))

for y in range(len(MX)):
    for x in range(len(MX[y])):
        if MX[y][x] != "X":
            continue
        for direction in ["right", "down", "diag", "diag2", "diag3", "diag4", "left", "up"]:
            if tryCell(MX, x, y, "XMAS", direction):
                dbg(f"FOUND XMAS at {x},{y} going {direction}")
                total = total + 1


mxPrint(MOUT)
print(f"Total: {total}")
