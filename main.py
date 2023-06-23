import oyaml as yaml
from tokens import *

with open("main.yaml", "r") as file:
    y = yaml.safe_load(file)

if y['START']:
    process_tokens(y['START'])

