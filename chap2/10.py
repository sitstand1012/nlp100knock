#10. 行数のカウント
"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import os
import urllib.request
import subprocess


url="https://nlp100.github.io/data/popular-names.txt"
CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")
urllib.request.urlretrieve(url, txtpath)


print("#####Programmable Way#####")
with open(txtpath,"r") as f:
    l=f.readlines()
print("row counted by program = \033[1m{0}\033[0m".format(len(l)))
print()
#print(os.getcwd())

print("#####UNIX Command Way#####")

os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))
cmd=["wc -l popular-names.txt"]
print("then, inputted command is \"{0}\"".format(cmd[0]))
print()
print("raw command out put is below")
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)
print(out.decode().rstrip())
print("-----------------------------")
print()

out=out.decode().strip().split()
#print(out)
print("row counted by unix command = \033[1m{0}\033[0m".format(out[0]))


