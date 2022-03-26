#18. 各行を3コラム目の数値の降順にソート
"""
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""

import os
import subprocess

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]

txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

#ちゃんとソートできてるかのflag
ver_prog=True
ver_unix=True

with open(txtpath,"r") as f:
    l=f.readlines()

#あとで使うのでデータ数を取っておく
n=len(l)

prog=[]

print("#####Programmable Way#####")


for i,line in enumerate(l):
    if line:
        #1行ずつsplitする
        spl=line.split()
        #print(spl,spl[0])
        prog.append(spl)

        #3列目を数値sortするので、intにキャストする
        prog[-1][2]=int(prog[-1][2])

#3列目の降順sort
prog.sort(key=lambda x:-x[2])

for i in range(n):
    prog[i][2]=str(prog[i][2])

print("After sort, first 5 rows are like this")
print("-----------------------------")
for i,line in enumerate(prog):
    if i<5:
        print("\t".join(line).rstrip())
print("-----------------------------")
print()

#降順になってるか確認
cnt=float("inf")
for i in range(n):
    num=int(prog[i][2])
    if num<=cnt:
        cnt=num
    else:
        ver_prog=False
        break

#UNIXコマンド"sort"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()

cmd=["sort -r -k 3 -n {0}".format(txtpath)]
print("Use \"sort\" like executing \"{0}\" \n to sort 1st line in txt ({1})".format(cmd[0],txtpath))
print()
out=subprocess.check_output(cmd,shell=True)
printout=out.decode().rstrip().split("\n")

print("After sort, first 5 rows are like this")
print("-----------------------------")
for i,line in enumerate(printout):
    if i<5:
        print(line.rstrip())
print("-----------------------------")
print()

#降順になってるか確認
cnt=float("inf")
for line in printout:
    if line:
        x=line.split("\t")
        num=int(x[2])
        if num <= cnt:
            cnt = num
        else:
            ver_unix = False
            break

#Verification(一応)
if (ver_prog)and(ver_unix):
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")