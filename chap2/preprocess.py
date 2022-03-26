"""
popular-names.txtは，アメリカで生まれた赤ちゃんの
「名前」「性別」「人数」「年」をタブ区切り形式で格納したファイルである．

これをダウンロードします。
"""

import os
import urllib.request

#タスクファイルのurl
url="https://nlp100.github.io/data/popular-names.txt"

#popular-names.txtをダウンロードするpathを指定します
CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

#実際にダウンロード
urllib.request.urlretrieve(url, txtpath)