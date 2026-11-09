h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())
total_start = h1 * 60 + m1
total_end = h2 * 60 + m2
for i in range(total_start, total_end + 1):
    hours = total_end // 60
    minuts = total_start % 60
    if minuts < 10:
        print(f'{hours}:0{minuts}')
    else:
        print(f'{hours}:{minuts}')