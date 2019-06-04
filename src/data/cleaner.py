import pandas as pd
import re

def pythonify_columns(data):
  return data.rename(to_snake, axis='columns')

def to_snake(string):
    return re.sub("([\s]+|[-]+|[+]+)", "_", string).lower().lstrip("_")
