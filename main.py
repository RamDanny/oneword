import ui
from tinydb import TinyDB, Query
from crypt import encrypt, decrypt, randpass, shahash
from format import tobyte, tostr


# global vars
PASSPHRASE = ''

def main():
    pin = input('Passphrase? ')
    # login
    if verify(pin):
        # generate new passphrase
        PASSPHRASE = randpass()
        # update passphrase in db
        db = TinyDB('pass.json')
        db.clear_cache()
        doc = db.update({'hash': shahash(PASSPHRASE)}, doc_ids=[1])
        print(f'Your new passphrase is {PASSPHRASE}')
        print('NOTE:     Remember your password very carefully')
        print('\t  The passphrase is newly generated for security purposes')
        print('\t  Don\'t forget your passphrase! You could get locked out!')
        print('\t  Note it down and store it in a physically safe location\n')
        # launch ui
        ui.uigen(pin)
        print(f'\nDon\'t forget, Your new passphrase is {PASSPHRASE}')
        print('Remember to save your password very carefully')
    else:
        print('Invalid password!\nTerminating...')

# verifies the user passphrase
def verify(pin):
    db = TinyDB('pass.json')
    db.clear_cache()
    doc = db.get(doc_id=1)
    if shahash(pin) == doc['hash']:
        return True
    else:
        return False


if __name__ == '__main__':
    main()