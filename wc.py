#!/usr/bin/python
import sys

def get_length(filename, options):
    fp = open(filename)
    lengths = get_length_pointer(fp)
    fp.close()
    if options:
        tmp_lengths = lengths
        lengths = []
        if "l" in options:
            lengths.append(tmp_lengths[0])
        if "m" in options:
            lengths.append(tmp_lengths[1])
        if "c" in options:
            lengths.append(tmp_lengths[2])
    return lengths

def get_length_pointer(fp):
    word_length = char_length = line_length = 0
    for line in fp:
        char_length += len(line)
        word_length += len(line.split())
        line_length += 1
    return line_length, word_length, char_length

def join_to_eight(strings):
    stri = ""
    for x in strings:
        length = len(x)
        if length < 8:
            stri += "{0}{1}".format(" " * (8 - length), x)
        else:
            stri += " {0}".format(x)
    return stri

if __name__ == "__main__":
    argc = len(sys.argv)
    if argc > 1:
        if argc == 2:
            filename = sys.argv[1]
            options = False
        else:
            options = sys.argv[1][1:]
            filename = sys.argv[2]
        lengths = map(lambda x: str(x), get_length(filename, options))
        print("{0} {1}".format(join_to_eight(lengths), filename))
    else:
        print("Please give a filename.")
