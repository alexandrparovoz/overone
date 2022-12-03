if __name__ == '__main__':

# мой список покупок

    shoplist = ['apple', 'mango','carrot', 'banana']
    print('I must to do ', len(shoplist), 'things.')

    print('Buying: ', end='')
    for item in shoplist:
        print(item, ', ', end='')

    print('\nAlso i need to buy rise')
    shoplist.append('rise')
    print('Now my shoplist looks like this:', shoplist)
    print('Sorting of my list.')
    shoplist.sort()
    print('Sorting list now looks like this:', shoplist)

    print('First what I must to buy is', shoplist[0])
    olditem= shoplist[0]
    del shoplist[0]
    print('I buying ', olditem[0])
    print('now my shoplist ', shoplist)



