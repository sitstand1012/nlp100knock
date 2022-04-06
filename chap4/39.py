#39. Zipfの法則
"""
単語の出現頻度順位を横軸，
その出現頻度を縦軸として，両対数グラフをプロットせよ．
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
rank=[]

for i,(w,num) in enumerate(c):
    rank.append(i+1)
    cnts.append(num)
length=len(set(cnts))
fig = plt.figure()

ax = fig.add_subplot(111)
ax.set_title("Show Zipf's low", fontsize = 16)
plt.xlabel('rank',fontsize=18)
plt.ylabel('counts',fontsize=18)
ax.set_yscale('log')  # y軸をlogスケールで描く
ax.set_xscale('log')  # x軸をlogスケールで描く

plt.plot(rank,cnts)
plt.show()