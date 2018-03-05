# Cypher

A Framework for Implementing Cyphers

<dl>
    <dt>Caesar Cypher - Not yet implemented!</dt>
    <dd>
        The Caesar cypher replaces each letter in the original text with a
        corresponding letter from a rotated alphabet. As such plain text letters
        will always translate to the same encrypted letter. This is trivially
        attacked via simple frequency analysis; assuming the original text is english
        then the most frequent letter in the encrypted text corresponds to "E" in
        the original text. Once you know the translation of one letter you have cracked
        the code.
    </dd>

    <dt>Vigenere Cypher</dt>
    <dd>
        While the Caesar cypher only uses a single substitute alphabet, the Vigenere
        cypher improves upon this by sequentially selecting from a list
        of rotated alphabets. This <i>polyalphabetic</i> substitution allows the same
        letter to be substituted with a different letter in the
        encripted text thus obfuscating the letter frequency relationship.

        This is still not a very strong cypher. At its heart
        it is simply an extension of the Caesar substitution
        cypher, several simple attacks exist, but it is easy to
        implement, analyse and fun to play with.
    </dd>
</dl>

## Implementation details

### Vigenere

A shared key word/phrase is used to select substitution alphabets from
the list of possible rotated alphabets. In this example our key
word is "MYPASSWORD" and the message text is "THIS IS MY SECRET TEXT".

The first letter, 'T', is replaced with the coresponding
letter, 'E', from the alphabet rotated to start with the first key
letter 'M'.

```python
alphabet['A'] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alphabet['B'] = "BCDEFGHIJKLMNOPQRSTUVWXYZ A"
alphabet['C'] = "CDEFGHIJKLMNOPQRSTUVWXYZ AB"
...
alphabet['M'] = "MNOPQRSTUVWXYZ ABCDEFGHIJKL"
                                    ^
```

The next plain text letter, 'H', is substituted from the alphabet
starting with 'Y', i.e. it is replaced with 'E', and so on.

```python
alphabet['A'] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alphabet['Y'] = "YZ ABCDEFGHIJKLMNOPQRATUVWX"
                        ^
```

We continue encrypting letters against alphabets selected from
the key phrase. Eventually, when we run out of letters in our key
phrase, we cycle back to the beginning.

## Cryptographic attack

There are a number of weakness in the Vigenere cypher:

1. The repeating key means it is possible to search the encrypted text
looking for sequence repeats which give us a clue to the length of the key.

1. Assuming we know, or can guess, the language of the original text then, knowing the
key length allows us to apply frequency analysis once more. The
cipher text can now be treated as N interleaved Caesar cyphers and each can be attacked independently.


## Usage

### Commandline options

```shell
$ python cypher.py --help
usage: cypher.py [-h] [--key KEY] [--encrypt] [--decrypt] [--verbose]
                 [--plain-text-file PLAIN_TEXT_FILE]

Encrypt/decrypt messages using Vigenere cypher method.

optional arguments:
  -h, --help            show this help message and exit
  --key KEY, -k KEY     The Vigenere cypher key.
  --encrypt, -E         Encrypt message
  --decrypt, -D         Decrypt message
  --verbose, -V         Additional output - handy for debugging!
  --plain-text-file PLAIN_TEXT_FILE, -p PLAIN_TEXT_FILE
                        Path to a file containing the plain text message.
```

### Encrypt a message

```shell
python cypher.py --key=MYPASSWORD -E
Enter your message text: THIS IS MY SECRET TEXT
EEXSR NNCALPTCIWONJHIQ
```

### Decrypt a message

```shell
python cypher.py --key=MYPASSWORD -D
Enter your message text: EEXSR NNCALPTCIWONJHIQ
THIS IS MY SECRET TEXT
```

### API

```python
from cypher.substitution import Vigenere
```

```python
class Vigenere:

    def __init__(self):
        """ Create a table of all the possible rotated alphabets """

    def encrypt(self, plain_text, key_word):
        """ Encrypt plain text with the given key word """

    def decrypt(self, cypher_text, key_word):
        """ Decrypt the cypher text using the key word """
```
