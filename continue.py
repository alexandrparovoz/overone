while True:
    s = input('Enter something: ')
    if s == 'exit':
        break
    if len(s) < 3:
        print('Too little')
        continue
    print('Entering string sufficient length')