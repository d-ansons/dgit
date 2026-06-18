import argparse
import os

from . import data

def main():
    args = parse_args()
    args.func(args)

def parse_args():
    parser = argparse.ArgumentParser()

    commands = parser.add_subparsers(dest='command')
    commands.required = True # dgit requires arguments

    init_parser = commands.add_parser('init')
    init_parser.set_defaults(func=init)
    init_parser.add_argument('path', nargs='?', default='.') # ? makes argument optional.

    return parser.parse_args()

def init(args):
    data.init()
    print(f'Initialised empty dgit repository in {os.getcwd()}/{data.GIT_DIR}')