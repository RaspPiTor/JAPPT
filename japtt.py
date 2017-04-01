import cmd

from XSS.xssencode import xssencode
from CI.ciencode import ciencode

import logger

LOGGER = logger.Logger()


class JapptShell(cmd.Cmd):
    intro = LOGGER.colour(r'''
     _   _    ____ _____ _____
    | | / \  |  _ \_   _|_   _|
 _  | |/ _ \ | |_) || |   | |
| |_| / ___ \|  __/ | |   | |
 \___/_/   \_\_|    |_|   |_|
 Just Another Pen Testing Tool

 ''', colour=31, bold=1)
    intro += LOGGER.colour('Welcome to JAPTT. Type help or ? to list commands.\n',
                           colour=32, bold=1)
    prompt = LOGGER.colour('(japtt)', 32, bold=1) + LOGGER.colour('>>>', 34, bold=1)
    file = None
    ruler = LOGGER.colour('=', colour=32, bold=1)

    def emptyline(self):
        pass

    def default(self, line):
        LOGGER.error('Unknown syntax: '+line)

    def do_print(self, args):
        print(args)

    def do_quit(self, _):
        'Exit from the Jappt shell'
        LOGGER.info('Exiting')
        exit()

    def do_EOF(self, _):
        LOGGER.info('Exiting')
        exit()

    def do_xssencode(self, args):
        'Put inputted javascript into a tag which could cause Cross Site Scripting'
        print('\n'.join(xssencode(args)))

    def do_ciencode(self, args):
        'Encode given command into injectable form for different languages'
        print('\n'.join(ciencode(args)))
if __name__ == '__main__':
    try:
        JapptShell().cmdloop()
    except KeyboardInterrupt:
        LOGGER.info('Exiting')
