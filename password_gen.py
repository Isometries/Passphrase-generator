# Produces random passphrase in English
# Copyright (C) 2018  Thunder Gabriel
# Email: tgabriel@protonmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


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
