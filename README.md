# phonetisch 

[![Build Status](https://travis-ci.org/muhammad-ahsan/phonetisch.svg?branch=master)](https://travis-ci.org/muhammad-ahsan/phonetisch) [![PyPI version](https://badge.fury.io/py/phonetisch.svg)](https://badge.fury.io/py/phonetisch)


Phonetic algorithms library in python focusing of multiple languages.

## Key features
* Implementation of Soundex and Caverphone.
* Simple to use.
* Support multiple languages.
* Supports Python 3.4+.

## Installation
Use pip to install the lastest version:

```bash
pip install phonetisch
```

## Usage Examples
```python
from phonetisch import soundex, caverphone

first_code = soundex.encode_word('Example')
second_code = soundex.encode_word('Ekzampul')

if first_code == second_code:
  print('Both words are homophones')
  
print(caverphone.encode_word("Thompson"))
```

## Reference
https://en.wikipedia.org/wiki/Soundex


## Links
* Project: https://github.com/muhammad-ahsan/phonetisch

## License
MIT License

## Contributers
* Muhammad Ahsan [@muhammad-ahsan](https://github.com/muhammad-ahsan)
* Dounia Sediame [@sediame](https://github.com/sediame)
