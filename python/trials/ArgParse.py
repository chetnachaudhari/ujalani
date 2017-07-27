#!/usr/bin/python
import argparse

parser = argparse.ArgumentParser(description="Sample code to try argparser module")
parser.add_argument('-i', '--input', help="Input File Name", required =True)
parser.add_argument('-o', '--output', help="Output File Name", required=True)
args = parser.parse_args()

print("Input File = %s" % args.input)
print("Output File = %s" % args.output)
