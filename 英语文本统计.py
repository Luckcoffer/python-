def idenity(test):
    Diction = {}
    for character in test:
        Diction.setdefault(character,0)
        Diction[character] += 1
    sort_Diction = dict(sorted(Diction.items(),key=lambda x: x[1],reverse=True))
    return sort_Diction
def merge_diction(Diction):
    merged = {}
    for key,value in Diction.items():
        lower_key = key.lower()
        if lower_key in merged:
            merged[lower_key] += value
        else:
            merged[lower_key] = value
    return merged
def number(Diction):
    total_number = 0
    rate = 0
    for key in Diction.keys():
        total_number += Diction.get(key,0)
    for key in Diction.keys():
        rate = Diction.get(key,0)/total_number
        print(key + ':'+f"{rate*100:.1f}%")
def detective(test):
    a = merge_diction(idenity(test))
    print(a)
    print('总数：'+str(len(test)))
    number(a)
while True:
    print('如果想要退出，输入break')
    test = input('请输入文本；')
    if test == 'break' or test == 'break':
        break
    detective(test) 
    continue