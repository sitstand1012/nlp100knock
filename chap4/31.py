#31. 動詞
"""
動詞の表層形をすべて抽出せよ．
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

#surfaceを保存する。setにすると重複を消せるので便利。
surfaceset=set()

#一文ごとに考える
for sent in all:
    #一単語ごとに考える
    for word in sent:
        #動詞なら
        if word.pos=="動詞":
            #setにadd
            surfaceset.add(word.surface)

surfacesetlen=len(surfaceset)

maxdisp=min(7,surfacesetlen)

#順不同にいくつか表示
print("There are {0} type of verb surfaces are in this sentence.".format(surfacesetlen))
print()
print("We now show only {0} surfaces.".format(maxdisp))
print("-----------------------------")
for i,v in enumerate(surfaceset):
    if i<maxdisp:
        print(v)
print("-----------------------------")