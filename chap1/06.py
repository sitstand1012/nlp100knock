#06. 集合
"""
“paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

#TrueをYesに、FalseをNoにするだけ
def convbool(flag):
    if flag:
        return "Yes"
    else:
        return "No"

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

sx="paraparaparadise"
sy="paragraph"

X=set(char_bigram(sx))
Y=set(char_bigram(sy))

#定義通りのX,Y
print("X=",X)
print("Y=",Y)


#和集合
uni=X|Y
print("X|Y(和集合)=",uni)

#積集合
pro=X&Y
print("X&Y(積集合)=",pro)

#差集合
sub=X-Y
print("X-Y(差集合)=",sub)

print("Q.\"se\" is in X ? A.{0}".format(convbool(("se" in X))))
print("Q.\"se\" is in Y ? A.{0}".format(convbool(("se" in Y))))