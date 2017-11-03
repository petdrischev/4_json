# Prettify JSON

Getting pretty print for json load file format.
# How use

Module contains 2 functions:
```python
def load_data(filepath):
    ...
    return data
  
def pretty_print_json(json_data):
    ...
    print(json_data)
```
Where filepath, it's path to load json file.
Example:
```python
import pprint_json
filepath = "./json_file.json"
json_loaded_data = load_data(filepath)
pretty_print_json(json_loaded_data)
```
# Quickstart

Example of script launch on Linux, Python 3.5:

```bash

$ python pprint_json.py <path to file>
# output example
#[
#    {
#        "Cells": {
#            "Address": "улица Академика Павлова, дом 10",
#           "AdmArea": "Западный административный округ",
#            "ClarificationOfWorkingHours": null,
#            "District": "район Кунцево",
#            "IsNetObject": "да",
#            "Name": "Ароматный Мир",
#           "OperatingCompany": "Ароматный Мир",
#           "PublicPhone": [
#               {
#                    "PublicPhone": "(495) 777-51-95"
#                }
#            ],
# ....
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
