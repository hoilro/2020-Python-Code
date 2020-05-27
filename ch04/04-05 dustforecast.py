PM = float(input('미세먼지(10마이크로그램)의 농도는?'))
if 151 <= PM:
    print('미세먼지 농도: {:.2f}, 등금: {}'.format(PM, '매우나쁨'))
if 81 <= PM:
    print('미세먼지 농도: {:.2f}, 등금: {}'.format(PM, '나쁨'))
if 31 <= PM:
    print('미세먼지 농도: {:.2f}, 등금: {}'.format(PM, '보통'))
else:
    print('미세먼지 농도: {:.2f}, 등금: {}'.format(PM, '좋음'))

