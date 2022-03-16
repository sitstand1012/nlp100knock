#03. 円周率
"""
“Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”
という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""

s="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
wlenl=[]

#split()すると" "(whitespace)ごとに切れるはず
l=s.split()

#iterativeに単語をとる
for word in l:
    #,.を除去
    true_word=word.replace(".","").replace(",","")
    #lenで長さを取れる
    wlenl.append(len(true_word))
print(wlenl)