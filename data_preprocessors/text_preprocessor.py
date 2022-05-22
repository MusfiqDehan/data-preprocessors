"""
A module for preprocessing textfiles
"""
from collections import Counter
from bnlp import NLTKTokenizer
import pandas as pd
import random
import re
import csv
import os
import fileinput
import glob
import nltk

# Checking punkt downloaded or not
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    print("punkt not found. downloading...")
    nltk.download('punkt')


# ======================================
# Creating corpus on given format
# ======================================
def build_parallel_corpus(src_file="", tgt_file="", separator="|||", src_tgt_file=""):
    """
    Build parallel corpus of two languages.
    """
    src_list = text2list(myfile_path=src_file)

    tgt_list = text2list(myfile_path=tgt_file)

    merge_list = zip(src_list, tgt_list)

    # Changing format of Bangla and English Data
    # chr(92) = '\'
    # chr(10) = '\n'
    src_tgt_list = [
        f"{src_line.rstrip('chr(10)')} {separator} {tgt_line.rstrip('chr(10)')}"
        for src_line, tgt_line in merge_list
    ]

    # Converting list into text file
    list2text(mylist=src_tgt_list, myfile_path=src_tgt_file)


# ======================================
# Separating corpus on given format
# ======================================
def separate_parallel_corpus(src_tgt_file="", separator="|||", src_file="", tgt_file=""):
    """
    Separate parallel corpus of two languages.
    """
    mylist = text2list(
        myfile_path=src_tgt_file,
    )

    for line in mylist:
        src_line, tgt_line = line.split(separator)
        with open(src_file, "a") as src_data:
            src_data.write(src_line + "\n")
        with open(tgt_file, "a") as tgt_data:
            tgt_data.write(tgt_line + "\n")


# ======================================
# Convert excel file into multiple text files
# ======================================
def excel2multitext(excel_file_path="",
                    column_names=None,
                    src_file="",
                    tgt_file="",
                    aligns_file="",
                    separator="|||",
                    src_tgt_file="",
                    ):
    """
    This function convert excel file into multiple text files
    """
    if column_names is None:
        column_names = []

    df = pd.read_excel(excel_file_path, header=None, names=column_names)
    # df.to_csv(src_file, sep="\n", header=False, index=False)

    src_list = list(df[column_names[0]])
    tgt_list = list(df[column_names[1]])
    aligns_list = list(df[column_names[2]])

    list2text(mylist=src_list, myfile_path=src_file)
    list2text(mylist=tgt_list, myfile_path=tgt_file)
    list2text(mylist=aligns_list, myfile_path=aligns_file)

    build_parallel_corpus(
        src_file=src_file,
        tgt_file=tgt_file,
        separator=separator,
        src_tgt_file=src_tgt_file
    )


# ======================================
# Convert to lower case
# ======================================
def convert2lower(sentence):
    return sentence.lower()


# ======================================
# Convert to upper case
# ======================================
def convert2upper(sentence):
    return sentence.upper()


# ======================================
# Decontracting words
# ======================================
def decontracting_words(sentence):
    # Decontracting words
    # https://en.wikipedia.org/wiki/Wikipedia%3aList_of_English_contractions
    # https://stackoverflow.com/a/19794953
    contractions = {
        "ain't": "am not",
        "aren't": "are not",
        "can't": "can not",
        "can't've": "can not have",
        "'cause": "because",
        "could've": "could have",
        "couldn't": "could not",
        "couldn't've": "could not have",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hadn't've": "had not have",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'd've": "he would have",
        "he'll": "he will",
        "he'll've": "he will have",
        "he's": "he is",
        "how'd": "how did",
        "how'd'y": "how do you",
        "how'll": "how will",
        "how's": "how is",
        "i'd": "i would",
        "i'd've": "i would have",
        "i'll": "i will",
        "i'll've": "i will have",
        "i'm": "i am",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'd've": "it would have",
        "it'll": "it will",
        "it'll've": "it will have",
        "it's": "it is",
        "let's": "let us",
        "ma'am": "madam",
        "mayn't": "may not",
        "might've": "might have",
        "mightn't": "might not",
        "mightn't've": "might not have",
        "must've": "must have",
        "mustn't": "must not",
        "mustn't've": "must not have",
        "needn't": "need not",
        "needn't've": "need not have",
        "o'clock": "of the clock",
        "oughtn't": "ought not",
        "oughtn't've": "ought not have",
        "shan't": "shall not",
        "sha'n't": "shall not",
        "shan't've": "shall not have",
        "she'd": "she would",
        "she'd've": "she would have",
        "she'll": "she will",
        "she'll've": "she will have",
        "she's": "she is",
        "should've": "should have",
        "shouldn't": "should not",
        "shouldn't've": "should not have",
        "so've": "so have",
        "so's": "so as",
        "that'd": "that would",
        "that'd've": "that would have",
        "that's": "that is",
        "there'd": "there would",
        "there'd've": "there would have",
        "there's": "there is",
        "they'd": "they would",
        "they'd've": "they would have",
        "they'll": "they will",
        "they'll've": "they will have",
        "they're": "they are",
        "they've": "they have",
        "to've": "to have",
        "wasn't": "was not",
        "we'd": "we would",
        "we'd've": "we would have",
        "we'll": "we will",
        "we'll've": "we will have",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what'll've": "what will have",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "when's": "when is",
        "when've": "when have",
        "where'd": "where did",
        "where's": "where is",
        "where've": "where have",
        "who'll": "who will",
        "who'll've": "who will have",
        "who's": "who is",
        "who've": "who have",
        "why's": "why is",
        "why've": "why have",
        "will've": "will have",
        "won't": "will not",
        "won't've": "will not have",
        "would've": "would have",
        "wouldn't": "would not",
        "wouldn't've": "would not have",
        "y'all": "you all",
        "y'all'd": "you all would",
        "y'all'd've": "you all would have",
        "y'all're": "you all are",
        "y'all've": "you all have",
        "you'd": "you would",
        "you'd've": "you would have",
        "you'll": "you will",
        "you'll've": "you will have",
        "you're": "you are",
        "you've": "you have"
    }

    sentence_decontracted = []

    for word in sentence.split():
        if word in contractions:
            word = contractions[word]

        sentence_decontracted.append(word)

    sentence = ' '.join(sentence_decontracted)
    sentence = sentence.replace("'ve", " have")
    sentence = sentence.replace("n't", " not")
    sentence = sentence.replace("'re", " are")
    sentence = sentence.replace("'ll", " will")
    sentence = sentence.replace("'d", " would")
    sentence = sentence.replace("'s", " is")
    sentence = sentence.replace("'m", " am")

    return sentence


# ======================================
# Remove a file
# ======================================
def remove_file(file_path=""):
    try:
        os.remove(file_path)
    except OSError:
        pass


# ======================================
# Convert a text file into a dataframe
# ======================================
def text2df(myfile_path="", mydataframe=pd.DataFrame()) -> pd.DataFrame:
    with open(myfile_path, "r") as myfile:
        mydataframe = pd.read_csv(myfile_path, sep="\n", header=None)
    return mydataframe


# ======================================
# Split English Paragraph
# ======================================
def split_paragraph_file(file_path="", modified_file_path=""):
    """
    This function split a English paragraph into sentences
    """
    with open(file_path, "r") as fp:
        data = fp.read()
        mylist = nltk.tokenize.sent_tokenize(data)

    # Converting list to text file
    with open(modified_file_path, "w") as new_file:
        for listitem in mylist:
            new_file.write("%s\n" % listitem)


# ======================================
# Split English Sentence
# ======================================
def split_paragraph(paragraph=""):
    """
    This function split a English Paragraph into sentences
    """
    sent_tokens = nltk.tokenize.sent_tokenize(paragraph)
    return sent_tokens


# ======================================
# Split English Sentence
# ======================================
def split_sentence(sentence):
    """
    This function split a English Sentence into words
    """
    word_tokens = nltk.tokenize.word_tokenize(sentence)
    return word_tokens


# ======================================
# Split Bangla Paragraph
# ======================================
def split_bangla_paragraph_file(file_path="", modified_file_path=""):
    """
    This function split a English paragraph into sentences
    """
    with open(file_path, "r") as fp:
        data = fp.read()
        bnltk = NLTKTokenizer()
        mylist = bnltk.sentence_tokenize(data)

    # Converting list to text file
    with open(modified_file_path, "w") as new_file:
        for listitem in mylist:
            new_file.write("%s\n" % listitem)


# ======================================
# Split Bangla Paragraph
# ======================================
def split_bangla_paragraph(paragraph=""):
    """
    This function split a English Paragraph into sentences
    """
    bnltk = NLTKTokenizer()
    sent_tokens = bnltk.sentence_tokenize(paragraph)
    return sent_tokens


# ======================================
# Split Bangla Sentence
# ======================================
def split_bangla_sentence(sentence):
    """
    This function split a Bangla Sentence into words
    """
    bnltk = NLTKTokenizer()
    word_tokens = bnltk.word_tokenize(sentence)
    return word_tokens


# =====================================================
# Copying desired lines from a text file and storing in a new text file
# =====================================================
def separate_lines(
    old_file_path="", new_file_path="", start_line=0, end_line=0
):
    """
    Copying desired lines from a text file and storing in a new text file
    """
    # Converting text file to list
    with open(old_file_path, "r") as old_file:
        old_data = [line.rstrip("\n") for line in old_file.readlines()]

        # Separating desired lines from list
        new_data = old_data[start_line:end_line]

    # Converting list to text file
    with open(new_file_path, "w") as new_file:
        for listitem in new_data:
            new_file.write("%s\n" % listitem)


# ===================================
# Count no of lines in a text file
# ===================================
def count_lines(file_path=""):
    """
    Count total no of lines in a text file
    """
    with open(file_path, "r") as fp:
        for count, line in enumerate(fp):
            pass
    return count + 1


# ========================================
# Count total words in a sentence
# ========================================
def count_words(sentence):
    """
    Count total words in a sentence
    """
    return len(sentence.split())


def count_bangla_words(sentence):
    """
    Count total Bangla words in a Bangla sentence
    """
    return len(split_bangla_sentence(sentence))


# ========================================
# Count total unique words in a sentence
# ========================================
def count_unique_words(sentence: str) -> int:
    """
    Count total unique words in a sentence
    """
    unique_count = 0
    for letter, count in Counter(sentence.split()).items():
        if count == 1:
            unique_count += 1

    return unique_count


# ========================================
# Count total characters in a sentence
# ========================================
def count_chars(sentence):
    """
    Count total characters in a sentence
    """
    return len(sentence)


# =====================================================
# Split a text file into train, validation and test set
# =====================================================
def split_textfile(
    main_file_path: str = "",
    train_file_path: str = "",
    val_file_path: str = "",
    test_file_path: str = "",
    train_size: float = 0.8,
    val_size: float = 0.1,
    test_size: float = 0.1,
    shuffle: bool = False,
    seed: int = 42,
):
    """
    Split a text file into train, validation and test set
    """
    start_line = 0
    total_line = count_lines(file_path=main_file_path)

    train_start_line = start_line
    train_end_line = int((total_line * train_size) + train_start_line)

    val_start_line = train_end_line
    val_end_line = int((total_line * val_size) + val_start_line)

    test_start_line = val_end_line
    test_end_line = int((total_line * test_size) + test_start_line)

    # Converting text file to list
    with open(main_file_path, "r") as main_file:
        main_data = [line.rstrip("\n") for line in main_file.readlines()]

        # Separating desired lines from list
        train_data = main_data[train_start_line: train_end_line]
        val_data = main_data[val_start_line: val_end_line]
        test_data = main_data[test_start_line: test_end_line]

        # Shuffling data
        if shuffle == True:
            random.seed(seed)
            random.shuffle(train_data)
            random.shuffle(val_data)
            random.shuffle(test_data)

    # Converting list to text file
    with open(train_file_path, "w") as train_file:
        for listitem in train_data:
            train_file.write("%s\n" % listitem)

    with open(val_file_path, "w") as val_file:
        for listitem in val_data:
            val_file.write("%s\n" % listitem)

    with open(test_file_path, "w") as test_file:
        for listitem in test_data:
            test_file.write("%s\n" % listitem)

    print("Total lines: ", len(main_data))
    print("Train set size: ", len(train_data))
    print("Validation set size: ", len(val_data))
    print("Test set size: ", len(test_data))


# =================================================
# Add a space before and after a punctuation mark
# =================================================
def space_punc(line):
    """
    Add a space before and after a punctuation mark
    and remove more than one space
    print(space_punc('bla. bla? "bla"bla.bla! bla...'))
    >> bla . bla ? " bla " bla . bla ! bla . . .
    """

    line = re.sub('([.,:;\-।!?"()])', r" \1 ", line)
    line = re.sub("\s{2,}", " ", line)
    return line


# ======================
# Remove punctuation
# ======================
def remove_punc(line):
    # initializing punctuations string
    punc = """!()-[]{}।;:'"\,<>./?@#$%^&*_~"""

    for letter in line:
        if letter in punc:
            line = line.replace(letter, "")

    line = re.sub("\s{2,}", " ", line)

    return line


# ======================
# Return Punctuation
# ======================
def return_punc(line):

    # initializing punctuations string
    punc = """!()-[]{}।;:'"\,<>./?@#$%^&*_~"""

    line = list(line)
    Dictionary = {}
    seq = []  # list of all indices with any punctuation

    for i, p in enumerate(line):
        if p in punc:
            seq.append(i)
            if p in Dictionary:
                Dictionary[p].append(i)
            else:
                Dictionary[p] = [i]

    line = list(filter(lambda x: x not in punc, line))

    for i in seq:
        for key, indices in Dictionary.items():
            if i in indices:
                line.insert(i, key)
                indices.remove(i)

    return "".join(line)


def remove_and_return_punc(line):
    print(remove_punc(line))
    print(return_punc(line))


def with_and_remove_punc(line):
    print(return_punc(line))
    print(remove_punc(line))


# =================================
# Convert a text file into a list
# =================================
def text2list(myfile_path=""):
    with open(myfile_path, "r") as myfile:
        mylist = [line.rstrip("\n") for line in myfile.readlines()]
    return mylist


# =================================
# Convert a text file into a csv file
# =================================
def text2csv(text_file_path="", csv_file_path=""):
    """
    Convert a text file into a csv file
    """
    # Converting text file to list
    with open(text_file_path, "r") as myfile:
        mylist = [line.rstrip("\n") for line in myfile.readlines()]

    # Converting list to csv file
    with open(csv_file_path, "w") as mycsv:
        writer = csv.writer(mycsv)
        writer.writerows(mylist)


def text2csv_with_header(text_file_path="", csv_file_path=""):
    """
    Convert a text file into a csv file with header/column names
    """
    # Converting text file to list
    with open(text_file_path, "r") as myfile:
        mylist = [line.rstrip("\n") for line in myfile.readlines()]

    # Converting list to csv file
    with open(csv_file_path, "w") as mycsv:
        writer = csv.writer(mycsv)
        writer.writerow(["bn", "en"])
        writer.writerows(mylist)


def text2csv_with_header2(text_file_path="", csv_file_path="", delimeter='\n', header=None):
    if header is None:
        header = []

    # reading given csv file
    # and creating dataframe

    mytext = pd.read_csv(text_file_path, sep=delimeter, header=None)

    # adding column headings
    mytext.columns = header

    # store dataframe into csv file
    mytext.to_csv(csv_file_path, index=None)


# =================================
# Convert a list into a text file
# =================================
def list2text(mylist=None, myfile_path=""):
    if mylist is None:
        mylist = []

    with open(myfile_path, "w") as myfile:
        for item in mylist:
            myfile.write(item + "\n")


# =============================
# Shuffle a text file's lines
# =============================
def shuffle_lines(old_file="", shuffled_file="", seed=0):
    """
    Shuffle a text file's lines
    """
    # Reading lines from text file
    with open(old_file, "r") as old_file:
        lines = old_file.readlines()

    # Shuffling lines
    random.seed(seed)
    random.shuffle(lines)

    # Writing lines to text file
    with open(shuffled_file, "w") as shuffled_file:
        for line in lines:
            shuffled_file.write(line)


# ========================================
# Merge multiple text files into one
# ========================================
def merge_textfiles(folder_path="", combined_file_path=""):
    """
    Merge multiple text files into one
    """
    # List of files to be merged
    file_list = os.listdir(folder_path)

    # Merging files
    with open(combined_file_path, "w") as combined_file:
        for file in file_list:
            with open(folder_path + file, "r") as myfile:
                combined_file.write(myfile.read())


# ========================================
# Empty Function
# ========================================
def empty_function(no_args):
    pass


# =========================================
# Apply a function in whole text file
# =========================================
def apply_whole(
    function_name, myfile_path="", modified_file_path=""
):
    mylist = text2list(myfile_path=myfile_path)

    # mylist = [function_name(item) for item in mylist]
    newlist = list(map(function_name, mylist))

    list2text(mylist=newlist, myfile_path=modified_file_path)
