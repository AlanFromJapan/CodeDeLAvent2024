import io
import sys
import re

REX= re.compile(r"mul\((\d+),(\d+)\)")
DONT= r"don't\(\).*do\(\)"

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

total=0
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
        ldo = re.sub(DONT, "", l)
        print(f"l: {l} -> ldo: {ldo}")

        matches = REX.finditer(ldo)
        for m in matches:
            a = int(m.group(1))
            b = int(m.group(2))
            print(f"mul({a},{b}) = {a*b}")
            total = total + a*b

print(f"Total: {total}")
