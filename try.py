import os
num_to_character={'0': '零', '1': '一', '2': '二', '3': '三','4': '四',
       '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}
character_to_num = dict()
for key, value in num_to_character.items():
    character_to_num[value] = int(key)
character_to_num['两'] = '2'


def tran(chara):
    res = 0
    mark = 0
    for c in chara:
        if c in character_to_num:
            if mark == 0:
                mark = character_to_num[c]
            else:
                mark = mark*10 + character_to_num[c]
        elif c == '万':
            res += mark*10000
            mark = 0
        elif c == '千':
            res += mark * 1000
            mark = 0
        elif c == '百':
            res += mark * 100
            mark = 0
        elif c == '十' and mark:
            res += mark * 10
            mark = 0
        elif c == '十' and not mark:
            res += 10
    if mark:
        res += mark
    return '%04d' % res


def change(txt_name, path=None):
    ss = txt_name.split()
    order = ss[0]
    name = ' '.join(ss[1:])
    if order[0] == '第':
        order = order[1:]
    if order[-1] == '章':
        order = order[:-1]
    # if order.isdecimal():
    #     return order
    # else:
    #     return tran(order)
    if order.isdigit():
        new = order + ' ' + name
    else:
        new = tran(order) + ' ' + name
    os.rename(path+txt_name, path+new)


if __name__ == '__main__':
    novel_path = '/home/zhanghua/novels/绝世邪神/'
    chapter_list = os.listdir(novel_path)
    for chapter in chapter_list:
        change(chapter, novel_path)
