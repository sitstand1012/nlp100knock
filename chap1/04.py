#04. 元素記号
"""
“Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，
それ以外の単語は先頭の2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）
への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

s="Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#先頭の1文字を取るindexのリスト
l=[1, 5, 6, 7, 8, 9, 15, 16, 19]

dict={}

#whitespace tokenizeできる
wlist=s.split()

#(index,単語)を出すようにiterate
for i,word in enumerate(wlist):
    c=""

    #1文字を取る場合
    if i+1 in l:
        c=word[:1]
    #2文字を取る場合
    else:
        c=word[:2]

    #indexは自然にするには+1しないといけないことに注意
    dict[c]=i+1
print(dict)