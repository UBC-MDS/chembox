from chembox.chembox import *
import pandas as pd

def test_get_combustion_equation():
    """Test combustion equation with possible chemicals."""
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
