from itertools import chain, cycle
from processor import encrypt, decrypt, Keys

if __name__ == '__main__':
    while True:
        key_to_use = Keys(input('Enter the key to use for this session: '))
        if len(key_to_use.getvalue()) < 8:
            print('Please enter a key with at least eight characters!')
        else:
            break

    to_copy = input('Auto Copy Encrypted Text to Clipboard? (Y/N): ').lower()
    if 'n' in to_copy:
        print('Encrypted Messages will NOT be automatically copied to the clipboard!')
        to_copy = False
    else:
        print('Encrypted Messages will be automatically copied to the clipboard!')
        to_copy = True

    while True:
        msg = input('$: ')
        msg = list(chain(*zip(msg.split(), cycle(' '))))[:-1]

        if msg[0].lower() == 'encrypt':
            to_encrypt = ''.join(msg[1:]).strip()
            print('Encrypting: ', to_encrypt)
            print(f'Encrypted Msg is: {encrypt(to_encrypt, key_to_use)}')

        elif msg[0].lower() == 'decrypt':
            to_decrypt = ''.join(msg[1:]).strip()
            print('Decrypting: ', to_decrypt)
            print(f'Decrypted Msg is: {decrypt(to_decrypt, key_to_use)}')

        elif msg[0].lower() == 'key':
            key = ''.join(msg[1:]).strip()
            if len(key) >= 8:
                if 'y' in input(f'The Key for this session will be changed to: {key}. Continue? (Y/N): ').lower():
                    key_to_use = Keys(key)
                    print('The Key is changed!')
            else:
                print('Please Use a Key with at least 8 characters.')
