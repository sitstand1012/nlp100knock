#13. col1.txtとcol2.txtをマージ
"""
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""

import os
import urllib.request
import subprocess

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")


col1path=os.path.join(CHAP2_DIR,"col1.txt")
col2path=os.path.join(CHAP2_DIR,"col2.txt")

#ファイル名に指定はないので"col1_2.txt"で保存することにします
col1_2path=os.path.join(CHAP2_DIR,"col1_2.txt")


col1=[]
col2=[]
ver_program=[]
ver_unix=[]

with open(col1path,"r") as f:
    l1=f.readlines()
with open(col2path,"r") as f:
    l2=f.readlines()
#ここで止まってると12ができてないよー(col1.txtとcol2.txtの長さは揃ってるはず)
assert len(l1)==len(l2)

print("#####Programmable Way#####")
length=len(l1)
sent=[]
for i in range(length):
    sentence="\t".join([l1[i].strip(),l2[i].strip()])
    sent.append(sentence)
    #print(sentence)
    #input()


#指定のpathに書き込み、保存
with open(col1_2path,"w") as f:
    f.write("\n".join(sent))

#再読み込み
with open(col1_2path,"r") as f:
    l=f.readlines()


print("Process complete!")
print("processed txt path is {0}".format(col1_2path))
print()

#処理したtxtデータ(col1_2.txt)の中身を先頭5行表示
print("5 rows of col1_2.txt is like this")
print("-----------------------------")
x=[]
for i,line in enumerate(l):
    if i<5:
        print(line.rstrip())
    if line:
        x.append(line.rstrip())
ver_program.append(x)
print("-----------------------------")
print()


#UNIXコマンド"paste"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()


cmd=["paste col1.txt col2.txt"]
print("Use \"paste\" like executing \"{0}\" to merge 1st column and 2nd column".format(cmd[0]))
print()
#先頭5行表示
print("5 rows result like this")
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().split("\n")
x=[]
for i,line3 in enumerate(printout):
    if i<5:
        print(line3)
    if line3:
        x.append(line3)
ver_unix.append(x)
print("-----------------------------")
print()

#Verification(一応)
if ver_program==ver_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")