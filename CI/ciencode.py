import argparse
import random
import shlex
import sys
parser=argparse.ArgumentParser()
parser.add_argument('code')
parser.add_argument('-l', '--language', default='bash')
def randomdata():
    chars='abcdefghijklmnopqrstuvwxyz0123456789'
    chars+=chars.upper()
    length=random.randint(5, 20)
    choice=random.choice
    return ''.join(choice(chars) for i in range(length))
def ciencode(args):
    if type(args)!=list:
        args=shlex.split(str(args))
    parser=argparse.ArgumentParser()
    parser.add_argument('code')
    parser.add_argument('-l', '--language', default='bash')
    args=parser.parse_args(args)
    if args.language=='bash':
        ignore='>/dev/null 2>&1'
        for i in '; & && | ||'.split():
            a=' '+i+random.choice([' ', ''])
            now=' {}{}{}'.format(ignore, a, args.code)
            if i=='&&':
                now=random.choice(['-h', '--help'])+now
            elif i=='||':
                now=randomdata()+now
            yield now
