#37. 「猫」と共起頻度の高い上位10語
"""
「猫」とよく共起する（共起頻度が高い）10語と
その出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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

#共起単語を設定
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
    #print(sentlen)
    for word in sent:
        #単語として、共起単語があればflagをon
        if word.surface==coreword:
            flag=True
    #共起単語があるので
    if flag:
        #共起単語を含む文中の形態素全てを見る
        for word in sent:
            #単語ならば
            if word.pos!="記号":
                #原型をとり
                w=word.base
                #共起語自身でないことを確認する
                if w!=coreword:
                    l.append(w)

#上位10単語
c=Counter(l).most_common()[:10]

print("Most 10 frequent Co-occurrence words with {0} are listed below".format(coreword))
for i,(w,num) in enumerate(c):
    print("{0}: word:{1} count:{2}".format(ordinal(i+1),w,num))

words=[]
cnts=[]
for i,(w,num) in enumerate(c):
    words.append(w)
    cnts.append(num)

fig = plt.figure()
ax = fig.add_subplot(111)
titleword="Top 10 words frequently co-occur with "+coreword
ax.set_title(titleword, fontsize = 16)
plt.xlabel('name',fontsize=18)
plt.ylabel('counts',fontsize=18)


plt.bar(words,cnts)
plt.show()