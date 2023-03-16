### Contains the user interface


from tinydb import TinyDB, Query
from shutil import get_terminal_size
from crypt import encrypt, decrypt
from format import tobyte, tostr

# global vars
TERMINAL_WIDTH = get_terminal_size().columns

# displays ui
def uigen(PASSPHRASE):
    # initialising database
    db = TinyDB('pwords.json')
    db.clear_cache()
    # main menu
    printer('[ONEWORD]')
    printer('')
    while True:
        printer('Main Menu:')
        printer('(1) Retrieve Passwords')
        printer('(2) Add Password')
        printer('(3) Edit Password')
        printer('(4) Remove Password')
        printer('(q) Quit')
        printer('')
        printer('Operation? ', end='', left=True)
        choice = input()
        printer('\n')
        # retrieve passwords
        if choice == '1':
            printer('RETRIEVE PASSWORDS')
            if len(db.all()) == 0:
                printer('No passwords saved. Add some first.')
                printer('\n')
            else:
                printer('Name given to password ?(/ to display all passwords) ', end='', left=True)
                pnamein = input()
                if pnamein == '/':
                    for pw in db:
                        printer(f'({pw.doc_id}) {pw["name"]} {decrypt(PASSPHRASE, pw["name"], tobyte(pw["iv"], raw=True), tobyte(pw["value"], raw=True))}')
                else:
                    pw = db.search(Query()['name'] == pnamein)
                    printer(f'({pw[0].doc_id}) {pw[0]["name"]} {decrypt(PASSPHRASE, pw[0]["name"], tobyte(pw[0]["iv"], raw=True), tobyte(pw[0]["value"], raw=True))}')
                printer('\n')
        # add password
        elif choice == '2':
            printer('ADD PASSWORD')
            printer('Name? ', end='', left=True)
            pname = input()
            printer('Password? ', end='', left=True)
            pword = input()
            # encrypt password
            ciphertext = encrypt(PASSPHRASE, pname, pword)
            # insert into db
            db.insert({'name': pname, 'iv': tostr(ciphertext[0], raw=True), 'value': tostr(ciphertext[1], raw=True)})
            printer('\n')
            printer('Inserted!')
            printer('\n')
        # edit password
        elif choice == '3':
            printer('EDIT PASSWORD')
            printer('Password number? ', end='', left=True)
            did = input()
            if db.contains(doc_id=int(did)):
                temp = db.get(doc_id=int(did))
                printer('New name? ', end='', left=True)
                pname = input()
                printer('New password? ', end='', left=True)
                pword = input()
                # encrypt password
                ciphertext = encrypt(PASSPHRASE, pname, pword)
                # insert into db
                temp = {'name': pname, 'iv': tostr(ciphertext[0], raw=True), 'value': tostr(ciphertext[1], raw=True)}
                db.update(temp, doc_ids=[int(did)])
                printer('\n')
                printer('Edited!')
            else:
                printer('\n')
                printer('No such password exists!')
            printer('\n')
        # Remove password
        elif choice == '4':
            printer('REMOVE PASSWORD')
            printer('Password number(s)? ', end='', left=True)
            dids = list(map(int, input().split()))
            printer('\n')
            for did in dids:
                if db.contains(doc_id=int(did)):
                    db.remove(doc_ids=[did])
                    printer(f'Removed password number ({did})!')
            printer('\n')
        # Quit app
        elif choice == 'q' or choice == 'Q':
            break

# pads the string to fit terminal width
def printer(string, width=TERMINAL_WIDTH, percent=50, left=False, end='\n'):
    rem = width - len(string)
    if not left:
        print(((rem * percent) // 100)*' ' + string + ((rem * percent) // 100)*' ', end=end)
    else:
        print(((rem * percent) // 100)*' ' + string, end=end)

if __name__ == '__main__':
    uigen('secret-pass-phrase')
