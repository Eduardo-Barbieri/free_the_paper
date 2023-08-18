import nltk
from gensim.models import Word2Vec

from language_model.pre_process_text import PreProcessText

from utils.exceptions import WordsNotFoundError


def get_words(training_words: str):
    flag = nltk.download("stopwords")
    if (flag == "False" or not flag):
        raise WordsNotFoundError
    else:
        # Add download log
        helper = PreProcessText()
        return helper.token_words(text=training_words)


def init_model(words: str, target: str):
    model = Word2Vec(
                sentences=[words],
                vector_size=100,
                window=5,
                min_count=1,
                workers=4
            )
    vocabulary = model.wv
    closest_words = model.wv.most_similar(target)
    return vocabulary, closest_words
