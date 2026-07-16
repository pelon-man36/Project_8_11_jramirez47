from notebook import Notebook
from pathlib import Path

def test_store_entries():
    """Testing store_entries method"""
    asking = Notebook()
    asking.store_entries()
    file = Path("entries.json")
    assert file.exists() == True


def test_read_stored_files():
    """Testing read_stored_files"""
    asking = Notebook()
    stored = asking.read_stored_entries()
    assert stored == []

def test_file_exists():
    asking = Notebook()
    assert asking.file_exist()

