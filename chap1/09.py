#09. Typoglycemia
"""
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば
”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”
）を与え，その実行結果を確認せよ．
"""
from random import *

#seed固定
seed(0)

s="I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

#typoglycemia処理をする関数
def typogly(word):
    #4文字以下ならそのまま出力
    if len(word)<=4:
        return word

    #単語の最初の文字
    b=word[0]

    #単語の内部
    i=word[1:-1]
    #list化してからshuffle
    i2=list(i)
    shuffle(i2)
    #また文字列に戻す
    i="".join(i2)

    #単語の最後の文字
    e=word[-1]

    #print(b,i,e)

    #b,i(変換済み),eをくっつけて文字列にして出力
    return "".join([b,i,e])

wlist=s.split()
ans=[]
for word in wlist:
    #各単語についてtypoglycemia処理
    ans.append(typogly(word))

#各単語を" "(whitespace)で繋いで出力
print(" ".join(ans))