#10. 行数のカウント
"""
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""

import os
import urllib.request
import subprocess

#タスクファイルのurl
url="https://nlp100.github.io/data/popular-names.txt"

#popular-names.txtをダウンロードするpathを指定します
CHAP2_DIR=os.environ["NLP100KNOCK_CHAP2_DIR"]
txtpath=os.path.join(CHAP2_DIR,"popular-names.txt")

#実際にダウンロード
urllib.request.urlretrieve(url, txtpath)


print("#####Programmable Way#####")
with open(txtpath,"r") as f:
    #readlines()は1行ごとに分けての読み込みだから
    l=f.readlines()

#len(l)で行数が判るってワケ
print("rows counted by program = \033[1m{0}\033[0m".format(len(l)))
print()
#print(os.getcwd())

print("#####UNIX Command Way#####")

#その後の実行コマンドを短く、見やすくするためにcdをしてそのファイル直下に移ります
os.chdir(CHAP2_DIR)
print("(Do \"cd {0}\")".format(CHAP2_DIR))

#subprocess.check_outputを利用して、シェルでの動きを再現しています。
#まぁ動かしてみればわかる。
cmd=["wc -l popular-names.txt"]
print("then, inputted command is \"{0}\"".format(cmd[0]))
print()
print("raw command output is below")
print("-----------------------------")
out=subprocess.check_output(cmd,shell=True)     #shell=Trueはセキュリティ上アブナイらしい(要検討)
print(out.decode().rstrip())
print("-----------------------------")
print()

out=out.decode().strip().split()
#print(out)
print("rows counted by unix command = \033[1m{0}\033[0m".format(out[0]))
print()

#Verification(いちおう)
if int(len(l))==int(out[0]):
    print("\033[1mResults verified\033[0m")
else:
    print("Should have some error... (Maybe not critical (like data type))")

