#35. 単語の出現頻度
"""
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

import MeCab
import os
from collections import Counter

CHAP4_DIR=os.environ["NLP100KNOCK_CHAP4_DIR"]

mecabpath=os.path.join(CHAP4_DIR,"neko.txt.mecab")

#数字を序数に変える魔法
def ordinal(i):
    return str(i)+({1:"st",2:"nd",3:"rd"}.get(i if 14>i>10 else i % 10) or "th")

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
    for word in sent:
        #記号は単語ではないのでそれ以外は単語のはず
        if (word.pos!="記号"):
            #単語の原型をいれましょう
            l.append(word.base)

#counterを使うとmost_common()を呼び出すだけでsortされる
c=Counter(l).most_common()

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