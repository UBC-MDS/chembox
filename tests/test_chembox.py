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

    expected = get_combustion_equation(C5H12)
    actual = pd.DataFrame(({"C5H12": [1], "O2": [8], "CO2": [5], "H2O": [6]}))
    assert actual == expected, "Balancing carbon or hydrogen incorrectly"

    expected = get_combustion_equation(C6H14)
    actual = pd.DataFrame(({"C6H14": [2], "O2": [19], "CO2": [12], "H2O": [14]}))
    assert actual == expected, "Balancing fractional oxygen incorrectly!"

    try:
        expected = get_combustion_equation(CO2)
    except KeyError:
        raise KeyError("Molecule needs only carbon and hydrogen atoms")

    try:
        expected = get_combustion_equation(LiH)
    except:
        raise KeyError("Molecule needs only carbon and hydrogen atoms")

    try:
        expected = get_combustion_equation(NO2)
    except:
        raise KeyError("Molecule needs only carbon and hydrogen atoms")

    try:
        expected = get_combustion_equation(1.0)
    except:
        raise TypeError("Molecule must be inserted as a string!")
    
    expected = get_combustion_equation(CH4)
    actual = pd.DataFrame(({"CH4": [1], "O2": [2], "CO2": [1], "H2O": [2]}))
    assert actual == expected, "Balancing when hydrogen is not 2*C+2"

    expected = get_combustion_equation(CH45)
    actual = pd.DataFrame(({"CH4": [5], "O2": [10], "CO2": [5], "H2O": [10]}))
    assert actual == expected, "Balancing with a multiplication factor"

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
