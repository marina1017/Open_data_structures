# ----------------------------------------------------
# ファイルの読み込み
# ----------------------------------------------------
# test_data = open('text.txt', 'r')

# stack = []
# for line in test_data:
#     #スタックに詰める
#     stack.append(line)

# for _ in range(len(stack)):
#     print(stack.pop())
# # ファイルをクローズする
# test_data.close()

f = open('text.txt', 'r')
line = f.readline()
stack = []

while line:
    stack.append(line.strip())
    if len(stack) < 3 and line == '\n':
        print("3行目以降で改行ありました")
        stack.pop()
        for _ in range(len(stack)):
            print("stack.pop()",stack.pop())
    else:
        if len(stack) == 3:
            for _ in range(len(stack)):
                print("stack.pop()",stack.pop())
    line = f.readline()
f.close()