import pandas as pd
import random
import re
import csv
import os
import fileinput
import glob


# ======================================
# Creating corpus on given format
# ======================================
def parallel_corpus_builder(src_file="", tgt_file="", separator="", src_tgt_file=""):
    """
    Build parallel corpus of two languages.
    """
    # Bangla File
    with open(src_file, "r") as src_data:
        src_list = [line.rstrip("\n") for line in src_data.readlines()]

    # English File
    with open(tgt_file, "r") as tgt_data:
        tgt_list = [line.rstrip("\n") for line in tgt_data.readlines()]

    # Merging Bangla and English Data
    merge_list = zip(src_list, tgt_list)

    separator = "|||"

    # Changing format of Bangla and English Data
    # chr(92) = '\'
    src_tgt_list = [
        f"{src_line.rstrip('chr(92)n')} {separator} {tgt_line.rstrip('chr(92)n')}"
        for src_line, tgt_line in merge_list
    ]

    # Converting list into text file
    with open(src_tgt_file, "w") as src_tgt:
        for item in src_tgt_list:
            src_tgt.write(item + "\n")


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
def text_file_to_dataframe(myfile_path="", mydataframe=pd.DataFrame()) -> pd.DataFrame:
    with open(myfile_path, "r") as myfile:
        mydataframe = pd.read_csv(myfile_path, sep="\n", header=None)
    return mydataframe


# ======================================
# Convert a text file into a list
# ======================================
def split_bangla_sentence(file_path=""):
    """
    This function split a bangla sentence into words
    """
    with open(file_path, "r") as fp:
        for line in fp:
            line = line.rstrip("\n")
            line = line.split(" ")
            for word in line:
                yield word


# ======================================
# Split Bangla and English Sentence
# ======================================
def split_bangla_paragraph(file_path=""):
    """
    This function split a bangla paragraph into sentences
    """
    with open(file_path, "r") as fp:
        for paragraph in fp:
            paragraph = paragraph.split("।")
            for line in paragraph:
                yield line


# =====================================================
# Copying desired lines from a text file and storing in a new text file
# =====================================================


def separate_lines_from_text_file(
    old_file_path="", new_file_path="", start_line=0, end_line=0
):
    """
    old_file_path = "Datasets/train/train-bn-en.txt"
    new_file_path = "Datasets/train/train-bn-en-50.txt"
    start_line = 0  # include
    end_line = 50   # exclude
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
def no_of_lines_in_text_file(file_path=""):
    """
    This function count no of lines in a text file
    path = "Datasets/train/train-bn-en.txt"
    """
    with open(file_path, "r") as fp:
        for count, line in enumerate(fp):
            pass
    return count + 1


# =================================================
# Add a space before and after a punctuation mark
# =================================================
def space_punc(line):
    """
    SPACE PUNC
    ----------
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
def text_file_to_list(myfile_path="", mylist=[]):
    with open(myfile_path, "r") as myfile:
        mylist = [line.rstrip("\n") for line in myfile.readlines()]
    return mylist


# =================================
# Convert a text file into a csv file
# =================================
def text_to_csv(text_file_path="", csv_file_path=""):
    """
    text_file_path = "Datasets/train/train-bn-en.txt"
    csv_file_path = "Datasets/train/train-bn-en.csv"
    """
    # Converting text file to list
    with open(text_file_path, "r") as myfile:
        mylist = [line.rstrip("\n") for line in myfile.readlines()]

    # Converting list to csv file
    with open(csv_file_path, "w") as mycsv:
        writer = csv.writer(mycsv)
        writer.writerows(mylist)


def text_to_csv_with_header(text_file_path="", csv_file_path=""):
    """
    text_file_path = "Datasets/train/train-bn-en.txt"
    csv_file_path = "Datasets/train/train-bn-en.csv"
    """
    # Converting text file to list
    with open(text_file_path, "r") as myfile:
        mylist = [line.rstrip("\n") for line in myfile.readlines()]

    # Converting list to csv file
    with open(csv_file_path, "w") as mycsv:
        writer = csv.writer(mycsv)
        writer.writerow(["bn", "en"])
        writer.writerows(mylist)


def text_to_csv_with_header2(text_file_path="", csv_file_path="", delimeter='\n', header=None):
    if header is None:
        header = []

    # reading given csv file
    # and creating dataframe
    mytext = pd.read_csv(text_file_path, delimiter=delimeter, header=None)

    # adding column headings
    mytext.columns = header

    # store dataframe into csv file
    mytext.to_csv(csv_file_path, index=None)


# =================================
# Convert a list into a text file
# =================================
def list_to_text_file(mylist=[], myfile_path=""):
    with open(myfile_path, "w") as myfile:
        for item in mylist:
            myfile.write(item + "\n")


# =============================
# Shuffle a text file's lines
# =============================
def shuffle_textfile_lines(old_file="", shuffled_file="", seed=0):
    random.seed(seed)
    lines = open(old_file, "r").readlines()
    random.shuffle(lines)
    open(shuffled_file, "w").writelines(lines)


# ========================================
# Merge multiple text files into one
# ========================================
def merge_text_files(folder_path="", combined_file_path=""):

    file_list = glob.glob(folder_path + "*.txt")

    with open(combined_file_path, "w") as file:
        input_lines = fileinput.input(file_list)
        file.writelines(input_lines)


# ========================================
# Count total characters in a sentence
# ========================================
def count_chars(sentence):
    total = 0
    for ch in sentence:
        total += 1
    return total


# ========================================
# Empty Function
# ========================================
def empty_function(no_args):
    pass


# =========================================
# Apply a function in whole text file
# =========================================
def apply_function_in_whole_text_file(
    function_name, myfile_path="", modified_file_path=""
):
    mylist = text_file_to_list(myfile_path=myfile_path, mylist=[])

    # mylist = [function_name(item) for item in mylist]
    newlist = list(map(function_name, mylist))

    list_to_text_file(mylist=newlist, myfile_path=modified_file_path)


# . venv/bin/activate
