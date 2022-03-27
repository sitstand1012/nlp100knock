#30. 形態素解析結果の読み込み
"""
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）
をキーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab
import os
from random import *

CHAP4_DIR=os.environ["NLP100KNOCK_CHAP4_DIR"]

mecabpath=os.path.join(CHAP4_DIR,"neko.txt.mecab")
seed(0)

class Morph:
    def __init__(self,inst):
        #[UNK]でないとき
        #表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音

        #[UNK]のとき
        #表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形
        #(読みや発音が不明になるため省かれるらしい。はぁ)

        surface,l=inst.split("\t")
        info=l.split(",")
        #[UNK]でないなら、このかたち。
        if len(info)==9:
            pos,pos1,_,_,_,_,base,_,_=info
        #[UNK]のときは、このかたち。
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

#一文ごとに考える
for sent in s:
    lin=sent.split("\n")
    partial=[]
    #一単語ごとに考える
    for line in lin:
        if (line)and(line!="EOS"):
            partial.append(Morph(line))
    all.append(partial)

cnt=0
sentlength=len(s)
maxdisp=min(7,sentlength//2)

#ランダムに何個か形態素解析結果を表示させる
print("display morphological analysis result randomly")
print("-----------------------------")
while cnt<maxdisp:
    sentid=randrange(sentlength)
    if not(all[sentid]):continue
    wordlength=len(all[sentid])
    wordid=randrange(wordlength)
    inst=all[sentid][wordid]
    print("case{0:2d} | surface:{1} \t base:{2} \t pos:{3} \t pos1:{4}"
          .format(cnt+1,inst.surface,inst.base,inst.pos,inst.pos1))
    cnt+=1

