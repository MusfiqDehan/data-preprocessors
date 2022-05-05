<h1 align="center">
    <img src="https://github.com/MusfiqDehan/data-preprocessors/raw/master/branding/logo.png">
</h1>

<p align="center">
    An easy to use tool for Data Preprocessing specially for Text Preprocessing
</p>

## Table of Contents
- [Installation](https://github.com/MusfiqDehan/data-preprocessors#installation)
- [Quick Start](https://github.com/MusfiqDehan/data-preprocessors#quick-start)


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

