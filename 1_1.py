# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline()
stack = []

while line:
    stack.append(line.strip())
    for _ in range(len(stack)):
        print("stack.pop()",stack.pop())
    line = f.readline()
# ファイルをクローズする
f.close()