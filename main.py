import sys
from itertools import chain, cycle
import webbrowser
from time import sleep

try:
    from processor import encrypt, decrypt
except ImportError:
    print('Module processor not found! Is the file processor.py in the same folder as main.py?')
    sleep(5)
    sys.exit()

try:
    from pyperclip import copy
    found = True
except ImportError:
    print('Module pyperclip not found! Auto Copy to Clipboard will be unavailable.')
    copy = None

if __name__ == '__main__':
    while True:
        key_to_use = input('Enter the key to use for this session: ')
        if len(key_to_use) < 8:
            print('Please enter a key with at least eight characters!')
        elif '1234567890' in key_to_use:
            print('Please do not use numbers! You can use special characters.')
        else:
            break

    if copy is not None:
        to_copy = input('Auto Copy Encrypted Text to Clipboard? (Y/N): ').lower()
        if 'n' in to_copy:
            print('Encrypted Messages will NOT be automatically copied to the clipboard!')
            to_copy = False
        else:
            print('Encrypted Messages will be automatically copied to the clipboard!')
            to_copy = True
    else:
        to_copy = False

    while True:
        print('\n')
        msg = input('$: ')
        msg = list(chain(*zip(msg.split(), cycle(' '))))[:-1]

        if msg[0].lower() == 'encrypt':
            to_encrypt = ''.join(msg[1:]).strip()
            print('Encrypting: ', to_encrypt)
            encrypted_message = encrypt(to_encrypt, key_to_use)
            print(f'Encrypted Msg is: {encrypted_message}')
            if to_copy:
                print('Copied To Clipboard!')
                copy(encrypted_message)

        elif msg[0].lower() == 'decrypt':
            to_decrypt = ''.join(msg[1:]).strip()
            print('Decrypting: ', to_decrypt)
            decrypted_message = decrypt(to_decrypt, key_to_use)
            print(f'Decrypted Msg is: {decrypted_message}')

        elif msg[0].lower() == 'key':
            key = ''.join(msg[1:]).strip()
            if len(key) >= 8 and '1234567890' not in key:
                if 'y' in input(f'The Key for this session will be changed to: {key}. Continue? (Y/N): ').lower():
                    key_to_use = key
                    print('The Key is changed!')
            else:
                print('Please Use a Key with at least 8 characters, and do not use numbers.')

        elif msg[0].lower() == 'clipboard' or msg[0].lower() == 'copy':
            if copy is not None:
                if to_copy:
                    if 'y' in input('Currently Your Encrypted Messages are being copied to the clipboard. Turn this '
                                    'off? (Y/N): ').lower():
                        to_copy = False
                        print('Auto Copy Turned Off!')
                    else:
                        print("Auto Copy is still On")
                else:
                    if 'y' in input('Currently Your Encrypted Messages are not being copied to the clipboard. Turn '
                                    'this on? (Y/N): ').lower():
                        to_copy = True
                        print('Auto Copy Turned On!')
                    else:
                        print('Auto Copy is still Off')
            else:
                print('The Module pyperclip was not found. Clipboard functions are unavailable. '
                      'Use "pip install pyperclip" to install it.')

        elif msg[0].lower() == 'help':
            webbrowser.open('README.md')

        elif msg[0].lower() == 'exit' or msg[0].lower() == 'close':
            if 'y' in input('Do You Want to Close the Program? (Y/N): ').lower():
                sys.exit()

        else:
            print(f'Command "{msg[0]}" Not Found! Please check the spelling again, or read the readme for more info.')
