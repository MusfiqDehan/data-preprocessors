# Data-Preprocessor
Preprocess your data before training a model.

## Installation
Install the stable release
For windows
`$ pip install -U data-preprocessors`

For Linux/WSL2
`$ pip3 install -U data-preprocessors`

## Quick Start
```python
from data_preprocessors import text_preprocessor as tp
sentence = "bla! bla- ?bla ?bla."
sentence = tp.remove_punc(sentence)
print(sentence)

>> bla bla bla bla
```

