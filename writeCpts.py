

def createDt(name, sizeOfArray=32):
    """Takes in a name of a data type and creates a structure of given size.
    Returns a string that can be copied easily to a plc IDE."""
    txt = f'TYPE {name}{sizeOfArray} : \n'
    txt += '\tSTRUCT\n'
    for i in range(sizeOfArray):
        txt += f'\t\tix{str(i).zfill(2)} : {name}; (*Index {str(i).zfill(2)} of struct array *)\n'
    txt += '\tEND_STRUCT\n'
    txt += 'END_TYPE\n'
    return txt

def createGetter(name, sizeOfArray=32):
    """Takes in a name of a data type and creates a function that handles it.
    Returns a string that can be copied easily to a plc IDE.
    This works only with elementary types as udts are not returnable"""
    txt = f'FUNCTION get{name.capitalize()}{sizeOfArray} : {name}\n'
    txt += '\tVAR_INPUT\n'
    txt += f'\t\tdata : {el}32; (*Data to work on*)\n'
    txt += '\t\tix : USINT; (*Index to retrieve*)\n'
    txt += '\tEND_VAR\n'

    txt += 'CASE ix OF\n'
    for i in range(sizeOfArray):
        txt += f'\t{i}: get{name.capitalize()}{sizeOfArray} := data.ix{str(i).zfill(2)}; (*Return index {i} for the data struct*)\n'
    txt += 'ELSE\n'
    txt += '\t(*Index is invalid, return initial function value*)\n'
    txt += '\tRETURN;\n'
    txt += 'END_CASE\n'
    txt += 'RETURN;\n'
    return txt

def createSetter(name, sizeOfArray=32):
    """Takes in a name of a data type and creates a function that handles it.
    Returns a string that can be copied easily to a plc IDE.
    This works only with elementary types as udts are not returnable"""
    txt = f'FUNCTION set{name.capitalize()}{sizeOfArray} : BOOL\n'
    txt += '\tVAR_IN_OUT\n'
    txt += f'\t\tdata : {name}{sizeOfArray}; (*Data to work on*)\n'
    txt += '\tEND_VAR\n'
    txt += '\tVAR_INPUT\n'
    txt += '\t\tix : USINT; (*Index to write*)\n'
    txt += f'\t\tvalue : {name}; (*Value to set to the index*)\n'
    txt += '\tEND_VAR\n'

    #Write code
    txt += 'CASE ix OF\n'
    for i in range(sizeOfArray):
        txt += f'\t{i}: data.ix{str(i).zfill(2)} := value; (*Set index {i} of the data struct with the value*)\n'
    txt += 'ELSE\n'
    txt += "\t(*Index is invalid, don't write anything, return false*)\n"
    txt += f"\tset{name.capitalize()}{sizeOfArray} := FALSE;\n"
    txt += '\tRETURN;\n'
    txt += 'END_CASE\n'
    txt += f"set{name.capitalize()}{sizeOfArray} := TRUE;\n"
    txt += 'RETURN;\n'
    return txt

if __name__ == '__main__':
    elDts = [
        'BOOL',             'BYTE',         'WORD',         'DWORD',	
        'LWORD',            'SINT',	        'USINT',        'INT',
        'UINT',	            'DINT',	        'UDINT',	    'LINT',	
        'ULINT',            'REAL',         'LREAL',        'STRING',
        'WSTRING',          'TIME',         'LTIME',        'DATE',
        'LDATE',            'DATE_AND_TIME','LDATE_AND_TIME',
        'TIME_OF_DAY',      'LTIME_OF_DAY'
    ]
    for el in elDts:
        print(createDt(el, 32))
        print(createGetter(el, 32))
        print(createSetter(el, 32))
