''' Сеты/множество '''


friends = {'Вася', 'Ася', 'Петя'}
prodrammers = {'Вася', 'Анотолий'}

print('intersection')
print(friends.intersection(prodrammers))
print('-' * 20)  #кто был

print('difference')
print(friends.difference(prodrammers))
print('-' * 20)  #кого не было

print('union')
print(friends.union(prodrammers))
print('-' * 20)  #все кто был

print('symmetric_difference')
print(friends.symmetric_difference(prodrammers))
print('-' * 20)  #были один раз

