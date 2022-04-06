#38. ヒストグラム
"""
単語の出現頻度のヒストグラムを描け．
ただし，横軸は出現頻度を表し，1から単語の出現頻度の最大値までの線形目盛とする．
縦軸はx軸で示される出現頻度となった単語の異なり数（種類数）である．
"""

import MeCab
import os
from collections import Counter
import matplotlib.pyplot as plt

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

coreword="猫"

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
    flag=False
    for word in sent:
        l.append(word.surface)
c=Counter(l).most_common()
cnts=[]

for i,(w,num) in enumerate(c):
    cnts.append(num)
length=len(set(cnts))
mi=min(cnts)
ma=max(cnts)

fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_title("Histgram of words frequency", fontsize = 16)
plt.xlabel('counts',fontsize=18)
plt.ylabel('uniqs',fontsize=18)
plt.hist(cnts,bins=length)
plt.show()