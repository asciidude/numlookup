import sys

def get_input():
    txt = ''

    for word in sys.argv[1:]:
        txt += f'{word} '
    
    return txt

in_arr = get_input().split(' ')

if __name__ == '__main__':
    if in_arr[0] == 'lookup':
        if not in_arr[1]:
            print('Unable to lookup null number')
            sys.exit(-1)
        
    elif in_arr[0] == 'credits':
        print('Created by pxpcandy! https://www.twitch.tv/pxpcandy')
    
    else:
        print('Sorry, that command does not exist')