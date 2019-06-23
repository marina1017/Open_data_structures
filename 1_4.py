# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline()
stack = []
set = set()

while line:
    line = f.readline()
    if line in set:
        print(line)
        pass
    else:
        set.add(line.strip())
print(set)

f.close()