#!/usr/bin/python

import sys, getopt

def main(argv):
    inputFile = ''
    outputFile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["iFile=", "oFile="])
    except getopt.GetoptError:
        print('CommandLineArguments.py -i <inputFile> -o <outputFile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('CommandLineArguments.py -i <inputFile> -o <outputFile>')
            sys.exit()
        elif opt in ("-i", "-iFile"):
            inputFile = arg
        elif opt in ("-o", "-oFile"):
            outputFile = arg
    print("InputFile is : %s " % inputFile)
    print(("OutputFile is : %s " % outputFile))

if __name__ == '__main__':
    main(sys.argv[1:])