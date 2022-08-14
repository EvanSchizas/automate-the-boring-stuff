while True:
    print('Please type your name: ')
    name = input()
    if name == 'your name':
        break
print('Thank you.\n')
print ('Type exit to exit. \n')
exit_status = input()

if exit_status == 'exit':
    quit()