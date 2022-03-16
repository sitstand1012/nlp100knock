#05. n-gram
"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

#文字ごとのbigram
def char_bigram(s):
    l=[]
    for i in range(len(s)-1):
        #[BOS]+1文字目のbi-gramを作る
        if i==0:
            l.append("".join(["_",s[i]]))
        #i文字目+(i+1)文字目のbi-gram
        l.append("".join([s[i],s[i+1]]))
    #最終文字+[EOS]のbi-gramを作る
    l.append("".join([s[-1], "_"]))
    return l

#単語ごとのbigram
def word_bigram(s):
    l=[]
    wlist=s.split()
    for i in range(len(wlist)-1):
        #[BOS]+1単語めのbi-gramを作る
        if i==0:
            l.append(["[BOS]",wlist[i]])
        #i単語目+(i+1)単語目のbi-gram
        l.append([wlist[i],wlist[i+1]])
    #最終単語+[EOS]のbi-gramを作る
    l.append([wlist[-1],"[EOS]"])
    return l

s="I am an NLPer"

#[BOS],[EOS]は_で表すことも
print(char_bigram(s))
print(word_bigram(s))

