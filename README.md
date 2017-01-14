# ctfpack
CTF, short for Capture The Flag, is a computer security competition. This repository provides some tools to solve the CTF problems easily.

## ROT
The extension for ROT13. ROT solves Caesar cipher by shifting some characters.

### usage

```
$ python rot.py <mode> <string> <placement>

<mode>:      Set encode or decode. If omitting, the mode becomes encode.
<string>:    Set the string you'd like to encode / decode.
<placement>: Set the number how many places you'd like to rotate the string.
```

Encode: rotating by 3 places:

```bash
$ python rot.py hello 3
khoor
```

Decode: rotating back by 3 places:

```bash
$ python rot.py decode khoor 3
hello
```

## sort
Sorting and output the result by any format.

### usage
```
$ python sort.py <filepath> <source splitter> <destination splitter>

<filepath>:             Set the filepath.
<source splitter>:      Set the splitter. e.g. If numetic string is '1 2 3 4 5', then splitter is ' '. If omitting, the source splitter becomes ','.
<destination splitter>: Set the splitter. e.g. If splitter is ',', then output is '1,2,3,4,5'. If omitting, the destination splitter becomes ', '.

option
-r, --reverse
        reverse sorting
```

sort.txt:

```
15,1,93,52,66,31,87,0,42,77,46,24,99,10,19,36,27,4,58,76,2,81,50,102,33,94,20,14,80,82,49,41,12,143,121,7,111,100,60,55,108,34,150,103,109,130,25,54,57,159,136,110,3,167,119,72,18,151,105,171,160,144,85,201,193,188,190,146,210,211,63,207
```

To sort numeric string:

```bash
$ python sort.py sort.txt
0, 1, 2, 3, 4, 7, 10, 12, 14, 15, 18, 19, 20, 24, 25, 27, 31, 33, 34, 36, 41, 42, 46, 49, 50, 52, 54, 55, 57, 58, 60, 63, 66, 72, 76, 77, 80, 81, 82, 85, 87, 93, 94, 99, 100, 102, 103, 105, 108, 109, 110, 111, 119, 121, 130, 136, 143, 144, 146, 150, 151, 159, 160, 167, 171, 188, 190, 193, 201, 207, 210, 211
```

You can assign the output format like this:

```
$ python sort.py sort.txt ',' ' '
0 1 2 3 4 7 10 12 14 15 18 19 20 24 25 27 31 33 34 36 41 42 46 49 50 52 54 55 57 58 60 63 66 72 76 77 80 81 82 85 87 93 94 99 100 102 103 105 108 109 110 111 119 121 130 136 143 144 146 150 151 159 160 167 171 188 190 193 201 207 210 211
```

Reverse:

```
$ python sort.py -r sort.txt ',' ' '
211 210 207 201 193 190 188 171 167 160 159 151 150 146 144 143 136 130 121 119 111 110 109 108 105 103 102 100 99 94 93 87 85 82 81 80 77 76 72 66 63 60 58 57 55 54 52 50 49 46 42 41 36 34 33 31 27 25 24 20 19 18 15 14 12 10 7 4 3 2 1 0
```
