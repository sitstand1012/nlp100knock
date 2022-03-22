#25. テンプレートの抽出
"""
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．
"""

import urllib.request
import os
import gzip
import shutil
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
        #print(d[0])
        england_txt=d[0]["text"]
        #print(england_txt)
l=england_txt.split("\n")
seeflag=False
dict={}
lastkey=""
for line in l:
    #データがクソなので、"}}"が来たら終わりということを教えないといけない
    if line=="}}":
        seeflag=False

    #seeflag=Trueのとき、基礎情報のデータを見ているはず
    if seeflag:
        #print(line)
        elem1=""
        elem2=""
        splitflag=True

        #先頭が*で始まる時は、前のkeyにくっつける形で、整形。
        if line[0]=="*":
            dict[lastkey]="".join([dict[lastkey],line])
        else:
            for i,c in enumerate(line):
                #最初の"="でsplitをする
                if (c=="=")and(splitflag):
                    elem1=line[1:i].strip()
                    elem2=line[i+1:].strip()
                    splitflag=False
            lastkey=elem1
            dict[elem1]=elem2

    #基礎情報の項目は"{{基礎情報"で始まる
    if re.match(r"\{\{基礎情報",line):
        seeflag=True
print("Basic information template dict is below")
print("-----------------------------")
print(dict)
print("-----------------------------")

