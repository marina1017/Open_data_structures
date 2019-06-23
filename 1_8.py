# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------

# ファイルをオープンする
test_data = open("text1.txt", "r")

# 行ごとにすべて読み込んでリストデータにする
lines = test_data.readlines()
striped_lines = map(lambda x:x.strip(),lines)
lists = []
#行数を数える
count = 0
for line in striped_lines:
    #偶数ならば
    if count % 2 == 0:
        print(line)
    else:
        lists.append(line)
    count += 1

for list in lists:
    print(list)