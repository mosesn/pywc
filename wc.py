#!/usr/bin/python
import sys
from math import log10

def get_length_filename(filename, options):
    fp = open(filename)
    lengths = get_length(fp, options)
    fp.close()
    return lengths

def get_length(fp, options):
    word_length = char_length = line_length = 0
    for line in fp:
        char_length += len(line)
        word_length += len(line.split())
        line_length += 1
    return filter_by_options((line_length, word_length, char_length), options)

def filter_by_options(lengths, options):
    if options:
        ret_lengths = []
        for pos, option in enumerate(options):
            if option:
                ret_lengths.append(lengths[pos])
    return ret_lengths

def join_to_eight(numbers):
    stri = ""
    for number in numbers:
        length = int(log10(number)) + 1
        if length < 8:
            stri += "{0}{1}".format(" " * (8 - length), number)
        else:
            stri += " {0}".format(number)
    return stri

def parse_options(options):
    ret_options = []
    for letter in options[1:]:
        if letter == "c":
            ret_options.append(2)
        elif letter == "w":
            ret_options.append(1)
        elif letter == "l":
            ret_options.append(0)
        else:
            raise ValueError("Illegal argument '{0}'.".format(letter))
    return ret_options

def parse_args(options):
    filenames = []

    ret_options = [False, False, False]
    start = True
    for pos, arg in enumerate(options):
        if start and (arg.startswith("-") and len(arg) > 1):
            or_list = parse_options(arg)
            for pos in or_list:
                ret_options[pos] |= True
        elif not start:
            filenames.append(arg)
        else:
            start = False
            filenames.append(arg)
    return validate(ret_options), filenames

def validate(options):
    if options[0] or options[1] or options[2]:
        return options
    else:
        return [True, True, True]

def stringify(lengths, filename):
    return "{0} {1}".format(join_to_eight(lengths), filename)

if __name__ == "__main__":
    options, filenames = parse_args(sys.argv[1:])
    if filenames:
        for filename in filenames:
            try:
                lengths = get_length_filename(filename, options)
                print(stringify(lengths, filename))
            except IOError as err:
                print err
    else:
        lengths = get_length(sys.stdin, options)
        print(stringify(lengths, ""))
