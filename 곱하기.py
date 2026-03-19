import random

count = int(input('풀 문제수'))
while True:
    a = [2, 3, 4, 5, 6, 7, 8, 9]
    b = [random.choice(a), random.choice(a)]
    answer = b[0] * b[1]
    print(b[0], 'x', b[1])
    count -= 1
    input( )
    print(answer)
    input( )
    if count < 1:
        print('끝')
        break