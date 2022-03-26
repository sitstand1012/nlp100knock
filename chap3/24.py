#24. ファイル参照の抽出
"""
記事から参照されているメディアファイルをすべて抜き出せ．
"""

import os
import json
import re

CHAP3_DIR=os.environ["NLP100KNOCK_CHAP3_DIR"]

target_file = os.path.join(CHAP3_DIR,"jawiki-country.json")

decoder=json.JSONDecoder()
res=[]
with open(target_file, 'r') as f:
    line = f.readline()
    while line:
        res.append(decoder.raw_decode(line))
        line = f.readline()

england_txt=""
for i,d in enumerate(res):
    if d[0]["title"]=="イギリス":
    #if d[0]["title"]=="エジプト":      #エジプトに変えても同じようにできるはず
        england_txt=d[0]["text"]
        #print(england_txt)
l=england_txt.split("\n")

print("Media files are these")
print("-----------------------------")
for line in l:
    #メディアファイルは全て"[[ファイル:"か[[File:で始まる…はず
    jafilematch=list(re.finditer(r"\[\[ファイル:.*?\]\]",line))
    enfilematch=list(re.finditer(r"\[\[File:.*?\]\]",line))
    if (jafilematch)or(enfilematch):
        #print(jafilematch,enfilematch)
        #表記形式をみると、行を"|"で仕切ったときの先頭に名前が含まれる
        #先頭から"[[ファイル:"と"]]"を除去すればいいはず
        for iter in jafilematch:
            begin,end=iter.span()
            s=line[begin:end]
            l=s.split("|")
            print(l[0].replace("[[ファイル:","").replace("]]",""))
        for iter in enfilematch:
            begin,end=iter.span()
            s=line[begin:end]
            l=s.split("|")
            print(l[0].replace("[[File:","").replace("]]",""))
print("-----------------------------")

