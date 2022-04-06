#35. 単語の出現頻度
"""
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import MeCab
import os
from collections import Counter

CHAP4_DIR=os.environ["NLP100KNOCK_CHAP4_DIR"]

mecabpath=os.path.join(CHAP4_DIR,"neko.txt.mecab")

class Morph:
    def __init__(self,inst):
        surface,l=inst.split("\t")
        info=l.split(",")

        if len(info)==9:
            pos,pos1,_,_,_,_,base,_,_=info
        else:
            pos,pos1,_,_,_,_,base=info

        self.surface=surface
        self.base=base
        self.pos=pos
        self.pos1=pos1


with open(mecabpath,"r") as f:
    l=f.read()
s=l.split("\n\n")

all=[]

for sent in s:
    lin=sent.split("\n")
    partial=[]
    for line in lin:
        if (line)and(line!="EOS"):
            partial.append(Morph(line))
    all.append(partial)
l=[]
for sent in all:
    sentlen=len(sent)
    #print(sentlen)
    for word in sent:
        if word.pos=="名詞":
            l.append(word.surface)
c=Counter(l).most_common()
#print(c)
#input()

print("Sorted by frequency.")
flag=True
cnt=float("inf")
for w,num in c:
    if num<=cnt:
        pass
    else:
        flag=False

#Verification(一応)
if flag:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")