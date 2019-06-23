# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------

# ファイルをオープンする
test_data = open("text.txt", "r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()
# dic
dic = {}
for line in lines:
    dic.get(line) = 0

# ファイルをクローズする
test_data.close()