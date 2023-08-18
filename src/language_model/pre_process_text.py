import string
from nltk.corpus import stopwords

import enchant


class PreProcessText(object):
    def __init__(self):
        self.valid_words = enchant.Dict("en_US")

    def __remove_punctuation(self, text):
        """
        Takes a String
        return : Return a String
        """
        message = []
        for x in text:
            if x in string.punctuation:
                pass
            else:
                message.append(x)
        message = ''.join(message)

        return message

    def __remove_stopwords(self, text):
        """
        Takes a String
        return List
        """
        words = []
        for x in text.split():

            if x.lower() in stopwords.words('english'):
                pass
            else:
                words.append(x)
        return words

    def __check_if_english_word(self, text):
        """
        Takes a List
        return List
        """
        words = []
        for x in text:
            if self.valid_words.check(x):
                words.append(x)
        return words

    def token_words(self, text=''):
        """
        Takes String
        Return Token also called  list of words that is used to
        Train the Model
        """
        message = self.__remove_punctuation(text)
        words = self.__remove_stopwords(message)
        words = self.__check_if_english_word(words)
        return words
