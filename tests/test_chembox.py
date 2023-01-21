import pytest
import os
import pandas as pd
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
    # Test for 2-digit substance
    assert get_elements('C5H12') == {'H': 12, 'C': 5}, "Incorrect result for 2-digit substance"
    # Test for multiple 2-digit substance
    assert get_elements('(C12H24)2') == {'H': 48, 'C': 24}, "Incorrect result for multiple 2-digit substance"

def test_get_molec_props():

    # Ensures that the dataset is in the correct place
    assert os.path.isfile('src/chembox/data/elements.csv') == True, 'The periodic table data set does not exist.'
    # Ensures that the returned dataframe is the correct shape
    assert get_molec_props('Al2(SO4)3(C2H4)5').shape == (5, 9), 'The get_molec_props function does not return the correct dataframe shape.'
    # Ensures that columns are in the correct order
    assert list(get_molec_props('Al2(SO4)3(C2H4)5')['Name']) == ['Aluminium', 'Carbon', 'Hydrogen', 'Oxygen', 'Sulfur'], 'The columns in the get_molec_props function are not in alphabetical order.'
    # Ensures that the function outputs the correct data frame
    assert get_molec_props('Al2(SO4)3(C2H4)5').equals(pd.read_csv("tests/get_molec_props_toy_df.csv", index_col=0))