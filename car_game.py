help_menu = '''
start - to start the car
stop - to stop the car
quit - to exit
'''
started = False

while True:
    options = input('> ').lower()
    if options == 'help':
        print(help_menu)
    elif options == 'start':
        if started:
            print('car already started!')
        else:
            print('Car started...Ready to go!')
            started = True
    elif options == 'stop':
        if not started:
            print('car already stopped!')
        else:
            print('Car stopped.')
            started = False
    elif options == 'quit':
        break
    else:
        print("I don't understand that...")
