# Cracking Codes with Python
# Chapter 07
# Example 1

# Transposition encryption

import logging
import sys
import getopt

logging.basicConfig(filename='chap07expl01.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of question')

def main(argv):

    key = 0
    message = ''
    
    try:
        logging.debug('Trying to get args')
        opts, args = getopt.getopt(argv, "hk:m:", ["key_length=", "message="])
    except getopt.GetoptError:
        logging.debug('Invalid arguments')
        print('c07e01.py -k <key_length> -m <message>')
        logging.debug('Ending.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            logging.debug('Help argument was passed.  Displaying help')
            print('c07e01.py -k <key_length> -m <message>')
            logging.debug('Ending.')
            sys.exit()
        elif opt in ("-k", "--key_length"):
            key = int(arg)
        elif opt in ("-m", "--message"):
            message = arg

    #print(key, message)
    ciphertext = encryptMessage(key, message)
    logging.debug('The ciphertext create is: {}'.format(ciphertext))
    print('The ciphertext is: {}|'.format(ciphertext))

def encryptMessage(key, message):
    ciphertext = [''] * key
    logging.debug('The key is {}.  The message is {}.'.format(key, message))

    for column in range(key):
        currentIndex = column
        #print(column)
        while currentIndex < len(message):
            ciphertext[column] += message[currentIndex]
            currentIndex += key
    
    return ''.join(ciphertext)

if __name__ == "__main__":
    main(sys.argv[1:])
