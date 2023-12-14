import pytest
from unittest.mock import patch, mock_open

from src.configloader import ConfigLoader

@patch("builtins.open", new_callable=mock_open, read_data="key: value")
def test_read_file(mock_open):
    cls = ConfigLoader()
    result = cls._ConfigLoader__read_file('dummy_path')
    assert result == 'key: value'

def test_load_from_string():
    data = 'key: value'
    result = ConfigLoader.load_from_string(data)
    assert result.key == 'value'

def test_load_from_string_with_node():
    data = 'parent:\n  child: value'
    result = ConfigLoader.load_from_string(data, 'parent')
    assert result.child == 'value'

@patch("builtins.open", new_callable=mock_open, read_data="key: value")
def test_load(mock_open):
    cls = ConfigLoader(file_paths=['dummy_path'])
    result = cls.load()
    assert result.key == 'value'

@patch("builtins.open", new_callable=mock_open, read_data="parent:\n  child: value")
def test_load_with_node(mock_open):
    cls = ConfigLoader(file_paths=['dummy_path'])
    result = cls.load('parent')
    assert result.child == 'value'