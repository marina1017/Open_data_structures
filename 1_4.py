# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline()
stack = []
set = set()

while line:
    if line in set:
        pass
    else:
        set.add(line.strip())
        print(line)
    line = f.readline()

f.close()