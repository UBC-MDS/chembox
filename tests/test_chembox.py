from chembox.chembox import *
import pandas as pd
import pytest

def test_get_combustion_equation():
    """ Test function for unit tests of the `get_combustion_equation`

    Raises:
        KeyError: Check if a molecule has only C and H atoms
        KeyError: Check if a molecule has only C and H atoms
        KeyError: Check if a molecule has only C and H atoms
        TypeError: Check if a molecule has string type
    """
    C5H12 = "C5H12"
    C6H14 = "C6H14"
    CO2 = "CO2"
    LiH = "LiH"
    NO2 = "NO2"
    CH4 = "CH4"
    CH45 = "(CH4)5"
    
    # test no half factor, regular CH molecule
    expected = get_combustion_equation(C5H12)
    actual = pd.DataFrame(({"C5H12": [1], "O2": [8], "CO2": [5], "H2O": [6]}))
    assert actual.equals(expected), "Balancing carbon or hydrogen incorrectly"

    # test multiplication factor
    expected = get_combustion_equation(C6H14)
    actual = pd.DataFrame(({"C6H14": [2], "O2": [19], "CO2": [12], "H2O": [14]}))
    assert actual.equals(expected), "Balancing fractional oxygen incorrectly!"

    # test a different regular, not just 2*C + 2
    expected = get_combustion_equation(CH4)
    actual = pd.DataFrame(({"CH4": [1], "O2": [2], "CO2": [1], "H2O": [2]}))
    assert actual.equals(expected), "Balancing when hydrogen is not 2*C+2"

    # test only C is in the molecule
    with pytest.raises(KeyError):
        get_combustion_equation(CO2)

    # test only H is in the molecule
    with pytest.raises(KeyError):
        get_combustion_equation(LiH)

    # test neither C or H is in the molecule
    with pytest.raises(KeyError):
        get_combustion_equation(NO2)

    # test inputting not a string
    with pytest.raises(TypeError):
        get_combustion_equation(1.0)
    
    # test input with brackets
    with pytest.raises(KeyError):
        get_combustion_equation(CH45)


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
