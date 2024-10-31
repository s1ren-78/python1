ex_1=289
match ex_1:
    case 2:
        print('happy')
    case 3:
        print('halo')
    case 4:
        print('sad')
        #匹配的更多
    case 35|27|68:
        print('hhh')
    case _:#通用匹配符
        print('000')
