#!/usr/bin/python
import oyaml as yaml
import sys
from tokens import *

with open(sys.argv[1], "r") as file:
    y = yaml.safe_load(file)
try:
    if y['START']:
        process_tokens(y['START'])
except KeyError:
    print("Missing START: collection.")

 