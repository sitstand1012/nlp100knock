#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」

"""
「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""

s1="パトカー"
s2="タクシー"
s=[]

#双方4文字なのを利用してfor文で処理すればおけ
for i in range(4):
    s.append(s1[i])
    s.append(s2[i])
print("".join(s))