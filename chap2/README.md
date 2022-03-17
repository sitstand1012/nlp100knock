# nlp100本ノック chap2
環境変数として次のものを利用しています

- `NLP100KNOCK_CHAP2_DIR`…`popular-names.txt`を保存し、13.以降に出る`col1.txt`,`col2.txt`を保存しているディレクトリ

## 変数の設定方法
0. (設定も何もしてない人向け)ホームディレクトリに.(shellname)rcを用意する(bashなら.bashrc,zshなら.zshrc)
`touch ~/.(shellname)rc`(bashなら`touch ~/.bashrc`)でいけるはず
1. `echo export NLP100KNOCK_CHAP2_DIR=/PATH/TO/dir_for_variable >> ~/.(shellname)rc`で書き込めます。
2. `source ~/.(shellname)rc`で設定を適用します。