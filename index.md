## SuperCipher

This is a python based open source program which can be used to encrypt/decrypt messages based on a text key. None of your data leaves your computer, meaning that this software is completely secure

### Downloads 

[Download Setup.exe](https://github.com/MrAyushBajpai/SuperCipher/releases/download/v1.0/setup.exe)
[Download Setup.zip](https://github.com/MrAyushBajpai/SuperCipher/releases/download/v1.0/setup.zip)
[Download Source Code.zip](https://github.com/MrAyushBajpai/SuperCipher/archive/refs/tags/v1.0.zip)
[Download Source Code.tar.gz](https://github.com/MrAyushBajpai/SuperCipher/archive/refs/tags/v1.0.tar.gz)

### Installation
Download Setup.exe (or Download Setup.zip and extract the .exe) and follow on-screen instructions for installation. You can also build from sources.

### Execute From Sources
- [Download The Source Code.zip](https://github.com/MrAyushBajpai/SuperCipher/archive/refs/tags/v1.0.zip) or [Download The Source Code.tar.gz](https://github.com/MrAyushBajpai/SuperCipher/archive/refs/tags/v1.0.tar.gz) or clone the [Github Repository](https://github.com/MrAyushBajpai/SuperCipher)
- [Download and install Python 3](https://www.python.org/downloads/)
- [Install pyperclip Library](https://pypi.org/project/pyperclip/) with "pip install pyperclip" in terminal.
- In the sources, execute main.py. Use [pyinstaller](https://pypi.org/project/pyinstaller) if you want to convert the .py to .exe. You can also use other libraries/tools for conversion, but only pyinstaller is completely tested.

### Usage
- On Initial Startup, the program will ask you the key that you want to use for encryption/decryption for the session. This key can be changed at any time later during runtime of program as well.
- The Program will ask you if you want to autocopy the encrypted message to clipboard, so that each time you will encrypt a message, the message will be copied automatically to the clipboard. THIS PREFERENCE CANNOT BE CHANGED WITHOUT RESTARTING THE PROGRAM AS OF Iniital Release v1.0 BUT MIGHT BE IMPLEMENTED LATER.
- You Can Enter Multiple Commands after the $ Sign to do a task as follows:

#### Commands
1. **Encrypt:** Use "Encrypt" followed by the message to encrypt it using the key which you have defined earlier.
2. **Decrypt:** Use "Decrypt" followed by the message to decrypt it using the key which you have defined earlier. Using a key different from the one which was used in encryption will result in a faulty decryption.
3. **Key:** Use "Key" followed by the key to change the current key for the session. NOTE:- A Key must have 8 characters, and should NOT comprise of numeric digits.
4. **Exit/Close:** Use "Exit" or "Close" To Exit out of the program. 
