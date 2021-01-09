import pytest

@pytest.fixture
def input_text():
    corpus = ["test sentence 1","test sentence 2","test sentence 3"]
    return corpus
