# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline().strip()
stack = []
set = set()

while line:
    if line in set:
        print(line)
        
    else:
        set.add(line)
    line = f.readline().strip()

f.close()