def what(q):
    if q[0] == 'game':
        if q[1] == 'run':
            if q[2] == '1':
                print('Starting game...')
            elif q[2] == '0':
                print('Stopping game...')
        elif q[1] == 'reload':
            print('Reload game...')
    elif q[0] == 'spam':
        for i in range(q[1]):
            print('SPAAAAAAAAAAM')

while 1:
    q = input('Cmd: ')
    w = q.split()
    if len(w) == 3:
        what(w)
    else:
        print('dddd'
        )