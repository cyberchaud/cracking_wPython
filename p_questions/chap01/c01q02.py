# Cracking Codes with Python
# Chapter 01
# Practice Set 01

# Rot(x) challenges

import logging
import sys
import getopt

logging.basicConfig(filename='chap01ques02.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of question')

def main(argv):
    cText = ''
    cRot = 0

    try:
        logging.debug('Trying to get args')
        opts, args = getopt.getopt(argv, "hc:s:", ["ciphertext=", "shifts="])
    except getopt.GetoptError:
        logging.debug('Invalid arguments')
        print('c01q01.py -c <ciphertext> -s <number of shifts>')
        logging.debug('Ending.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            logging.debug('Help argument was passed.  Displaying help')
            print('c01q01.py -c <ciphertext> -r <number of shifts>')
            logging.debug('Ending.')
            sys.exit()
        elif opt in ("-c", "--ciphertext="):
            cText = arg
        elif opt in ("-s", "--shifts"):
            cRot = int(arg)

    logging.debug('Decoding cipher text {} and rotating {} times'.format(cText, cRot))
    print('The cipher text is: ', cText)
    print('The shifts is: ', cRot)
    print('The ciphertext is: ', decrypt(cText, cRot))


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

def decrypt(text, rotation):
    result = ''
    for i in text:
        if i.isalpha():
            if i.isupper():
                result += chr((ord(i) - rotation - 65) % 26 + 65)
            else:
                result += chr((ord(i) - rotation - 97) % 26 + 97)
        else:
            result += chr((ord(i)))
    return result

if __name__ == "__main__":
    main(sys.argv[1:])