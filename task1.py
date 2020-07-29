# Суперпарсер аргументов
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('arg', nargs='*')
args = parser.parse_args()
if len(args.arg) == 0:
    print("no args")
for i in args.arg:
    print(i)
