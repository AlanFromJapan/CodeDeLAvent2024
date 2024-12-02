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


lr =[]
ll = []
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
        ll.append(int(l.split("   ")[0]))  #split by space
        lr.append(int(l.split("   ")[1]))

lr.sort()
ll.sort()

lrcount= {}
for i in lr:
    if i in lrcount:
        lrcount[i] = lrcount[i] + i
    else:
        lrcount[i] = i


total = 0
for i in ll:
    if i in lrcount:
        total = total + lrcount[i]

print(f"Total: {total}")