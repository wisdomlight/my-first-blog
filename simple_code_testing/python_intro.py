dict = {}
print('Hello, Django girls!')
in_ = input("what is your name")
while in_ != 'Exit!':

    dict['name'] = in_

    print('Here\'s the name added to dict', dict['name'])

    if dict['name']== 'Sherab':
        print(dict['name'] ,'is admin on this machine')
    elif dict['name']  == 'sherab':
        print(dict['name'] + 'is' + dict['name'].isupper())
    else:
        print('Hi'+ dict['name'] + ',for admin rights you\'ll need Sherab')

    in_ = input('what is your name')
