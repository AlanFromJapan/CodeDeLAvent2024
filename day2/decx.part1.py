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

def isSafe(l= []):
    direction = "?"
    for i in range(len(l) -1):
        #min 1 max 3 diff
        if l[i] == l[i+1] or abs(l[i] - l[i+1]) > 3:
            return False
        
        if i == 0:
            direction = "up" if l[i] < l[i+1] else "down"
        else:
            if direction == "up" and l[i] > l[i+1]:
                return False
            elif direction == "down" and l[i] < l[i+1]:
                return False

    return True


total = 0
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

        #parse
        parts = l.split(" ")
        parts = [int(x) for x in parts]

        dbg(f"Processing: {parts}")

        if isSafe(parts):
            total = total + 1
            dbg("SAFE\n")
        else:
            dbg("UNSAFE\n")

print(f"Total safe reports: {total}")