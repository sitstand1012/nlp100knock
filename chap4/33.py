#33. 「AのB」
"""
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

import MeCab
import os

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

#「の」で連結するnoun phraseを保存する。setに(ry
nounphraseset=set()

for sent in all:
    #3つの形態素を跨って見る必要があるため、inは使いづらいので、長さを測って愚直に見る
    sentlen = len(sent)
    for i in range(sentlen-2):
        #2つの名詞が「の」で連結されているなら
        if (sent[i].pos=="名詞")and(sent[i+1].surface=="の")and(sent[i+2].pos=="名詞"):
            #setにadd
            nounphraseset.add("".join([sent[i].surface,sent[i+1].surface,sent[i+2].surface]))

nounphrasesetlen=len(nounphraseset)
maxdisp=min(7,nounphrasesetlen)


#いくつか表示
print("There are {0} type of noun phrase sets are in this sentence.".format(nounphrasesetlen))
print()
print("We now show only {0} surfaces.".format(maxdisp))
print("-----------------------------")
for i,v in enumerate(nounphraseset):
    if i<maxdisp:
        print(v)
print("-----------------------------")