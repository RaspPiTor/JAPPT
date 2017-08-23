import argparse
import random
import shlex
def randomdata():
    chars='abcdefghijklmnopqrstuvwxyz0123456789'
    chars+=chars.upper()
    length=random.randint(5, 20)
    choice=random.choice
    return ''.join(choice(chars) for i in range(length))
def bashiencode(args):
    ignore='>/dev/null 2>&1'
    for i in '; & && | ||'.split():
        a=random.choice([' ', ''])+i+random.choice([' ', ''])
        now='{}{}{}'.format(ignore, a, args.code)
        if i=='&&':
            now=args.expected+now
        elif i=='||':
            now=randomdata()+now
        yield now
def ciencode(args):
    if type(args)!=list:
        args=shlex.split(str(args))
    parser=argparse.ArgumentParser()
    parser.add_argument('code')
    parser.add_argument('-l', '--language', default='bash')
    parser.add_argument('-e', '--expected', default='',
        help='Expected input, used to make program run sucessfully')
    try:
        args=parser.parse_args(args)
    except SystemExit:
        return
    if args.language=='bash':
        print('\n'.join(bashiencode(args)))
