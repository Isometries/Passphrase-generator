import sys
from secrets import randbelow


class Password_generator:
    password = ''
    words = []
    filesize = 0

    def __init__(self, min, max):

        self.min = min
        self.max = max

        self.getSize()

    def getSize(self):

        for line in open('words.txt', 'rb'):
            self.filesize += 1

    def calcPassword(self):

        with open('words.txt', 'rb') as word_dict:
            lines = word_dict.readlines()
            pass_size = 0
            while pass_size < self.min:
                rand_line = randbelow(self.filesize)
                new_word = lines[rand_line].decode("utf-8")[:-1]

                if pass_size + len(new_word) > self.max:
                    pass
                else:
                    self.password += new_word
                    pass_size += len(new_word)
                    self.words.append(new_word)

        return self.words

    def printPassword(self):
        for word in self.words:
            print(word)


if __name__ == '__main__':
    min_len, max_len = int(sys.argv[1]), int(sys.argv[2])
    pw = Password_generator(min_len, max_len)
    pw.calcPassword()
    pw.printPassword()
