<div align="center">
    
<img src="https://github.com/MusfiqDehan/data-preprocessors/raw/master/branding/logo.png">

<p>Data Preprocessors</p>

<sub>An easy-to-use tool for Data Preprocessing especially for Text Preprocessing</sub>

<!-- Badges -->

<!-- [<img src="https://deepnote.com/buttons/launch-in-deepnote-small.svg">](PROJECT_URL) -->
    
[![](https://img.shields.io/pypi/v/data-preprocessors.svg)](https://pypi.org/project/data-preprocessors/)
[![Downloads](https://img.shields.io/pypi/dm/data-preprocessors)](https://pepy.tech/project/data-preprocessors)
    
<!-- [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mJuRfIz__uS3xoFaBsFn5mkLE418RU19?usp=sharing)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/keras-team/keras-io/blob/master/examples/vision/ipynb/mnist_convnet.ipynb) -->

</div>

## **Table of Contents**

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
    - [Split Textfile](#split-textfile)
    - [Build Parallel Corpus](#build-parallel-corpus)
    - [Separate Parallel Corpus](#separate-parallel-corpus)
    - [Decontruct Words of Sentence](#deconstruct-word-of-sentence)
    - [Remove Punctuation](#remove-punctuation)
    - [Space Punctuation](#space-punctuation)
    - [Text File to List](#text-file-to-list)
    - [Text File to Dataframe](#text-file-to-dataframe)
    - [List to Text File](#list-to-text-file)
    - [Remove File](#remove-file)
    - [Count Characters of a Sentence](#count-characters-of-a-sentence)
    - [Count Words of Sentence](#count-characters-of-a-sentence)
    - [Count No of Lines in a Text File](#count-no-of-lines-in-a-text-file)
    - [Convert Excel to Multiple Text Files](#convert-excel-to-multiple-text-files)
    - [Merge Multiple Text Files](#merge-multiple-text-files)
    - **[Apply Any Function in a Full Text File](#apply-a-function-in-whole-text-file)**

    

## **Installation**
Install the latest stable release<br>
**For windows**<br>
```
pip install -U data-preprocessors
```

**For Linux/WSL2**<br>
```
pip3 install -U data-preprocessors
```

## **Quick Start**

```python
from data_preprocessors import text_preprocessor as tp
sentence = "bla! bla- ?bla ?bla."
sentence = tp.remove_punc(sentence)
print(sentence)

>> bla bla bla bla
```

## **Features**

### Split Textfile

This function will split your textfile into train, test and validate. Three separate text files. By changing `shuffle` and `seed` value, you can randomly shuffle the lines of your text files.

```python
from data_preprocessors import text_preprocessor as tp
tp.split_textfile(
    main_file_path="example.txt",
    train_file_path="splitted/train.txt",
    val_file_path="splitted/val.txt",
    test_file_path="splitted/test.txt",
    train_size=0.6,
    val_size=0.2,
    test_size=0.2,
    shuffle=True,
    seed=42
)

# Total lines:  500
# Train set size:  300
# Validation set size:  100
# Test set size:  100
```

### Separate Parallel Corpus

By using this function, you will be able to easily separate `src_tgt_file` into separated `src_file` and `tgt_file`.

```python
from data_preprocessors import text_preprocessor as tp
tp.separate_parallel_corpus(src_tgt_file="", separator="|||", src_file="", tgt_file="")
```

### Decontracting Words from Sentence

```python
tp.decontracting_words(sentence)
```

### Remove Punctuation

By using this function, you will be able to remove the punction of a single line of a text file.

```python
from data_preprocessors import text_preprocessor as tp
sentence = "bla! bla- ?bla ?bla."
sentence = tp.remove_punc(sentence)
print(sentence)

# bla bla bla bla
```

### Space Punctuation

By using this function, you will be able to add one space to the both side of the punction so that it will easier to tokenize the sentence. This will apply on a single line of a text file. But if we want, we can use it in a full twxt file.

```python
from data_preprocessors import text_preprocessor as tp
sentence = "bla! bla- ?bla ?bla."
sentence = tp.space_punc(sentence)
print(sentence)

# bla bla bla bla
```

### Text File to List

Convert any text file into list.

```python
 mylist= tp.text2list(myfile_path="myfile.txt")
```

### List to Text File

Convert any list into a text file (filename.txt)

```python
tp.list2text(mylist=mylist, myfile_path="myfile.txt")
```

### Count Characters of a Sentence

This function will help to count the total characters of a sentence.

```python
tp.count_chars(myfile="file.txt")
```

### Convert Excel to Multiple Text Files

This function will help to Convert an Excel file's columns into multiple text files.

```python
tp.excel2multitext(excel_file_path="",
                    column_names=None,
                    src_file="",
                    tgt_file="",
                    aligns_file="",
                    separator="|||",
                    src_tgt_file="",
                    )
```

### Apply a function in whole text file

In the place of `function_name` you can use any function and that function will be applied in the full/whole text file.

```python
from data_preprocessors import text_preprocessor as tp
tp.apply_whole(
    function_name, 
    myfile_path="myfile.txt", 
    modified_file_path="modified_file.txt"
)
```

