tag = 'TT_101'
print(tag[0], tag[3], tag[-1], len(tag))

line = '2026-10-24 08:15:00'
print(line[0:4], line[5:7], line[:10], line[11:], line[-8:-3])

digits = '0123456789'
print(digits[::2], digits[1::2], digits [::-1])

levels = [42.1, 42.3, 42.0, 41.8, 41.9, 42.5, 43.0, 43.2]
print(levels[-3:], levels[:2], levels[-100:])

row = '2026-10-19 08:15:00;TT_101;85,4;OK'
parts = row.split(';')
print(parts, parts[2])
print(' НАСОС H-2 АВАРИЯ '.split())
print('TT_101.PV'.partition('.'), 'TT_101'.partition('.'))

tag2 = 'PT_204.PV'
print('PT' in tag2, tag2.startswith(('TT', 'PT')), tag2.endswith('.SP'))
print('204'.isdigit(), '-2'.isdigit(), '2.5'.isdigit())

print(';'.join(['2026-10-19', 'TT_101', '85.4']))
log = 'AL:H2 AL:LT12 AL:H2 OK AL:H2'
print(log.count('AL:H2'), log.find('LT'), log.find('FT'))