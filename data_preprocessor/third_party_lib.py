import nltk
from deep_translator import GoogleTranslator


# =================================
# converting words into pos tags
# =================================
def words_to_tags(sentence):
    sentence = nltk.tokenize.word_tokenize(sentence)
    tagged_sentence = nltk.pos_tag(sentence)
    tags = [tag for word, tag in tagged_sentence]
    tags_str = ' '.join([str(tag) for tag in tags])
    return tags_str


# ========================================
# Get Words Tags Dictionary
# ========================================
def get_en_word_tag_dict(target=""):
    tgt_token = nltk.tokenize.word_tokenize(target)
    en_word_tag_dict = dict((key, value)
                            for key, value in nltk.pos_tag(tgt_token))
    return en_word_tag_dict


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
