a = [23, 15, 5, 6, 7, 90]


while True:
    b = False
    for i in range(0, len(a) - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
            b = True
    if not b:
        break


print(a)
