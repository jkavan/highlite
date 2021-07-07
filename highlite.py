#!/usr/bin/env python

import sys
import getopt
import re
from termcolor import colored

#
# You can freely customize the colors and/or styles if you like (though
# the changes may be overwritten by the upgrade process).
#
# Available colors:
#   fore      back
#   ----      ----
#   grey      on_grey
#   red       on_red
#   green     on_green
#   yellow    on_yellow
#   blue      on_blue
#   magenta   on_magenta
#   cyan      on_cyan
#   white     on_white
#
# Available styles:
#   bold
#   dark
#   underline
#   blink
#   reverse
#   concealed

colors = [
    ["green", ""],
    ["red", ""],
    ["yellow", ""],
    ["blue", ""],
    ["magenta", ""],
    ["white", ""],
    ["cyan", ""],
    ["grey", "on_white"],
    ["blue", "on_white"],
    ["yellow", "on_white"],
    ["white", "on_red"],
    ["white", "on_yellow"],
    ["white", "on_blue"],
    ["white", "on_magenta"],
]

styles = ["bold", "underline"]

# Search is case-sensitive by default. Can be overriden with `-i`
ignore_case = False

# ---

USAGE = ("An utility for highlighting command line output using one or more regular expressions.\n"
         "\n"
         "Usage: [COMMAND] | hl [OPTION] REGEX...\n"
         "\n"
         "OPTIONS:\n"
         "  -h, --help         Print this help message\n"
         "  -v, --version      Print version information\n"
         "  -i, --ignore-case  Ignore case when searching\n"
        )

VERSION = "highlite version 0.1.0"

def get_fore_color(index):
    """ Returns a foreground color from the list """
    index = index % (len(colors))
    color = colors[index][0]
    if color == '':
        return None
    return color

def get_back_color(index):
    """ Returns a background color from the list """
    index = index % (len(colors))
    color = colors[index][1]
    if color == '':
        return None
    return color

def colorize(text, regexes, ignore_case):
    """
    Surrounds regex matches with ANSI colors and returns the colored text

    :param text: Text that will be colorized.
    :param regexes: A list of search terms (in regexp format). Which text matches to colorize.
    :return: Colorized text.
    """
    flags = re.IGNORECASE if ignore_case else 0
    # Loop through each argument (regex)
    for index, regex in enumerate(regexes):
        # Add color around the matches
        text = re.sub(regex,
                      lambda m: colored(
                          '{}'.format(m.group()),
                          get_fore_color(index),
                          get_back_color(index),
                          styles),
                      text,
                      flags=flags)
    return text

def validate_regex(regexes):
    """ Checks if the given regex(es) are valid. """
    try:
        for regex in regexes:
            re.compile(regex)
    except re.error:
        print("Invalid regex pattern: " + regex)
        sys.exit(1)

def parse_args(args):
    """
    Parses command line arguments and sets global options

    :returns: operands (list of regexes)
    """
    global ignore_case
    try:
        options, arguments = getopt.getopt(
            args,
            'vhi',
            ["version", "help", "ignore-case"])
        for o, a in options:
            if o in ("-v", "--version"):
                print(VERSION)
                sys.exit()
            if o in ("-h", "--help"):
                print(VERSION)
                print(USAGE)
                sys.exit()
            if o in ("-i", "--ignore-case"):
                ignore_case = True
        if not arguments:
            print(USAGE)
            sys.exit(1)
        # save regexes (operands) to a list
        operands = [str(arg) for arg in arguments]
    except (getopt.GetoptError, ValueError) as e:
        print("Error: " + e.msg)
        print(USAGE)
        sys.exit(1)
    return operands

def main():
    """ Main function """
    regexes = parse_args(sys.argv[1:])
    global ignore_case
    try:
        # Use command line arguments as regexes
        validate_regex(regexes)
        # Tell Python to ignore the line if it contains invalid Unicode data
        sys.stdin.reconfigure(errors='ignore')
        # Read lines from stdin
        for line in sys.stdin:
            line = colorize(line.rstrip(), regexes, ignore_case)
            sys.stdout.write(line + '\n')
    # Catch Ctrl+C and exit cleanly
    except KeyboardInterrupt:
        sys.stdout.flush()

if __name__ == "__main__":
    main()
