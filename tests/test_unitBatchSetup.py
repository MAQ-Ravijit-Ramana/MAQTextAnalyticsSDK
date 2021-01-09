import pytest

from MAQTextSDK.BatchSetup import BatchSetup

def test_unit_init():
    with pytest.raises(TypeError):
        inputTransform = BatchSetup('test string')
        inputTransform.makeBody()

def test_unit_makeBody(input_text):
    inputTransform = BatchSetup(input_text)
    actual = inputTransform.makeBody()
    expected = {'data':[{'id':'0','text':'test sentence 1'},{'id':'1','text':'test sentence 2'},{'id':'2','text':'test sentence 3'}]}
    assert expected == actual