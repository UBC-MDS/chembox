def get_elements(molecule : str):
    """
    Convert a chemical molecule into its constituent elements with its respective counts as a dataframe.
    
    Parameters
    ----------
    molecule : str
        Chemical molecule.
    
    Returns
    -------
    dataframe
        The dataframe of each chemical elements with its molecular weight and count.
        
    Examples
    --------
    >>> from chembox.chembox import get_elements
    >>> get_elements('5(C2H4)')
    |    C    |    H    |    count    |
    |    2    |    4    |      5      |
    """

    # get_elements function code here
    # ...
    import pandas as pd
    
    
    
    return True

def is_valid(molecule: str) -> bool: 
    """
    Check if the given string of a chemical molecule is chemically valid

    Parameters
    ----------
    molecule : str
        Input chemical molecule

    Returns
    -------
    is_valid : bool
        True if the chemical molecule is valid and false otherwise

    Examples
    --------
    >>> from chembox.chembox import is_valid
    >>> is_valid('CH')
    False
    >>> is_valid('CH4')
    True
    >>> is_valid('CH3COOH')
    True
    """
    import pandas as pd
    
    return True

def get_molec_props(molecule: str):
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
    >>> from chembox.chembox import get_molec_props
    >>> get_molec_props('CH')
    | Element | Atomic_Mass | Atomic_Radius | Density | Electron_Config |
    |    C    |   12.011    |      170      | 2.2670  |   +4, +2, -4    |
    |    H    |   1.0080    |      120      |8.988e-5 |      +1/-1      |

    """
    import pandas as pd
    return True

def get_combustion_equation(molecule: str):
    """
    Returns a dataframe with a balanced combustion equation for the given molecule.
    
    Parameters
    ----------
    molecule : str
        Input chemical molecule as a string ready to be parsed

    Returns
    -------
    comb_df : dataframe
        A dataframe containing the balanced coefficients of the combustion equation relating to the molecule.

    Examples
    --------
    >>> from chembox.chembox import get_combustion_equation
    >>> get_combustion_equation('C5H12')
    | C5H12 | O2 | CO2 | H2O |
    |   1   |  8 |  5  |  6  | 
    """
    import pandas as pd

    if type(molecule) != str:
        raise TypeError("Molecule must be inserted as a string!")   

    C5H12 = pd.DataFrame({"C": [1], "H": [4], "count": [5]})
    # mol_df = get_elements(molecule)
    if not (set(C5H12.columns.tolist()) == set(["C", "H"]) or set(C5H12.columns.tolist()) == set(["C", "H", "count"])):
        raise KeyError("The molecule needs to have on carbon and hydrogen atoms, please try again")

    if not is_valid(molecule):
        return "The molecule inserted is not valid, please try again"

    # get atom counts from string parser
    num_C = C5H12.loc[0, "C"]
    num_H = C5H12.loc[0, "H"]
    num_O2 = (num_C * 2 + num_H/2) / 2
    num_mol = 1
    count = 1
    if "count" in C5H12.columns:
        count = C5H12.loc[0, "count"]

    comb_eq = pd.DataFrame({molecule: [num_mol], "O2": [num_O2], "CO2": [num_C], "H2O": [num_H/2]})

    # account for fractional oxygen
    if (num_O2 + num_C + num_H)%1 != 0:
        comb_eq = comb_eq.mul(2, axis=0)

    # multiplication factor
    if count > 1:
        comb_eq = comb_eq.mul(count, axis=0)

    return comb_eq.astype(int)