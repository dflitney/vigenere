# Cypher


Utility to en/de-code text using the Vigenere cypher.

## The Vigenere Cypher

This is not a cryptographically strong cypher. At its heart
it is simply an extension of the Caesar substitution
cypher, several simple attacks exist, but it is simple to
implement, analyse and fun to play with.

The Caesar cypher replaces each letter in the original text with a
corresponding letter from a rotated alphabet. As such it is trivially
attacked via simple frequency analysis. Assuming the original text is english
then the most frequent letter in the encrypted text corresponds to "E" in
the original text. Once you know the translation of one letter you have cracked
the code.

The Vigenere cypher improves upon this by selecting each letter from a set
of rotated alphabets. This means that the same letter can be substituted
with a different letter at different points in the text. This obfuscates
the frequency relationship making it harder to crack.

### Example

A shared key word/phrase is used to select substitution alphabets from
the list of possible rotated alphabets. In this example our key
word is "MYPASSWORD" and the message text is "THIS IS MY SECRET TEXT".

The first letter, "T", is replaced with the coresponding
letter, 'E', from the alphabet starting with the first key
letter, "M",...

```python
alphabet['A'] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alphabet['B'] = "BCDEFGHIJKLMNOPQRSTUVWXYZ A"
alphabet['C'] = "CDEFGHIJKLMNOPQRSTUVWXYZ AB"
...
alphabet['M'] = "MNOPQRSTUVWXYZ ABCDEFGHIJKL"
                                    ^
```

...and the next plain text letter "H" is taken from the alphabet
starting with "Y", i.e. it is replaced with "E", and so on.

```python
alphabet['A'] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
alphabet['Y'] = "YZ ABCDEFGHIJKLMNOPQRATUVWX"
                        ^
```

Eventually we run out of letters in our key phrase at which
point we cycle back to the beginning.

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

