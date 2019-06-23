# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------

# ファイルをオープンする
test_data = open("text.txt", "r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()
striped_lines = map(lambda x:x.strip(),lines)
# dic
dic = {}
for line in striped_lines:
    #辞書内にkeyとして存在しているか
    if dic.get(line) == None:
        dic[line] = 1
    else:
        dic[line] += 1
#辞書をkeyで長さの短い順でソートする
sorted_list = sorted(dic.items(),key=lambda x:len(x[0]))
#重複する行については現れた回数だけ出力させる
for key, value in sorted_list:
    if value > 1:
        print(key)

# ファイルをクローズする
test_data.close()