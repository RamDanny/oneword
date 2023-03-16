# oneword
Bytesized Password Manager

Welcome to Oneword!

* This is a small project made to easily store and retrieve passwords locally

* The source code is written entirely in Python

* In addition to inbuilt Python libraries, the libraries used by the Python scripts are:
  1. Pycryptodomex -- For cryptography (https://www.pycryptodome.org/src/introduction)
  2. TinyDB -- For storage (https://tinydb.readthedocs.io/en/latest/index.html)
  3. All-escapes -- For representing binary esscapes in text (https://pypi.org/project/all-escapes/)

* The only thing to remember is to keep noting down the passphrase generated for every session. This is done for security reasons


# Installation

1. Download all the files in the repo
2. Open a CLI(Command Line Interface) or Terminal
3. Run the main.py file
4. In the case of running Oneword for the first time, use the passphrase: secret-pass-phrase
5. After finishing the current session, note down the new random passphrase generated (preferably on paper or a notepad). This is the passphrase to be used for logging in to the next session. The master passphrase changes each session to maintain security.
