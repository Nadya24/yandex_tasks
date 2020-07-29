import argparse

parser = argparse.ArgumentParser()

max_int = 100
min_int = 0
middle = 50

parser.add_argument('--barbie', nargs='?', const=50, default=50,
                    type=int, help='This will be option One')
parser.add_argument('--cars', nargs='?', const=50, default=50,
                    type=int, help='This will be option Two')
parser.add_argument('--movie', nargs='?', const='other',
                    default='other', type=str,
                    help='This will be option Three')


args = parser.parse_args()

dict_m = {
    'melodrama': 0, 'football': 100, 'other': 50
}


one = args.barbie
two = args.cars
three = dict_m.get(args.movie)
if not three:
    three = args.get('other')

if (one > max_int) or (one < min_int):
    one = middle

if ((two > max_int) or (two < min_int)):
    two = middle


boy = int((100 - one + two + three) / 3)
girl = 100 - boy
print("boy: ", boy)
print("girl: ", girl)
