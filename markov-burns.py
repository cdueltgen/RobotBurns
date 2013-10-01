#!/usr/bin/env python

import sys
from random import randint

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    chains_dict = {}
    words = corpus.split()
    for word in range(len(words)-2):
        tuple_key = words[word], words[word+1]
        # the following line is rad and replaces an if:else. Look it up.
        chains_dict.setdefault(tuple_key,[]).append(words[word+2])
    # print chains_dict
    return chains_dict

def start_keys(chains):
    start_line = []
    for key in chains:
        if key[0].istitle():
            start_line.append(key)
    return start_line

def make_stanza(key, chains):
    stanza = [key[0], key[1]]
    while True:
        next_list = chains[key]
        next = next_list[randint(0,len(next_list)-1)]
        stanza.append(next)
        if next.endswith((".","!")) == True:
            return stanza
        key = (key[1], next)

def format_stanza(stanza):
    lines = []
    line = []
    for i in stanza:
        line.append(i)
        if i.endswith((",",";","?","--",":")) == True and stanza[stanza.index(i)+1].islower() == False:
            lines.append(" ".join(line))
            line = []
    lines.append(" ".join(line))
    for i in lines:
        print i

def make_text(chains, num_stanzas):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    start_lines = start_keys(chains)

    for i in range(num_stanzas):
        key = start_lines[randint(0,len(start_lines)-1)]
        stanza = make_stanza(key, chains)
        format_stanza(stanza)
        print

    return "--Robot Burns"

def main():
    args = sys.argv

    # Change this to read input_text from a file
    f = open("burns-poems-and-songs.txt")
    input_text = f.read()
    num_stanzas = int(args[1])

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict, num_stanzas)
    print random_text

if __name__ == "__main__":
    main()
