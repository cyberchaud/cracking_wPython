# Cracking Codes with Python
# Chapter 06
# Practice Set 01

# Caesar cracking

import logging
import sys
import getopt

logging.basicConfig(filename='chap01ques02.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of question')

def main(argv):
    file_path = ''

    try:
        logging.debug('Trying to get args')
        opts, args = getopt.getopt(argv, "hf:", ["filepath="])
    except getopt.GetoptError:
        logging.debug('Invalid arguments')
        print('c06q01.py -f <file_path')
        logging.debug('Ending.')
        sys.exit(2)

    for opt, arg in opts:
        if opt == "-h":
            logging.debug('Help argument was passed.  Displaying help')
            print('c01q01.py -f <file_path>')
            logging.debug('Ending.')
            sys.exit()
        elif opt in ("-f", "--filepath"):
            file_path = arg

    logging.debug('Trying to open: {}'.format(file_path))
    #print('The file path is ', file_path)

    f = openFile(file_path)
    lines = f.readlines()
    
    for line in lines:
        if len(line) > 1:
            # print(line.strip())
            for x in range(0, 25):
                print(decrypt(line, x))                

    f.close()



def openFile(file):

    try:
        f = open(file, "r")
    except IOError as err:
        print('File path not found.')
        print(err)
        sys.exit(2)
    
    return f

def decrypt(text, rotation):
    result = ''
    for i in text:
        if i not in ['\'', '!', '?', '.']:
            if i.isalpha():
                if i.isupper():
                    result += chr((ord(i) + rotation - 65) % 26 + 65)
                elif i == ' ':
                    results += ' '
                else:
                    result += chr((ord(i) + rotation - 97) % 26 + 97)
            else:
                result += chr((ord(i)))
    return result

if __name__ == "__main__":
    main(sys.argv[1:])
