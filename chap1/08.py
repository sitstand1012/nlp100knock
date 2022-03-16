#08. 暗号文
"""
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
・英小文字ならば(219 - 文字コード)の文字に置換
・その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""

#英小文字列
alp=[chr(ord("a")+i) for i in range(26)]
#print(alp)

#暗号化関数
def cipher(s):
    ret=[]
    #文章内を1文字ずつ見る
    for c in s:
        #文字が英小文字なら
        if c in alp:
            #指定の変換を
            ret.append(chr(219-ord(c)))
        #そうでないなら
        else:
            #そのまま
            ret.append(c)
    return "".join(ret)


#明日赤段位ってマジ？前作九段受けたことないけどひょっとしたらワンチャンあるっしょ。俺はサファリとギガデリが極端に苦手なだけで地力はあるし。
s="Tomorrow, there is a RED Dan Rank, really? " \
  "I've never taken the previous 9-dan, but maybe there's a chance. " \
  "I'm just extremely bad at Safari and Gigadelli, but I have the EARTH POWER."

print(cipher(s))