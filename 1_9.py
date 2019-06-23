import random

# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------

# ファイルをオープンする
test_data = open("text1.txt", "r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()
striped_lines = list(map(lambda x:x.strip(),lines))
random.shuffle(striped_lines)
for list in striped_lines:
    print(list)
