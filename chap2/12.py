#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
"""
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
"""

import os
import subprocess

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

#col1.txtとcol2.txtの保存場所を指定
col1path=os.path.join(CHAP2_DIR,"col1.txt")
col2path=os.path.join(CHAP2_DIR,"col2.txt")

col1=[]
col2=[]
ver_program=[]
ver_unix=[]

with open(txtpath,"r") as f:
    l=f.readlines()

print("First, 5 rows are like this")
print("-----------------------------")
for i,line in enumerate(l):
    if i<5:
        print(line.rstrip())
print("-----------------------------")
print()

print("#####Programmable Way#####")
for line in l:
    #"\t"(tab)で分ける
    lis=line.split("\t")
    #print(lis)

    #index=0が1行目、index=1が2行目に相当
    col1.append(lis[0])
    col2.append(lis[1])

#指定のpathに書き込み、保存
with open(col1path,"w") as f:
    f.write("\n".join(col1))
with open(col2path,"w") as f:
    f.write("\n".join(col2))

#再読み込み
with open(col1path,"r") as f:
    l1=f.readlines()
with open(col2path,"r") as f:
    l2=f.readlines()

print("Process complete!")
print("col1.txt path is {0}".format(col1path))
print("col2.txt path is {0}".format(col2path))
print()

#col1.txtの中身を先頭5行表示
print("5 rows of col1.txt is like this")
print("-----------------------------")
x=[]
for i,line in enumerate(l1):
    if i<5:
        print(line.rstrip())
    if line:
        x.append(line.rstrip())
ver_program.append(x)
print("-----------------------------")
print()

#col2.txtの中身を先頭5行表示
print("5 rows of col2.txt is like this")
print("-----------------------------")
x=[]
for i,line in enumerate(l2):
    if i<5:
        print(line.rstrip())
    if line:
        x.append(line.rstrip())
ver_program.append(x)
print("-----------------------------")
print()

#UNIXコマンド"cut"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()

#比較の都合上、1行目・2行目を2回に分けて取ってきている
#コマンドの中身はおして知るべし。
cmd=["cut -f 1 popular-names.txt"]
print("1. Use \"cut\" like executing \"{0}\" to slice 1st column".format(cmd[0]))
print()
#1行目の先頭5行表示
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

cmd=["cut -f 2 popular-names.txt"]
print("2. Use \"cut\" like executing \"{0}\" to slice 2nd column".format(cmd[0]))
print()
#2行目の先頭5行表示
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

#もし、まとめて取りたいならこうしてね
cmd=["cut -f 1,2 popular-names.txt"]
print("(if you want to fetch 2 column one time, type \"{0}\")".format(cmd[0]))
print()

#Verification(一応)
if ver_program==ver_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")