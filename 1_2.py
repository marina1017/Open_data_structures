# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline()
stack = []
count = 0
count1 = 0

while line:
    stack.append(line.strip())
    if len(stack) == 3:
        for _ in range(len(stack)):
            print("stack.pop()",stack.pop())
    line = f.readline()
    
f.close()