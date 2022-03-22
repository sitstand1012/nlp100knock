#27. 内部リンクの除去
"""
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ（参考: マークアップ早見表）．
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


def weak_emphas_remove(s):
    ns=re.sub(r"\'\'","",s)
    return ns

def emphas_remove(s):
    ns=re.sub(r"\'\'\'","",s)
    return ns

def strong_emphas_remove(s):
    ns=re.sub(r"\'\'\'\'\'","",s)
    return ns

#内部リンク除去関数
def internal_link_remove(s):
    iter_begin=list(re.finditer(r"\[\[",s))
    iter_end=list(re.finditer(r"\]\]",s))
    bra_begin =list(re.finditer(r"\{\{",s))

    place_bra=[""]*len(s)
    place_internal=[""]*len(s)


    #{{(ブラ)の先頭を記録
    for i in range(len(bra_begin)):
        begin,end=bra_begin[i].span()
        for j in range(begin,end):
            place_bra[j]="1"

    # [[(内部リンク)の先頭を記録
    for i in range(len(iter_begin)):
        begin,end=iter_begin[i].span()
        for j in range(begin,end):
            place_internal[j]="1"

    #[[~~]]のペアがある時
    if (iter_begin)and(iter_end):
        nsl=[]
        end=0
        l=[]
        #[[~~]]のペアを順に見る
        for i in range(len(iter_begin)):
            begin,_=iter_begin[i].span()

            #まずは[[~~]]より前(外)にある部分を挿入
            nsl.append(s[end:begin])

            _,end = iter_end[i].span()

            #[[~~]]の列を単純に抽出
            ext=s[begin:end]
            print(ext)

            #"[[ファイル"で始まるメディアファイルは無視
            if (re.match(r"\[\[ファイル",ext))or(re.match(r"\[\[File",ext)):
                nsl.append(ext)
                continue

            ind=0
            #ext内を順に走査
            for i,c in enumerate(ext):
                #"|"があるとき
                if (c=="|"):
                    for j in range(i,-1,-1):
                        #前に遡って[[が先に来るならsplit
                        if (place_internal[begin+j]):
                            l.append(ext[ind:i])
                            ind=i+1
                            break
                        #そうでないならsplitしない
                        elif (place_bra[begin+j]):
                            break
            l.append(ext[ind:i+1])

            #split終了後"[["と"]]"を除去
            for i in range(len(l)):
                l[i]=l[i].replace("[[","").replace("]]","")

            #print("l",l)
            #規則より最終要素のみが表層テキストとして残るはず
            nsl.append(l[-1])
        #最後の[[~~]]よりあとの部分を挿入
        nsl.append(s[end:])

        #print("nsl",nsl)
        ns="".join(nsl)
        return ns
    else:
        return s



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
            if true_line != new_line:
                print("\"{0}\" \n is substituted into \n\"{1}\"".format(new_line,true_line))
                print()
            dict[lastkey]="".join([dict[lastkey],true_line])
        else:
            for i,c in enumerate(line):
                if (c=="=")and(splitflag):
                    elem1=line[1:i].strip()
                    elem2=line[i+1:].strip()
                    splitflag=False

            new_elem1=weak_emphas_remove(emphas_remove(strong_emphas_remove(elem1)))
            new_elem2=weak_emphas_remove(emphas_remove(strong_emphas_remove(elem2)))

            #内部リンク除去
            true_elem1=internal_link_remove(new_elem1)
            true_elem2=internal_link_remove(new_elem2)

            #変更部分を表示
            if true_elem1!=new_elem1:
                print("\"{0}\" \n is substituted into \n\"{1}\"".format(new_elem1,true_elem1))
                print()
            if true_elem2!=new_elem2:
                print("\"{0}\" \nis substituted into \n\"{1}\"".format(new_elem2,true_elem2))
                print()


            lastkey = true_elem1
            dict[true_elem1]=true_elem2

    if re.match(r"\{\{基礎情報",line):
        seeflag=True

print("Basic information template dict (removed emphasis and internal link) is below")
print("-----------------------------")
print(dict)
print("-----------------------------")

