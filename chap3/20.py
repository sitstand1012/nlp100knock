#20. JSONデータの読み込み
"""
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import urllib.request
import os
import gzip
import shutil
import json

#タスクファイルのurl
url="https://nlp100.github.io/data/jawiki-country.json.gz"

#jawiki-country.json.gzをダウンロードする場所を指定
CHAP3_DIR=os.environ["NLP100KNOCK_CHAP3_DIR"]
gzpath=os.path.join(CHAP3_DIR,"jawiki-country.json.gz")

#実際にダウンロード
urllib.request.urlretrieve(url, gzpath)

source_file = gzpath

#解凍先
target_file = os.path.join(CHAP3_DIR,"jawiki-country.json")

#gzファイルを解凍
with gzip.open(source_file, mode="rb") as gzip_file:
    with open(target_file, mode="wb") as decompressed_file:
        shutil.copyfileobj(gzip_file, decompressed_file)

#100本knockのjsonは不完全なjsonファイルらしく、raw_decodeが必要らしい
#see:https://www.nooozui.com/entry/20200110/1578612600
decoder=json.JSONDecoder()
res=[]
with open(target_file, 'r') as f:
    line = f.readline()
    while line:
        res.append(decoder.raw_decode(line))
        line = f.readline()

england_txt=""
#「イギリス」が出たら本文表示しようね
for i,d in enumerate(res):
    if d[0]["title"]=="イギリス":
        england_txt=d[0]["text"]
        print(england_txt)
