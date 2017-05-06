######################
#import sys

#read = (line.rstrip() for line in sys.stdin)


######################3
import re
import sys

# for line in sys.stdin:
#     tst = line.rstrip()

# print(line)


tst=['I need to undersstand the human mind human human', 'humanity humahuman n human']
#st = "acc, aac, abc, azc"
#pat = r"a.c"
#print(tst)
#fst = re.sub(pat,"aEc", st)
#print(fst)
pattern = r"human"
fst=[]
for word in tst:
    #print(word)
    #dupl = re.findall(pattern, word)
    fst.append(re.sub(pattern, "computer", word, 1))
for el in fst:
    print(el)
    #if dupl:
    #   print(word)
    #\bprint(dupl)
   # dupl1 = re.findall(pattern1, word)
   # print(dupl1)
#    print(len(dupl))
    #if len(dupl) >= 2:
     #   print(word)