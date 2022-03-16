#05. n-gram
"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

def char_bigram(s):
    l=[]
    for i in range(len(s)-1):
        if i==0:
            l.append("".join(["_",s[i]]))
        l.append("".join([s[i],s[i+1]]))
    l.append("".join([s[-1], "_"]))
    return l

def word_bigram(s):
    l=[]
    wlist=s.split()
    for i in range(len(wlist)-1):
        if i==0:
            l.append(["[BOS]",wlist[i]])
        l.append([wlist[i],wlist[i+1]])
    l.append([wlist[-1],"[EOS]"])
    return l
def process(s):
    l=list(s)
    l.append("*")
    l.insert(0,"*")
    return "".join(l)


s="I am an NLPer"

#[BOS],[EOS]は_で表すことも
print(char_bigram(s))
print(word_bigram(s))

