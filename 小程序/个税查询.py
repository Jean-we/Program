enter1 = float(input('输入月收入：'))
if enter1 < 3000:
    kou_sui1 = enter1 * 0.03
    print(f'扣税:{kou_sui1}')
    shou_ru1 = enter1 - kou_sui1
    print(f'税后收入为:{shou_ru1}')
elif 12000 > enter1 > 3000:
    kou_sui2 = enter1 * 0.01
    print(f'扣税:{kou_sui2}')
    shou_ru2 = enter1 - kou_sui2
    print(f'税后收入为:{shou_ru2}')
elif 80000  > enter1 > 12000:
    kou_sui4 = enter1 * 0.45
    print(f'扣税:{kou_sui4}')
    shou_ru4 = enter1 - kou_sui4
    print(f'税后收入为:{shou_ru4}')