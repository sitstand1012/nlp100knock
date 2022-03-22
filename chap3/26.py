#26. 強調マークアップの除去
"""
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ（参考: マークアップ早見表）．
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

#弱い強調除去
def weak_emphas_remove(s):
    ns=re.sub(r"\'\'","",s)
    return ns

#強調除去
def emphas_remove(s):
    ns=re.sub(r"\'\'\'","",s)
    return ns

#強い強調除去
def strong_emphas_remove(s):
    ns=re.sub(r"\'\'\'\'\'","",s)
    return ns

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
for line in l:
    if line=="}}":
        seeflag=False

    if seeflag:
        elem1=""
        elem2=""
        splitflag=True

        if line[0]=="*":
            new_line=weak_emphas_remove(emphas_remove(strong_emphas_remove(line)))
            if line != new_line:
                print("\"{0}\" \n is substituted into \n\"{1}\"".format(line, new_line))
                print()
            dict[lastkey]="".join([dict[lastkey],new_line])
        else:
            for i,c in enumerate(line):
                if (c=="=")and(splitflag):
                    elem1=line[1:i].strip()
                    elem2=line[i+1:].strip()
                    splitflag=False

            #強調除去
            new_elem1=weak_emphas_remove(emphas_remove(strong_emphas_remove(elem1)))
            new_elem2=weak_emphas_remove(emphas_remove(strong_emphas_remove(elem2)))

            #変更部分を表示
            if elem1!=new_elem1:
                print("\"{0}\" \n is substituted into \n\"{1}\"".format(elem1,new_elem1))
                print()
            if elem2!=new_elem2:
                print("\"{0}\" \nis substituted into \n\"{1}\"".format(elem2,new_elem2))
                print()
            lastkey = new_elem1
            dict[new_elem1]=new_elem2

    if re.match(r"\{\{基礎情報",line):
        seeflag=True

print("Basic information template dict (removed emphasis) is below")
print("-----------------------------")
print(dict)
print("-----------------------------")

