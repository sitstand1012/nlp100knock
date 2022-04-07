#36. 頻度上位10語
"""
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

import MeCab
import os
from collections import Counter
import matplotlib.pyplot as plt

CHAP4_DIR=os.environ["NLP100KNOCK_CHAP4_DIR"]

mecabpath=os.path.join(CHAP4_DIR,"neko.txt.mecab")

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
        if word.pos!="記号":
            l.append(word.surface)
c=Counter(l).most_common()[:10]

print("Most frequent 10 words are listed below")
for i,(w,num) in enumerate(c):
    print("{0}: word:{1} count:{2}".format(ordinal(i+1),w,num))

words=[]
cnts=[]
for i,(w,num) in enumerate(c):
    words.append(w)
    cnts.append(num)

#matplotlibマスターに、俺はなる！
fig = plt.figure()
ax = fig.add_subplot(111)
titleword="Top 10 words frequently occur with"
ax.set_title(titleword, fontsize = 16)
plt.xlabel('name',fontsize=18)
plt.ylabel('counts',fontsize=18)

plt.bar(words,cnts)
plt.show()