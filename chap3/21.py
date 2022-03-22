#21. カテゴリ名を含む行を抽出
"""
記事中でカテゴリ名を宣言している行を抽出せよ．
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
    if d[0]["title"] == "イギリス":
    #if d[0]["title"]=="エジプト":      #エジプトに変えても同じようにできるはず
        england_txt=d[0]["text"]
        #print(england_txt)
l=england_txt.split("\n")

print("Category lines are these")
print("-----------------------------")
for line in l:
    #print(line)
    #カテゴリ名を宣言する部分は"[[Category:"で始まる
    if re.match(r"\[\[Category:",line):
        print(line)
print("-----------------------------")

