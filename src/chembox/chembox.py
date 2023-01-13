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

def get_molec_props(molecule : str):
    """
    Returns a dataframe with various properties of each element in the molecule

    Parameters
    ----------
    molecule : str
        Input chemical molecule as a string ready to be parsed

    Returns
    -------
    property_df : dataframe
        A dataframe containing the properties of the molecule.

    Examples
    --------
    >>> get_molec_props('CH')
    | Element | Atomic_Mass | Atomic_Radius | Density | Electron_Config |
    |    C    |   12.011    |      170      | 2.2670  |   +4, +2, -4    |
    |    H    |   1.0080    |      120      |8.988e-5 |      +1/-1      |

    """

def get_combustion_equation():
    # for Wilfred
    print('Hello world')
