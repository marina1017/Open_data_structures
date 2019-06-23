# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
f = open('text.txt', 'r')
line = f.readline()
stack = []

def reverse_print(stack):
    for _ in range(len(stack)):
            print("stack.pop()",stack.pop())

while line:
    
    if len(stack) >= 3 and line == '\n':
        print("3行目以降で改行ありました")
        reverse_print(stack)
    else:
        stack.append(line.strip())
    line = f.readline()
reverse_print(stack)
f.close()