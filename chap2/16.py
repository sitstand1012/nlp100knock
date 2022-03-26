#16. ファイルをN分割する
"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
"""

import os
import subprocess
from math import *

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]

#今回は、popular-names.txtを使うことにします
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

ver_program=[]
ver_unix=[]
unix_split_suffixes=[]

#splitでは[a-z]*2の26^2=676ファイルまでしか分割できない
max_split=676

for i in range(26):
    for j in range(26):
        c1=chr(ord("a")+i)
        c2=chr(ord("a")+j)
        unix_split_suffixes.append("".join([c1,c2]))

with open(txtpath,"r") as f:
    l=f.readlines()

print("How many numbers of files of {0} do you want to split into (max {1}) ? ".format(txtpath,max_split))

#標準入力により、分割数nを指定。
n=max(1,min(int(input()),min(len(l),max_split)))
print()
onefile_length=ceil(len(l)/n)
print("about {0} lines per file".format(onefile_length))
print()
print("#####Programmable Way#####")

#n分割します
print("Split into {0} files.".format(n))
x=[]
for i,line in enumerate(l):
    if (i%onefile_length)==0:
        if (n!=len(l))and(i==0):
            pass
        else:
            ind=(i+1)//onefile_length
            with open(os.path.join(CHAP2_DIR,"out"+str(ind)),"w") as f:
                f.write("".join(x))
        x=[]
    if line:
        x.append(line)
if x:
    with open(os.path.join(CHAP2_DIR, "out" + str(ind+1)), "w") as f:
        f.write("".join(x))
print("completed.")

print("-----------------------------")
for i in range(n):
    with open(os.path.join(CHAP2_DIR,"out"+str(i+1)),"r") as f:
        l=f.readlines()
    x=[]
    for j,line in enumerate(l):
        if j==0:
            print("head line of \"out{0}\" is \"{1}\"".format(i+1,line.strip()))
        if line:
            x.append(line.strip())
    ver_program.append(x)
print("-----------------------------")
print()

#UNIXコマンド"split"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()

cmd=["split -l {0} {1} out".format(onefile_length,txtpath)]
print("Use \"split\" like executing \"{0}\" \n to split into {1} files of txt ({2})".format(cmd[0],n,txtpath))
print()
out=subprocess.check_output(cmd,shell=True)

print("-----------------------------")
for i in range(n):
    with open(os.path.join(CHAP2_DIR,"out"+unix_split_suffixes[i]),"r") as f:
        l=f.readlines()
    x=[]
    for j,line in enumerate(l):
        if j==0:
            print("head line of \"out{0}\" is \"{1}\"".format(unix_split_suffixes[i],line.strip()))
        if line:
            x.append(line.strip())
    ver_unix.append(x)
print("-----------------------------")

#Verification(一応)
if ver_program==ver_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")