import cmd, sys, readline
class Shell(cmd.Cmd):
    intro='''
     _   _    ____ _____ _____ 
    | | / \  |  _ \_   _|_   _|
 _  | |/ _ \ | |_) || |   | |  
| |_| / ___ \|  __/ | |   | |  
 \___/_/   \_\_|    |_|   |_|  
Welcome to JAPTT. Type help or ? to list commands.\n'''
    prompt='(japtt)'
    file=None
    def do_print(self, args):
        print(args)
    def do_quit(self, args):
        exit()
    def do_EOF(self, args):
        exit()
if __name__ == '__main__':
    Shell().cmdloop()
