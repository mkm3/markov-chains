"""Generate Markov text from text files."""

import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path)
    text = contents.read()
    contents.close()

    return text

# open_and_read_file('green-eggs.txt')


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """
    
    # contents = open_and_read_file('green-eggs.txt')

    chains = {}

    words = text_string.split()

    words.append(None)

    # for i in range(len(words) - 1):
    #     print(words[i], words[i + 1])

    for idx in range(len(words) - 2):
        
        key = (words[idx], words[idx + 1])
        value = words[idx + 2]

    # for word in range(len(words) - 1):
    #     chains[words[word], words[word + 1]] = chains[words[word], words[word + 2]]

        if key not in chains:
            chains[key] = []

        chains[key].append(value)


    # for item, value in chains:
    #     print(f'{item}:{value}')

    return chains

# print(make_chains('green-eggs.txt'))


def make_text(chains):
    """Return text from chains."""

    key = choice(list(chains.keys()))
    words = [key[0], key[1]]
    word = choice(chains[key])

    while word is not None:
        key = (key[1], word)
        words.append(word)
        word = choice(chains[key])

        # your code goes here
    return " ".join(words)



input_path = sys.argv[0]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
