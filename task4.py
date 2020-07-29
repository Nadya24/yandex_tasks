import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--upper', action="store_true")
parser.add_argument('--lines', nargs="?")
parser.add_argument('input', nargs="?")
parser.add_argument('output', nargs="?")

args = parser.parse_args()

input_file = args.input
output_file = args.output

if args.upper:
    res = ''
    with open(input_file, 'r') as f:
        res = f.read()
    res1 = res.upper()
    with open(input_file, 'w') as f:
        f.write(res1)


if args.lines:
    n = int(args.lines)
    res = ''
    with open(input_file, 'r') as f:
        res = f.readlines()
    with open(output_file, 'w') as f:
        f.writelines(res[:n])

if not args.upper and not args.lines:
    res = ''
    with open(input_file, 'r') as f:
        res = f.readlines()
    with open(output_file, 'w') as f:
        f.writelines(res)
