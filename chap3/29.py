#29. 国旗画像のURLを取得する
"""
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

import urllib.request
import requests
import os
import gzip
import shutil
import json
import re

from PIL import Image
import io
from urllib.request import urlopen
import matplotlib.pyplot as plt

CHAP3_DIR=os.environ["NLP100KNOCK_CHAP3_DIR"]

target_file = os.path.join(CHAP3_DIR,"jawiki-country.json")

ImageFile.LOAD_TRUNCATED_IMAGES = True

decoder=json.JSONDecoder()
res=[]


def weak_emphas_remove(s):
    ns=re.sub(r"\'\'","",s)
    return ns

def emphas_remove(s):
    ns=re.sub(r"\'\'\'","",s)
    return ns

def strong_emphas_remove(s):
    ns=re.sub(r"\'\'\'\'\'","",s)
    return ns

def internal_link_remove(s):
    iter_begin=list(re.finditer(r"\[\[",s))
    iter_end=list(re.finditer(r"\]\]",s))
    bra_begin =list(re.finditer(r"\{\{",s))

    place_bra=[""]*len(s)
    place_internal=[""]*len(s)

    for i in range(len(bra_begin)):
        begin,end=bra_begin[i].span()
        for j in range(begin,end):
            place_bra[j]="1"

    for i in range(len(iter_begin)):
        begin,end=iter_begin[i].span()
        for j in range(begin,end):
            place_internal[j]="1"

    if (iter_begin)and(iter_end):
        nsl=[]
        end=0
        l=[]

        for i in range(len(iter_begin)):
            begin,_=iter_begin[i].span()

            nsl.append(s[end:begin])

            _,end = iter_end[i].span()

            ext=s[begin:end]
            #print(ext)
            if (re.match(r"\[\[ファイル",ext))or(re.match(r"\[\[File",ext)):
                nsl.append(ext)
                continue
            ind=0
            for i,c in enumerate(ext):
                if (c=="|"):
                    for j in range(i,-1,-1):
                        if (place_internal[begin+j]):
                            l.append(ext[ind:i])
                            ind=i+1
                            break
                        elif (place_bra[begin+j]):
                            break
            l.append(ext[ind:i+1])

            for i in range(len(l)):
                l[i]=l[i].replace("[[","").replace("]]","")
            #print("l",l)
            nsl.append(l[-1])
        nsl.append(s[end:])
        #print("nsl",nsl)
        ns="".join(nsl)
        return ns
    else:
        return s

#メディアファイル除去関数
def file_remove(s):
    jafilematch=list(re.finditer(r"\[\[ファイル:.*?\]\]",s))
    enfilematch=list(re.finditer(r"\[\[File:.*?\]\]",s))
    range_list=[]
    for iter in jafilematch:
        range_list.append(iter.span())
    for iter in enfilematch:
        range_list.append(iter.span())
    range_list.sort()
    if (range_list):
        end=0
        nsl=[]
        for i in range(len(range_list)):
            begin,_=range_list[i]
            nsl.append(s[end:begin])
            _,end=range_list[i]

            ext=s[begin:end]
            #print(ext)
            l=ext.split("|")
            if len(l)==1:
                nsl.append("")
            else:
                nsl.append(l[-1].replace("]]",""))
        nsl.append(s[end:])
        ns="".join(nsl)
        #print(s)
        #print(ns)
        return ns
    else:
        return s

#{{}}をカットする関数(しかし、良い関数が見つからなかったので、使用見送り。)
def bra_cut(s):
    bramatch = list(re.finditer(r"\{\{.*?\}\}", s))
    range_list=[]
    for iter in bramatch:
        range_list.append(iter.span())
    range_list.sort()
    if (range_list):
        end=0
        nsl=[]
        for i in range(len(range_list)):
            begin,_=range_list[i]
            nsl.append(s[end:begin])
            _,end=range_list[i]

            ext=s[begin:end]
            #print(ext)
            l=ext.split("|")
            if (len(l)==3)or(len(l)==4):
                nsl.append(l[-1].replace("}}",""))
            else:
                nsl.append("")
        nsl.append(s[end:])
        ns="".join(nsl)
        #print(s)
        #print(ns)
        return ns
    else:
        return s

#結局つかってない
def markup_remove(s):
    ns=bra_cut(s)
    #n2s=ref_cut(s)
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
            true_line=internal_link_remove(new_line)
            final_line=file_remove(true_line)


            dict[lastkey]="".join([dict[lastkey],final_line])
        else:
            for i,c in enumerate(line):
                if (c=="=")and(splitflag):
                    elem1=line[1:i].strip()
                    elem2=line[i+1:].strip()
                    splitflag=False

            new_elem1=weak_emphas_remove(emphas_remove(strong_emphas_remove(elem1)))
            new_elem2=weak_emphas_remove(emphas_remove(strong_emphas_remove(elem2)))

            true_elem1=internal_link_remove(new_elem1)
            true_elem2=internal_link_remove(new_elem2)

            final_elem1=file_remove(true_elem1)
            final_elem2=file_remove(true_elem2)

            lastkey = final_elem1
            dict[final_elem1]=final_elem2

    if re.match(r"\{\{基礎情報",line):
        seeflag=True

"""
print(dict)
for k,v in dict.items():
    print(k,v)
    newv=markup_remove(v)
    dict[k]=newv
    #input()
"""
link=dict["国旗画像"]
countryname=dict["略名"]

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop" : "url",
    "titles": "File:{0}".format(link),
    "iwurl":"True"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
url = DATA["query"]["pages"]['23473560']["imageinfo"][0]["url"]
#print(url)
print("the wikipedia link of {0}\'s country flag is \"{1}\"".format(countryname,url))

#urlの画像を表示しようと思ったけどできなかった
#問題には入ってないので今後の課題ということで
"""
a_img = Image.open(io.BytesIO(requests.get(url).content))
plt.figure(figsize=(20,20))
plt.imshow(a_img)
"""