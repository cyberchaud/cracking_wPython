# Cracking Codes with Python
# Chapter 08
# Example 1

# Transposition encryption

import logging
import sys
import getopt
import math

logging.basicConfig(filename='chap08expl01.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of question')

def main(argv):

    key = 0
    message = ''
    
    try:
        logging.debug('Trying to get args')
        opts, args = getopt.getopt(argv, "hk:c:", ["key_length=", "ciphertext="])
    except getopt.GetoptError:
        logging.debug('Invalid arguments')
        print('chap08expl01.py -k <key_length> -c <ciphertext>')
        logging.debug('Ending.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            logging.debug('Help argument was passed.  Displaying help')
            print('chap08expl01.py -k <key_length> -c <ciphertext>')
            logging.debug('Ending.')
            sys.exit()
        elif opt in ("-k", "--key_length"):
            key = int(arg)
        elif opt in ("-c", "--ciphertext"):
            message = arg

    #print(key, message)
    plaintext = decryptMessage(key, message)
    logging.debug('The ciphertext create is: {}'.format(message))
    print('The plaintext is: {}|'.format(plaintext))

def decryptMessage(key, message):

    logging.debug('The key is {}.  The message is {}.'.format(key, message))

    numOfColumns = int(math.ceil(len(message) / float(key)))
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    plaintext = [''] * numOfColumns
    
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)

if __name__ == "__main__":
    main(sys.argv[1:])
