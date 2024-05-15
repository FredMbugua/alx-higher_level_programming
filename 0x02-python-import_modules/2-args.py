#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    num = len(argv)
    argc = len(argv) - 1
    if argc == 0:
        print('{} arguments'.format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, argv[1]))
    elif argc > 1:
        print('{} arguments'.format(argc))
        for i in range(1, num):
            print('{}: {}'.format(i, argv[i]))
