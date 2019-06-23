# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline()
stack = []

while line:
    stack.append(line.strip())
    line = f.readline()
    
for _ in range(len(stack)):
    print("stack.pop()",stack.pop())
# ファイルをクローズする
f.close()