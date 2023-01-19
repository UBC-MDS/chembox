
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
    >>> get_elements('(C2H4)5')
    {'H': 20, 'C': 10}
    >>> get_elements('Al2(SO4)3')
    {'O': 12, 'S': 3, 'Al': 2}
    """

    # get_elements function code here
    import pandas as pd
    import numpy as np
    
    # Read fundamental elements
    # don't forget to change path to /data/elements.csv
    element = pd.read_csv('/data/elements.csv')
    symbol = element['Symbol']
    symbol_len1 = element.loc[element['Symbol'].str.len() == 1, 'Symbol']
    symbol_len2 = element.loc[element['Symbol'].str.len() == 2, 'Symbol']
    
    #1 Check fundamental elements of length = 2
    pos_2 = []
    elm_2 = []
    for elm in symbol_len2:
        if molecule.find(elm) != -1:    
            pos_2.append(molecule.find(elm))
            elm_2.append(molecule[molecule.find(elm):molecule.find(elm)+2])
               
    #2 Check fundamental elements of length = 1
    pos_1 = []
    elm_1 = []
    for elm in symbol_len1:
        if molecule.find(elm) != -1:    
            pos_1.append(molecule.find(elm))
            elm_1.append(molecule[molecule.find(elm)])
    
    #3 Construct basic number of fundamental elements
    #3.1 for fundamental elements of length = 1
    no_1 = []
    for pos in pos_1:
        if molecule[pos+1].isdigit():
            no_1.append(molecule[pos+1])
        else:
            no_1.append(1)      
    #3.2 for fundamental elements of length = 2       
    no_2 = []
    for pos in pos_2:
        no_2.append(molecule[pos+2])
        
    #4 Make intermediate dataframe result
    imd = {'element': np.concatenate([elm_1,elm_2]),
        'pos': np.concatenate([pos_1,pos_2]),
        'no': np.concatenate([no_1,no_2]),
        'parent': np.zeros(len(np.concatenate([elm_1,elm_2]))),
        'parent_start': np.zeros(len(np.concatenate([elm_1,elm_2]))),
        'parent_stop': np.zeros(len(np.concatenate([elm_1,elm_2]))),
        'mult': np.zeros(len(np.concatenate([elm_1,elm_2]))),
        'mult_no': np.zeros(len(np.concatenate([elm_1,elm_2])))}
    imd_df = pd.DataFrame(imd)
        
    #4 Detect parenthesis
    pos_parent_start = []
    for idx, i in enumerate(molecule):
        if i == "(":
            pos_parent_start.append(idx)
    pos_parent_stop = []
    for idx, i in enumerate(molecule):
        if i == ")":
            pos_parent_stop.append(idx)
            
    #5 Adding parenthesis position to dataframe
    for i in range(len(pos_parent_start)):
        # print(pos_parent_start[i],pos_parent_stop[i])
        
        for j, pos in enumerate(imd['pos']):
            # print(i,pos_parent_start[i],pos_parent_stop[i],j,pos)
            
            if pos>pos_parent_start[i] and pos<pos_parent_stop[i]:
                imd_df.iloc[j,4] = pos_parent_start[i]
                imd_df.iloc[j,5] = pos_parent_stop[i]
                imd_df.iloc[j,3] = 1
    
    #6 Multiply with no. of substances
    for i in range(imd_df.shape[0]):
        # print(i,molecule[int(imd_df.iloc[i,5]+1)])
        if imd_df.iloc[i,3]==1:
            imd_df.iloc[i,6] = molecule[int(imd_df.iloc[i,5]+1)]
            imd_df.iloc[i,7] = int(imd_df.iloc[i,6]) * int(imd_df.iloc[i,2])
        else:
            imd_df.iloc[i,7] = 1 * int(imd_df.iloc[i,2])
            
    #7 Final dictionary
    imd_df['mult_no'] = imd_df['mult_no'].astype(int)
    final_dict = {k:v for k,v in zip(imd_df['element'],imd_df['mult_no'])}
    
    return final_dict


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
    elements = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/chembox/main/src/chembox/data/elements.csv')
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
    
    conjugates = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/chembox/main/src/chembox/data/conjugates.csv')
    elements = pd.read_csv('https://raw.githubusercontent.com/UBC-MDS/chembox/main/src/chembox/data/elements.csv')
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
            ox_state = (info['OxidationStates'])

            try:
                elem_val = int(ox_state)
            except ValueError:
                raise ValueError('Oxidation state of '+ elem+ ' could be multiple. The formula could not be easily checked.')

            valance += elem_val * components[elem]
        else:
            raise ValueError('An unknown element '+elem+' entered. Please check your input.')

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