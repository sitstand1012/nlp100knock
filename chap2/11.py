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

print("First, 5 rows are like this")
print("-----------------------------")
for i,line in enumerate(l):
    if i<5:
        print(line.rstrip())
print("-----------------------------")
print()
print("#####Programmable Way#####")
l2=[]
for line in l:
    l2.append(line.rstrip().replace("\t"," "))
print("By the program, 5 rows became like this")
print("-----------------------------")
for i,line2 in enumerate(l2):
    if i<5:
        print(line2)
    #input()
print("-----------------------------")
print()
print("#####UNIX Command Way#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
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
cmd=["cat popular-names.txt | tr '\t' '\ '"]
print("3. Use \"tr\" like executing \"{0}\"".format(cmd[0]))
print()
print("All results are same as this")
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().split("\n")
for i,line3 in enumerate(printout):
    if i<5:
        print(line3)
    #input()
print("-----------------------------")
