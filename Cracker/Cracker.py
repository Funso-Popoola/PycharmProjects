import os
import time


class Cracker():

    def __init__(self):

        os.chdir(".")
        self.string_option = []
        self.givenText = self.get_given_string()
        self.letters = self.split_text(self.givenText)
        print self.letters
        self.word_len = self.get_num_of_holes_to_fill()
        start = time.time()
        self.correct_words = self.open_dict()
        self.possible_words = self.permute(self.letters, self.letters,
                                self.word_len)
        print(self.possible_words)
        print("")
        print(time.time() - start)
        print(self.get_solution(self.possible_words))
        print(time.time() - start)

    def get_given_string(self):
        givenText = raw_input("Enter the alphabet options :")
        return givenText

    def get_num_of_holes_to_fill(self):
        num = raw_input("How many spaces are there to fill?:")
        num = int(num)
        return num

    def permute(self, parent_array, letter_array, space):
        if (space == 1):
            return letter_array
        else:

            final_array = list()
            for letter in letter_array:
                my_parent = list(parent_array)
                sub_final_array = list()
                for each in letter:
                    my_parent.remove(each)
                for item in my_parent:
                    sub_str = letter + item
                    sub_final_array.append(sub_str)
                final_array += (sub_final_array)
            return self.permute(parent_array, final_array, space - 1)

    def open_dict(self):
        try:
            dict_file = open("dict.txt", 'r')
            feed = list()
            for line in dict_file:
                temp = (line.strip("\n"))
                for letter in self.letters:
                    if(temp.startswith(letter)):
                        feed.append(temp.strip("'s").lower())
                        break
            return feed
        except IOError, e:
            print "File opening operation failed", e
        finally:
            dict_file.close()

    def is_word_in_dict(self, word):
        is_present = False
        val = None
        try:
            val = self.correct_words.index(word.lower())
        except ValueError as e:
            #print(e)
            val = -1
        finally:
            if (val >= 0):
                is_present = True
        return is_present

    def get_solution(self, word_array):
        final_solution = list()
        for word in word_array:
            if(self.is_word_in_dict(word)):
                if(final_solution.count(word) == 0):
                    print word + "\n"
                    final_solution.append(word)
        return final_solution

    def file_exists(self, path):
        status = False
        if(os.path.isfile(path)):
            if(os.path.exists(path)):
                status = True
        return status

    def split_text(self, text):
        alpha = []
        if(text is not None):
            text.lower()
            for each in text:
                for single_char in each:
                    alpha.append(single_char)
        return alpha


def crack():
    Cracker()


crack()




