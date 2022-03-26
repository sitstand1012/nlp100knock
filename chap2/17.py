#17. １列目の文字列の異なり
"""
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはcut, sort, uniqコマンドを用いよ．
"""

import os
import subprocess

CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]

txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

with open(txtpath,"r") as f:
    l=f.readlines()

print("#####Programmable Way#####")

first_line_set=set()

#splitしてindex=0を取り出すだけ
for i,line in enumerate(l):
    if line:
        spl=line.split()
        #print(spl,spl[0])
        first_line_set.add(spl[0])
        #input()
print("The set of first line processed by program is below")
print("-----------------------------")
print(first_line_set)
print("-----------------------------")
#input()


#UNIXコマンド"cut,sort,uniq"を利用した確認
print("#####Verification by UNIX Command#####")
print("First, change the directory to \"NLP100KNOCK_CHAP2_DIR\"")
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
print()

cmd=["cut -f 1 {0} | sort | uniq".format(txtpath)]
print("Use \"cut,sort,uniq\" like executing \"{0}\" \n to count uniqueness of 1st line in txt ({1})".format(cmd[0],txtpath))
print()
out=subprocess.check_output(cmd,shell=True)
first_line_set_unix=set(out.decode().rstrip().split("\n"))

print("The set of first line processed by unix command is below")
print("-----------------------------")
print(first_line_set_unix)
print("-----------------------------")

#Verification(一応)
if first_line_set==first_line_set_unix:
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")