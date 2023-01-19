
import pytest
from chembox.chembox import *


def test_is_valid():

    # Test for Value
    with pytest.raises(ValueError):
        # check if ValueError is raised when the element input is wrong
        is_valid('Nx2CO3')

    with pytest.raises(ValueError):
        # check if ValueError is raised when the oxidation state is not unique
        # here, carbon alone can have multiple oxidation states
        is_valid('C2H6')

    # Test for calcium carbonate (a common salt)
    assert is_valid('Al2(SO4)3')

    # Test for sodium hydroxide (a common base)
    assert is_valid('NaOH')

    # Test for carbonic acid (a common acid)
    assert is_valid('H2CO3')

    # Test for invalid chemical (too many chlorines)
    assert not is_valid('H2(CO3)10')

     # Test for invalid chemical (too few sodiums)
    assert not is_valid('NaCO3')
    
def test_get_elements():
    
    # Test for one substance combination
    assert get_elements('(C2H4)5')=={'H': 20, 'C': 10}, "Incorrect result for one substance combination"
    # Test for two substance combination
    assert get_elements('Al2(SO4)3')== {'O': 12, 'S': 3, 'Al': 2}, "Incorrect result for two substance combination"
    # Test for more than two substance combination
    assert get_elements('Al2(SO4)3(C2H4)5') == {'H': 20, 'C': 10, 'O': 12, 'S': 3, 'Al': 2}, "Incorrect result for more than two substance combination"