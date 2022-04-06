#34. 名詞の連接
"""
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
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

nounconjunctionset=set()
for sent in all:
    sentlen=len(sent)
    #print(sentlen)
    l=[]
    for word in sent:
        if word.pos=="名詞":
            l.append(word.surface)
        else:
            if len(l)>0:
                w="".join(l)
                nounconjunctionset.add(w)
                l=[]

nounconjunctionsetlen=len(nounconjunctionset)
maxdisp=min(7,nounconjunctionsetlen)
print("There are {0} type of noun conjunction sets are in this sentence.".format(nounconjunctionsetlen))
print()
print("We now show only {0} surfaces.".format(maxdisp))
print("-----------------------------")
for i,v in enumerate(nounconjunctionset):
    if i<maxdisp:
        print(v)
print("-----------------------------")