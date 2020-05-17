![Encipher screenshot](/screenshots/encipher_screenshot.png?raw=true "Optional Title")

# Encipher
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger) 
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

Encipher is a simple **File encryption commad-line tool** written in python.

  - Encrypt files
  - Decrypt files
  - Password protected 



🔍 Requirements
----

  - Linux distribution
  - Python 3 or greater
  - Vertual environment (optional) 



📦 Installation
----

Better run within a virtualenv

```sh
git clone git@github.com:RavisaraDev/encipher.git
cd encipher
pip install -r requirements.txt
``` 


🚀 Usage
----

You can simply run encipher by
```python
python encypher.py 
```
### or
Run with Command-Line Arguments
```python
python encipher.py [Option] [Folder_path] [Password]
```

#### Command-Line Arguments

| Argument name| Example argument | Explanation |
| -------- | ------- | -------- |
| Option | ```-e``` or ```-d```| ```-e``` to encrypt files ```-d``` to decrypt files|
| Folder_path |``` /john/Docs/Secrets```| Path to folder that needs to encrypt or decrypt|
| Password |``` #123&GhysA1```| Your passoword (To decrypt needs same passoword used to encrypt) |



🗞 License
----

Encipher is licensed under the [MIT License](/LICENSE)
