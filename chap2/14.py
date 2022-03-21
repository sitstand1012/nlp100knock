#14. 先頭からN行を出力
"""
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
"""

import os
import urllib.request
import subprocess

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]

#今回は、popular-names.txtを使うことにします
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

ver_program=[]
ver_unix=[]

with open(txtpath,"r") as f:
    l=f.readlines()

#どんな入力があっても、この行数より多い行数は出さないようにします。(視認性のため)
#適宜数字を変えて良い
max_printnum=min(10,len(l))

print("How many lines of beginning of {0} do you want to fetch ? (max {1})".format(txtpath,max_printnum))

#標準入力により、行数nを指定。
n=max(1,min(int(input()),max_printnum))

print("#####Programmable Way#####")

#先頭n行表示
print("Print {0} head lines.".format(n))
print("-----------------------------")
for i,line in enumerate(l):
    if i<n:
        print(line.strip())
        if line:
            ver_program.append(line.strip())

print("-----------------------------")
print()


#UNIXコマンド"head"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()


cmd=["head -n {0} {1}".format(n,txtpath)]
print("Use \"head\" like executing \"{0}\" \n to print {1} lines of head of txt ({2})".format(cmd[0],n,txtpath))
print()
#先頭n行表示
print("Print {0} head lines.".format(n))
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().split("\n")
x=[]
for i,line3 in enumerate(printout):
    if i<n:
        print(line3)
        if line3:
            ver_unix.append(line3)
print("-----------------------------")
print()

#Verification(一応)
if ver_program==ver_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")