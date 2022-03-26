# nlp100本ノック chap3
環境変数として次のものを利用しています

- `NLP100KNOCK_CHAP3_DIR`…`jawiki-country.json.gz`、`jawiki-country.json`を保存するフォルダ

## 環境変数の設定方法
[chap2](https://github.com/sitstand1012/nlp100knock/blob/main/chap2/README.md)と同じようにやれば良い。

## データ保存方法の検討
- `preprocess.py`を利用すると良い？
- ~~[chap2](https://github.com/sitstand1012/nlp100knock/blob/main/chap2/README.md)と同様~~
  - `wget -P $NLP100KNOCK_CHAP3_DIR https://nlp100.github.io/data/jawiki-country.json.gz && gzip -d $NLP100KNOCK_CHAP3_DIR/jawiki-country.json.gz`でした。(gzipの解凍操作が必要です)

~~最後の方はやっつけになってるけど許して~~