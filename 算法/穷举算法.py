gj = 0
while gj <= 100 // 5:
    mj = 0 
    while mj <= 100 // 3:
        xj = 100 - gj - mj
        if xj % 3 == 0 and 5 * gj + 3 * mj + xj / 3 == 100:
            print(f"公鸡: {gj}只, 母鸡: {mj}只, 小鸡: {xj}只")
        mj += 1
    gj += 1 
    