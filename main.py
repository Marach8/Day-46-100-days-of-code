print('\033[4mMOKEBEAST\033[0m')
print()

dict = {}
info = ['Beast name', 'Type', 'Special Move', 'HP', 'MP']

print('Enter the following details for your Mokebeast')
print()
for i in info:
  if i == 'Type':
    print(f'{i} (Air,Earth, Water, Spirit or Fire), ', end='')
  else:
    print(f'{i}, ', end='')
print()

def printer(a):
  info[2] = 'Sp.Move'
  print()
  for c in info:
    if c == info[-1]:
      print(f'\033[1;33m{c:^10}\033[0m', end='')
    else:
      print(f'\033[1;33m{c:^10}\033[0m', end='|')
  print()
  print('__________________________________________________')
  for i, j in a.items():
    print(f'\033[34m{i:^10}\033[0m', end='|')
    for m, n in j.items():
      if m == 'MP':
        print(f'{n:^10}', end='')
      else:
        print(f'{n:^10}', end='|')
    print()
while True:
  print()
  a = input('''\033[0;33mEnter the details in the other above seperating each with a comma
\033[0m>> ''').split(',')
  
  for k in a:
    dict[a[0]] = {'Type': a[1], 'Special Move': a[2], 'HP': a[3], 'MP': a[4]}

  print()
  ask = input('Do you want to input another Beast? y/n: ').lower()
  if ask == 'y':
    continue
  else:
    break
printer(dict) 