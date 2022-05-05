<h1>
    <img src="https://github.com/MusfiqDehan/data-preprocessors/raw/master/branding/logo.png">
</h1>

[![](https://img.shields.io/pypi/v/data-preprocessors.svg)](https://pypi.org/project/data-preprocessors/)
[![Downloads](https://static.pepy.tech/personalized-badge/data-preprocessors?period=total&units=international_system&left_color=black&right_color=orange&left_text=Downloads)](https://pepy.tech/project/data-preprocessors)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1mJuRfIz__uS3xoFaBsFn5mkLE418RU19?usp=sharing)
[![Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://kaggle.com/kernels/welcome?src=https://github.com/keras-team/keras-io/blob/master/examples/vision/ipynb/mnist_convnet.ipynb)

<p>
    An easy to use tool for Data Preprocessing specially for Text Preprocessing
</p>

## **Table of Contents**
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Functions](#functions)
    - [Split Textfile](#split-textfile)
    - [Parallel Corpus Builder](#split-textfile)
    - [Remove Punc](#split-textfile)

## **Installation**
Install the latest stable release<br>
**For windows**<br>
`$ pip install -U data-preprocessors`

**For Linux/WSL2**<br>
`$ pip3 install -U data-preprocessors`

## **Quick Start**
```python
from data_preprocessors import text_preprocessor as tp
sentence = "bla! bla- ?bla ?bla."
sentence = tp.remove_punc(sentence)
print(sentence)

>> bla bla bla bla
```

## **Functions**
### Split Textfile

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

