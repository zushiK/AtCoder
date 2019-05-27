s = input()
s1 = int(s[0:2])
s2 = int(s[2:4])
flag1 = False
flag2 = False

if s1 > 0 and s1 < 13:
    flag1 = True
if s2 > 0 and s2 < 13:
    flag2 = True


if flag1 and flag2:
    print('AMBIGUOUS')
elif flag1 and not flag2:
    print('MMYY')
elif not flag1 and flag2:
    print('YYMM')
else:
    print('NA')
