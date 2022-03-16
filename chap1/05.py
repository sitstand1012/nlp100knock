#05. n-gram
"""
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

#文字ごとのbigram
def char_bigram(s):
    l=[]

    #単語列に
    wlist=s.split()

    #単語ごとに
    for word in wlist:
        #[BOW]+1文字目のbi-gram
        l.append("".join(["_", word[0]]))
        for i in range(len(word)-1):
            #i文字め+(i+1)文字めのbi-gram
            l.append("".join([word[i], word[i+1]]))
        #最後の文字+[EOW]のbi-gram
        l.append("".join([word[-1], "_"]))
    return l

#単語ごとのbigram
def word_bigram(s):
    l=[]
    wlist=s.split()
    #[BOS]+最初の単語のbi-gramを作る
    l.append(["[BOS]", wlist[0]])
    for i in range(len(wlist)-1):
        #i単語目+(i+1)単語目のbi-gram
        l.append([wlist[i],wlist[i+1]])
    #最終単語+[EOS]のbi-gramを作る
    l.append([wlist[-1],"[EOS]"])
    return l

s="I am an NLPer"

#[BOW],[EOW]は_で表す
print(char_bigram(s))
print(word_bigram(s))

