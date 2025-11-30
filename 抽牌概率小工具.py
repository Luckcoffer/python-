#第四代
print('====抽牌概率小工具====')
print('\n如要退出，请输入quit\n')
def jiechen(n):
    num = 1
    for i in range(1,n+1):
        num = num*i
    return num
while True:
    total_cards = input('总牌数 = ')
    if total_cards.lower() == 'quit' or total_cards.lower() == 'quit' :
        print('感谢使用')
        break
    try:
        total_cards = int(total_cards)
        desired_cards = int(input('期望牌的个数 = '))
        if desired_cards > total_cards:
            print('情况不存在，请重新输入')
            continue
        draw_cards = int(input('抽牌数 = '))
        if draw_cards >= total_cards:
            print('概率100%！！！')
            continue
        a = jiechen(total_cards)
        b = jiechen(draw_cards)
        c = jiechen(total_cards-draw_cards)
        d = jiechen(total_cards-desired_cards)
        e = jiechen(total_cards-desired_cards-draw_cards)
        all_conditions = a/(b*c)
        opposite_conditions = d/(b*e)
        probability = 1-opposite_conditions/all_conditions
        desired_cards_number = draw_cards * (desired_cards/total_cards)
        print(f'抽到牌的概率为{probability:.1%}')
        print('抽到牌的期望值为%.1f'%(desired_cards_number))
    except ValueError:
        print('输入无效，请输入数字')
        continue