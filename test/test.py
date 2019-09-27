from argument.argument import Argument
from argument.argument_parser import ArgumentParser
from argument.command import Command


@Argument
def simple():
    print('simple')


@Argument(help='1 arg')
def simple_with_arg(arg):
    print('this is your arg %s' % arg)


@Argument
def simple_with_2_args(arg1, arg2):
    print('those are your args: %s %s' % (arg1, arg2))


@Command
def command():
    print('this is a command')


@Command(help='1 arg')
def command_with_arg(arg, arg1=None):
    print('this the command arg: %s, arg1: %s' % (arg, arg1))


class ClassCommand(object):
    @staticmethod
    @Argument
    def argument_in_class():
        print('argument_in_class')

    @staticmethod
    @Command
    def command_in_class(arg=None):
        print('command_in_class. arg %s' % arg)


parser = ArgumentParser()
parser.parse_args()
