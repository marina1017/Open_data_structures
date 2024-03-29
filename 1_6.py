# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------

# ファイルをオープンする
test_data = open("text.txt", "r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()

Sset = set(map(lambda x:x.strip(),lines))
# 一行ずつ表示する
sorted_set = sorted(Sset, key=lambda x: len(x))
print(sorted_set)

# ファイルをクローズする
test_data.close()