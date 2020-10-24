# Cracking Codes with Python
# Chapter 01
# Practice Set 01

# Rot(x) challenges

import logging
import sys
import getopt

logging.basicConfig(filename='chap01ques03.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of question')

def main(argv):
    pText = ''
    cText = ''
    cRot = 0

    try:
        logging.debug('Trying to get args')
        opts, args = getopt.getopt(argv, "hp:c:", ["plaintext=", "ciphertext="])
    except getopt.GetoptError:
        logging.debug('Invalid arguments')
        print('c01q01.py -p <plaintext> -c <ciphertext>')
        logging.debug('Ending.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            logging.debug('Help argument was passed.  Displaying help')
            print('c01q03.py -p <plaintext> -c <ciphertext>')
            logging.debug('Ending.')
            sys.exit()
        elif opt in ("-p", "--plaintext="):
            pText = arg
        elif opt in ("-c", "--ciphertext"):
            cText = arg

    logging.debug('Finding difference plain text {} and cipher text {}'.format(pText, cText))
    print('The plain text is: ', pText)
    print('The cipher text is: ', cText)
    print('The rotation shift is: ', delta(pText, cText))


def encrypt(text, rotation):
    result = ''
    for i in text:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) + rotation - 65) % 26 + 65)
            else:
                result += chr((ord(i) + rotation - 97) % 26 + 97)
        else:
            result += chr((ord(i)))
    return result


def delta(text, cipher):
    result = 0
    print(ord(cipher[0]) - 65) % 26 + 65
    print(ord(text[0]) - 65) % 26 + 65
    result = (ord(cipher[0]) - 65) % 26 - (ord(text[0]) - 65) % 26
    return str(abs(result))


if __name__ == "__main__":
    main(sys.argv[1:])