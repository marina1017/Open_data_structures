# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
# f = open('text.txt', 'r')
# line = f.readline().strip()
# stack = []
# set = set()

# while line:
#     set.add(line)
#     sorted_set = sorted(set)
#     print("sorted_set",sorted_set)
#     # if line in set:
#     #     print(line)
        
#     # else:
#     #     set.add(line)
#     line = f.readline().strip()

# f.close()

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