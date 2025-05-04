t = input().split()
reg = input()

troom = int(t[0])
match reg:
    case 'freeze':
        if troom > int(t[1]): troom = int(t[1])
    case 'heat':
        if troom < int(t[1]): troom = int(t[1])
    case 'auto':
        troom = int(t[1])
    case 'fan':
        pass

print(troom)