"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
その結果をneko.txt.mecabというファイルに保存せよ．このファイルを用いて，
以下の問に対応するプログラムを実装せよ．

"""

import MeCab
import os
import urllib.request

url="https://nlp100.github.io/data/neko.txt"

#事前設定したpathを呼び出し
CHAP4_DIR=os.environ["NLP100KNOCK_CHAP4_DIR"]

#テキストのpath
txtpath=os.path.join(CHAP4_DIR,"neko.txt")

#.mecabファイルのpath
mecabpath=os.path.join(CHAP4_DIR,"neko.txt.mecab")

#とりまurlからデータダウンロード
urllib.request.urlretrieve(url, txtpath)

#パーザ準備
wakati = MeCab.Tagger()

with open(txtpath,"r") as f:
    l=f.readlines()

parsed=[]

for line in l:
    #１行ずつパージリザルトを格納
    result=wakati.parse(line)
    parsed.append(result)

#"\n\n"で区切ることで、確実に区切れるようになっているはず。
with open(mecabpath,"w") as f:
    f.write("\n\n".join(parsed))


"""
with open(mecabpath,"r") as f:
    l=f.read()
s=l.split("\n\n")

for sent in s:
    lin=sent.split("\n")
    for line in lin:
        print(line)
    input()
"""