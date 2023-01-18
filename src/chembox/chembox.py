import os
cur_dir = os.getcwd()
SRC_CHEMBOX = cur_dir[
    : cur_dir.index("chembox") + len("chembox")
] + '/src/chembox/'

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
    >>> from chembox import get_elements
    >>> get_elements('5(C2H4)')
    |    C    |    H    |    count    |
    |    2    |    4    |      5      |
    """

    # get_elements function code here
    # ...
    import pandas as pd
    
    
    
    return True


def get_components(molecule):
    """
    Convert a chemical molecule into its constituent elements with its respective counts as a dataframe.
    
    Parameters
    ----------
    molecule : str
        Chemical molecule.
    
    Returns
    -------
    defaultdict
        A dictionary that contains the elements as keys and values as counts
        
    Examples
    --------
    >>> from chembox import get_components
    >>> get_components('Na2SO4')
    defaultdict(int, {'Na': 2, 'S': 1, 'O': 4})
    """
    from collections import defaultdict
    import pandas as pd
    components = defaultdict(int)
    elements = pd.read_csv(SRC_CHEMBOX+ 'data/elements.csv')
    # find subcomponents
    while molecule.find(')') >= 0:
        end_brac = molecule.find(')')
        start_brac = end_brac - 1
        while molecule[start_brac] != '(':
            start_brac -= 1
        subcomponent = get_components(molecule[start_brac + 1:end_brac])
        ind_start = end_brac + 1 
        ind_end = ind_start + 1
        while ind_end < len(molecule) and molecule[ind_end].isnumeric():
            ind_end += 1

        # Get the subscript number
        num = molecule[ind_start: ind_end]
        # Update the count of the molecules
        for comp in subcomponent:
            subcomponent[comp] = subcomponent[comp] * int(num)
        # Remove the original string containing ()
        molecule = molecule.replace(molecule[start_brac:end_brac+1]+num, '')
        for comp in subcomponent:
            components[comp] += subcomponent[comp]

    # if there are no more brackets
    import re
    # split by capital letters
    elem_set = re.findall('[A-Z][^A-Z]*', molecule)
    for elem in elem_set:
        if re.search(r"\d", elem):
            components[elem[:re.search(r"\d", elem).start()]] += \
                int(elem[re.search(r"\d", elem).start():])
        else:
            components[elem] += 1
    
    return components


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
    >>> from chembox import is_valid
    >>> is_valid('Na2SO4')
    True
    >>> is_valid('CaCO3')
    True
    >>> is_valid('NaCl2')
    False
    """
    import pandas as pd
    from collections import defaultdict
    
    conjugates = pd.read_csv(SRC_CHEMBOX+'data/conjugates.csv')
    elements = pd.read_csv(SRC_CHEMBOX+'data/elements.csv')
    components = defaultdict(int)
    for conj in conjugates['name']:
        # if there exists a conjugate abbreviation
        if molecule.find(conj) >= 0:
            molecule = molecule.replace(conj, '')
            components[conj] = 1
            multiple_loc = molecule.find('()')

            # Handle if there are multiple conjugates
            if multiple_loc >= 0:
                ind_start = multiple_loc + len('()') 
                ind_end = ind_start + 1
                while ind_end < len(molecule) and molecule[ind_end].isnumeric():
                    ind_end += 1

                # Get the subscript number
                num = molecule[ind_start: ind_end]
                # Update the count of the molecules
                components[conj] = components[conj] * int(num)
                # Remove the original string containing ()
                molecule = molecule.replace('()'+num, '')
    # find if there exist brackets

    other_elem = get_components(molecule)
    for elem in other_elem:
        components[elem] += other_elem[elem]

    valance = 0

    for elem in components:
        if len(conjugates[conjugates['name']==elem]) == 1:
            valance += int(conjugates[conjugates['name']==elem]['valance']) * \
                components[elem]
        elif len(elements[elements['Symbol']==elem]) == 1:
            info = elements[elements['Symbol']==elem]
            group = int(info['Group'])
            period = int(info['Period'])

            if group > 3:
                elem_val = group - 18
            else:
                elem_val = group
            valance += elem_val * \
                components[elem]
        else:
            raise ValueError('An unknown element '+elem+' entered. Please check your input.')
    # check if final valance is 0
    return valance == 0

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
    >>> from chembox import get_molec_props
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
    >>> from chembox import get_combustion_equation
    >>> get_combustion_equation('C5H12')
    | C5H12 | O2 | CO2 | H2O |
    |   1   |  8 |  5  |  6  | 
    """
    import pandas as pd
    return True