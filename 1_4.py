# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline().strip()
stack = []
set = set()

while line:
    if not line in set:
        set.add(line)
        print(line)
    line = f.readline().strip()

f.close()