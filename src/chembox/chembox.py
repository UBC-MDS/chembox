import pandas as pd

def get_elements(formula):
    """
    Convert chemistry formular into fundamental chemical elements with its respective counts as a dataframe.
    
    Parameters
    ----------
    formula : str
        Chemistry formular.
    
    Returns
    -------
    dataframe
        The dataframe of each chemical elements with its molecular weight and count.
        
    Examples
    --------
    >>> from chembox import get_elements
    >>> get_elements('5(C2H4)')
    --------------
    C - H - count
    2 - 4 - 5
    """

    # get_elements function code here
    # ...
    
    return True

def is_valid(formula: str) -> bool: 
    """
    Check if a given string chemical formula is chemically valid

    Parameters
    ----------
    formula : str
        Input chemical formula

    Returns
    -------
    is_valid : bool
        True if the chemical formula is valid and false otherwise

    Examples
    --------
    >>> is_valid('CH')
    False
    >>> is_valid('CH4')
    True
    >>> is_valid('CH3COOH')
    True
    """
    
    return True

def get_molar_mass():
    # for Vikram
    return 0.0

def get_combustion_equation():
    # for Wilfred
    print('Hello world')
