#! /usr/bin/env python3
import time
import sys
__isatty__=sys.stdout.isatty()
class Logger:
    def __init__(self, level=0, colour=True):
        self.usecolour=bool(colour)
        if level<1:
            self.level=0
        elif level<2:
            self.level=1
        elif level<3:
            self.level=2
        else:
            self.level=0
            self.error('Specified log level(%s) not in allowed levels [0, 1, 2]' % level)
            self.info('Log level 0 assumed')
    def colour(self, msg, colour=1, bold=False):
        msg=str(msg)
        if self.usecolour:
            if __isatty__:
                if 'idlelib' not in list(sys.modules):
                    addcolour= '\033[%s;%sm' % (int(bool(bold)), colour)
                    end='\x1b[0m'
                    msg=addcolour+msg.replace(end, addcolour)+end
        return msg
    def colourprint(self, msg, colour=1, bold=False):
        #sys.stdout and sys.stderr used for python2 and python3 compatability
        if colour==31:
            sys.stderr.write(self.colour(msg, colour=colour, bold=bold)+'\n')
        else:
            sys.stdout.write(self.colour(msg, colour=colour, bold=bold)+'\n')
    def info(self, msg):
        if self.level==0:
            msg=[time.strftime('[%H:%M:%S]'),
                 '[INFO]',
                 str(msg)]
            self.colourprint(' '.join(msg),32)
    def warning(self, msg):
        if self.level<2:
            msg=[time.strftime('[%H:%M:%S]'),
                 '[WARNING]',
                 str(msg)]
            self.colourprint(' '.join(msg),33)
    def error(self, msg):
        msg=[time.strftime('[%H:%M:%S]'),
             '[ERROR]',
             str(msg)]
        self.colourprint(' '.join(msg),31)

if __name__=='__main__':
    logger=Logger()
    print(logger.colour('this is an %s test' % logger.colour('amazing, %s and useful' % logger.colour('sucessful', colour=33, bold=1), colour=32)))
    logger.colourprint('Is a tty: %s' % __isatty__)
    logger.info('this is some infomation')
    logger.warning('this is a warning')
    logger.error('this is a critical error')
    sys.stderr.write('hi\n')
