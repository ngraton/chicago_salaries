import pytest
import pandas as pd

def test_column_names():
  data = pd.read_csv('data/processed/chicago-salaries-processed.csv')
  assert 'name' in data.columns
