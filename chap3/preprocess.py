"""
Wikipedia記事のJSONファイルをダウンロードします
"""

import urllib.request
import os
import gzip
import shutil

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

