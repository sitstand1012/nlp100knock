#23. セクション構造
"""
記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ．
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
        england_txt=d[0]["text"]
        #print(england_txt)
l=england_txt.split("\n")

for line in l:
    #print(line)
    #sectionは必ず"=="で始まるはず
    if re.match(r"==",line):
        #level計算はこれでいいはず
        level=(line.count("="))//2-1

        #section名は行から"="を除去すれば良い(ついでに" "(whitespace)も除く)
        sectionname=re.sub(r'=+',"",line).strip()
        print("section {0} is in level {1}".format(sectionname,level))

