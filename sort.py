import sys

def sort(arr, dst_splitter):
    arr = sorted(arr)
    for i, num in enumerate(arr):
        if not i == (len(arr) - 1):
            print(num, end = dst_splitter)
        else:
            print(num)

def check_num(arr, dst_splitter):
    isnum = True
    for i, n in enumerate(arr):
        try:
            arr[i] = int(n)
        except:
            print('ERROR: ' + '{0:15s}'.format(repr(arr[i])) + ' is not a number.')
            isnum = False
    if isnum == False:
        exit()
    sort(arr, dst_splitter)

def load(filepath, src_splitter, dst_splitter):
    file = open(filepath, 'r')
    data = file.read()
    arr  = data.split(src_splitter)
    check_num(arr, dst_splitter)

def check_arg(params):
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
    load(filepath, src_splitter, dst_splitter)

def main():
    params = sys.argv
    check_arg(params)
main()
