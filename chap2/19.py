#19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
"""
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
"""

import os
import subprocess
from collections import OrderedDict

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]

txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

#ちゃんとソートできてるかのflag
ver_prog=[]
ver_unix=[]

with open(txtpath,"r") as f:
    l=f.readlines()

#あとで使うのでデータ数を取っておく
n=len(l)

list_firstline=[]

print("#####Programmable Way#####")

od=OrderedDict()
for i,line in enumerate(l):
    if line:
        spl=line.split()
        #print(spl,spl[0])
        od[spl[0]]=od.get(spl[0],0)+1

sortedod=sorted(od.items(),key=lambda x:(-x[1],x[0]))

print("After sort, top 5 elements of 1st row are like this")
print("-----------------------------")
for i,inst in enumerate(sortedod):
    if i<5:
        print("\t".join([inst[0],str(inst[1])]).rstrip())
    if line:
        ver_prog.append([inst[0],str(inst[1])])
print("-----------------------------")
print()


#UNIXコマンド"sort"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()

cmd=["cut -f 1 {0} | sort | uniq -c | sort -k 1nr".format(txtpath)]
print("Use \"sort\" like executing \"{0}\" \n to sort 1st line in txt ({1})".format(cmd[0],txtpath))
print()
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().rstrip().split("\n")
print("After sort, output of first 5 rows are like this")
print("-----------------------------")
for i,line in enumerate(printout):
    if i<5:
        print(line.rstrip())
    if line:
        inst=line.strip().split(" ")
        ver_unix.append([inst[1], str(inst[0])])

print("-----------------------------")
print()

#Verification(一応)
if ver_prog==ver_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")