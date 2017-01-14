import sys

def sort(arr, dst_splitter, mode):
    arr.sort()

    if mode == 'reverse':
        arr.reverse()

    output(arr, dst_splitter)


def load(filepath, src_splitter, dst_splitter, mode):
    file = open(filepath, 'r')
    data = file.read()
    arr  = data.split(src_splitter)
    check_num(arr, dst_splitter, mode)


def check_num(arr, dst_splitter, mode):
    isnum = True

    for i, n in enumerate(arr):
        try:
            arr[i] = int(n)
        except:
            print('ERROR: ' + '{0:15s}'.format(repr(arr[i])) + ' is not a number.')
            isnum = False

    if isnum == False:
        exit()

    sort(arr, dst_splitter, mode)


def check_arg(params):
    # if reverse option exists
    if '-r' in params:
        mode = 'reverse'
        params.remove('-r')
    elif '--reverse' in params:
        mode = 'reverse'
        params.remove('--reverse')
    else:
        mode = 'normal'

    # check arguments
    if len(params) == 4:
        filepath     = params[1]
        src_splitter = params[2]
        dst_splitter = params[3]
    elif len(params) == 3:
        filepath     = params[1]
        src_splitter = params[2]
        dst_splitter = ', '
    elif len(params) == 2:
        filepath     = params[1]
        src_splitter = ','
        dst_splitter = ', '
    else:
        print('Invaild command line arguments')
        exit()

    # load file
    load(filepath, src_splitter, dst_splitter, mode)


def output(arr, dst_splitter):
    for i, num in enumerate(arr):
        if not i == (len(arr) - 1):
            # output with splitter
            print(num, end = dst_splitter)
        else:
            # for last output
            print(num)


def main():
    params = sys.argv
    check_arg(params)
main()
