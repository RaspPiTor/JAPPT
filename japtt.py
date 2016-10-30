import cmd, readline
import logger
logger=logger.Logger()
class JapptShell(cmd.Cmd):
    intro=logger.colour('''
     _   _    ____ _____ _____ 
    | | / \  |  _ \_   _|_   _|
 _  | |/ _ \ | |_) || |   | |  
| |_| / ___ \|  __/ | |   | |  
 \___/_/   \_\_|    |_|   |_|
 Just Another Pen Testing Tool
 
 ''', colour=31, bold=1)
    intro+=logger.colour('Welcome to JAPTT. Type help or ? to list commands.\n',
                         colour=32, bold=1)
    prompt=logger.colour('(japtt)', 32, bold=1)+logger.colour('>>>', 34, bold=1)
    file=None
    ruler=logger.colour('=', colour=32, bold=1)
    def emptyline(self):
        pass
    def default(self, line):
        logger.error('Unknown syntax: '+line)
    def do_print(self, args):
        print(args)
    def do_quit(self, args):
        'Exit from the Jappt shell'
        logger.info('Exiting')
        exit()
    def do_EOF(self, args):
        logger.info('Exiting')
        exit()
if __name__ == '__main__':
    try:
        JapptShell().cmdloop()
    except KeyboardInterrupt:
        logger.info('Exiting')
