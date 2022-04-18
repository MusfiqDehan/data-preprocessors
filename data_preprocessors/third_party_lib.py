import nltk
import spacy
from flair.data import Sentence
from flair.models import SequenceTagger
from deep_translator import GoogleTranslator
from textblob import TextBlob


# =================================
# converting words into pos tags
# =================================
def words_to_tags(sentence):
    sentence = nltk.tokenize.word_tokenize(sentence)
    tagged_sentence = nltk.pos_tag(sentence)
    tags = [tag for word, tag in tagged_sentence]
    tags_str = ' '.join([str(tag) for tag in tags])
    return tags_str


def get_correct_spelling(sentence: str) -> str:
    '''
    Get correct spelling of a sentence.\n
    At first install dependencies \n
    `!pip install -U textblob`
    '''
    correct_spelling = TextBlob(sentence).correct()
    return correct_spelling


# ========================================
# Get Words Tags Dictionary
# ========================================
def get_nltk_postag_dict(target=""):
    ''' Get nltk pos tags '''
    target_tokenized = nltk.tokenize.word_tokenize(target)
    nltk_postag_dict = dict((key, value)
                            for key, value in nltk.pos_tag(target_tokenized))
    return nltk_postag_dict


def get_spacy_postag_dict(target=""):
    ''' Get spacy pos tags '''
    nlp = spacy.load("en_core_web_sm")
    target_tokenized = nlp(target)
    spacy_postag_dict = dict((token.text, token.tag_)
                             for token in target_tokenized)
    return spacy_postag_dict


def get_flair_postag_dict(target=""):
    ''' Get flair pos tags '''
    tagger = SequenceTagger.load("pos")
    target_tokenized = Sentence(target)
    tagger.predict(target_tokenized)
    flair_postag_dict = dict((token.text, token.tag)
                             for token in target_tokenized)
    return flair_postag_dict


# ========================
# Translate a sentence
# ========================
def deep_translation(sentence, source="bn", target="en"):
    """
    Translate a sentence from one language to another using Google Translator.\n
    At first install dependencies \n
    `!pip install -U deep-translator`

    """
    translator = GoogleTranslator()
    translated_sentence = translator.translate(
        sentence, source=source, target=target)
    return translated_sentence
