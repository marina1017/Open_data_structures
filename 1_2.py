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
    stack.append(line.strip())
    if len(stack) == 3:
        reverse_print(stack)
    line = f.readline()

reverse_print(stack)

f.close()