import sys

def rot(char, num):
    if   'a' <= char <= 'z':
        return chr((ord(char) - ord('a') + int(num)) % 26 + ord('a'))
    elif 'A' <= char <= 'Z':
        return chr((ord(char) - ord('A') + int(num)) % 26 + ord('A'))
    else:
        return char


def output(string, num):
    result = (rot(char, num) for char in string)
    result = ''.join(result)
    print(result)


def check(params):
    # check arguments
    if len(params) == 3:
        string = params[1]
        num    = params[2]
    elif len(params) == 4:
        mode   = params[1]
        string = params[2]
        num    = params[3]
    else:
        print('Invaild command line arguments')
        exit()

    # check rotation number
    try:
        num = int(num)
    except:
        print('A rotation number must be an integer')
        exit()

    # check mode
    if len(params) == 4:
        if mode == 'encode':
            num = num
        elif mode == 'decode':
            num = -num
        else:
            print('A mode must be encode or decode')
            print('If omitting, a mode is encode')
            exit()

    # call output if all params is OK
    output(string, num)


def main():
    params = sys.argv
    check(params)
main()
