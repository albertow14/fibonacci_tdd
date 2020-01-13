import unittest
import pytest
from personal_error import ErrorNone
from personal_error import ErrorText
## CODIGO PRODUCCIÓN

def mi_fibonicci(index):
    if index is None:
        raise ErrorNone

    if index is str(index):
        raise ErrorText
    
    if index < 2:
        return index
        
    return mi_fibonicci(index - 1) + mi_fibonicci(index - 2)



## codigo de tests
class TestFibonacci(unittest.TestCase):
    def test_index_zero_return_zero(self):
        index = 0
        expected_result = 0

        result = mi_fibonicci(index)

        assert result == expected_result
    
    def test_index_one_return_one(self):
        index = 1
        expected_result = 1

        result = mi_fibonicci(index)
        
        assert result == expected_result

    def test_index_two_return_one(self):
        index = 2
        expected_result = 1

        result = mi_fibonicci(index)

        assert result == expected_result
    
    def test_index_three_return_two(self):
        index = 3
        expected_result = 2

        result = mi_fibonicci(index)

        assert result == expected_result

    def test_index_four_return_three(self):
        index = 4
        expected_result = 3
        
        result = mi_fibonicci(index)

        assert result == expected_result

    def test_index_ten_return_fifty_five(self):
        index = 10
        expected_result = 55

        result = mi_fibonicci(index)

        assert result == expected_result
   
    def test_index_none_return_error(self):
        index = None
        with pytest.raises(ErrorNone):
            assert mi_fibonicci(index)
        
    def test_index_text_type_personal_error(self):
        index = "personal_error"
        with pytest.raises(ErrorText):
            assert mi_fibonicci(index)