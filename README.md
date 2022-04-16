# Data-Preprocessor
An easy to use tool for Data Preprocessing specially for Text Preprocessing

## Installation
Install the stable release<br>
For windows<br>
`$ pip install -U data-preprocessors`

For Linux/WSL2<br>
`$ pip3 install -U data-preprocessors`

## Quick Start
```python
from data_preprocessors import text_preprocessor as tp
sentence = "bla! bla- ?bla ?bla."
sentence = tp.remove_punc(sentence)
print(sentence)

>> bla bla bla bla
```

