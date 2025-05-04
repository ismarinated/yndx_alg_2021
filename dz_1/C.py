tel = []

for i in range(4):
    line = input()
    tn = ''.join([ch for ch in line if ch in '0123456789'])

    dic = {
        'code' : '',
        'num' : ''
    }

    if len(tn) == 7:
        dic['code'] = '495'
        dic['num'] = tn

    else:
        dic['code'] = tn[1:4]
        dic['num'] = tn[4:]

    tel.append(dic)

for i in range(3):
    if tel[0] == tel[i + 1]: print('YES')
    else: print('NO')