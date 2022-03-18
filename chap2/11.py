#11. タブをスペースに置換
"""
タブ1文字につきスペース1文字に置換せよ．
[行間補完]###そののちに整形したデータを直に出力せよ(一部で良い)###
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

import os
import urllib.request
import subprocess

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

with open(txtpath,"r") as f:
    l=f.readlines()

#verificationを行うための配列
ver_program=[]
ver_unix=[]

#まず、てはじめにもとの先頭5行を確認。
print("First, 5 rows are like this")
print("-----------------------------")
for i,line in enumerate(l):
    if i<5:
        print(line.rstrip())
print("-----------------------------")
print()

#プログラムを利用した解決法
print("#####Programmable Way#####")
l2=[]
for line in l:
    #replace("\t"," ")で"\t"(タブ)->" "(whitespace)へ変換
    shaped=line.rstrip().replace("\t"," ")
    l2.append(shaped)

#できたやつを先頭5行確認
print("By the program, 5 rows became like this")
print("-----------------------------")
x=[]
for i,line2 in enumerate(l2):
    if i<5:
        print(line2)
    if line2:
        x.append(line2)
ver_program.append(x)
print("-----------------------------")
print()

#UNIXコマンドを利用した解決法
print("#####UNIX Command Way#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
#その後の実行コマンドを短く、見やすくするためにcdをしてそのファイル直下に移ります
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()

#expandを利用した方法
cmd=["expand -t 1 popular-names.txt"]
print("1. Use \"expand\" like executing \"{0}\"".format(cmd[0]))
"""
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().split("\n")
for i,line3 in enumerate(printout):
    if i<5:
        print(line3)
    #input()
print("-----------------------------")
print()
"""

#sedを利用した方法
cmd=["sed -e 's/\t/\ /g' popular-names.txt"]
print("2. Use \"sed\" like executing \"{0}\"".format(cmd[0]))
"""
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().split("\n")
for i,line3 in enumerate(printout):
    if i<5:
        print(line3)
    #input()
print("-----------------------------")
print()
"""

#trを利用した方法
cmd=["cat popular-names.txt | tr '\t' '\ '"]
print("3. Use \"tr\" like executing \"{0}\"".format(cmd[0]))
print()

#全部同じ結果になるんでtrの場合だけ実行
#先頭5行だけ確認
print("All results are same as this")
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().split("\n")
x=[]
for i,line3 in enumerate(printout):
    if i<5:
        print(line3)
    #input()
    if line3:
        x.append(line3)
ver_unix.append(x)
print("-----------------------------")
print()
#Verification(いちおう)
if ver_program==ver_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")