# PLC STRUCTS AS ARRAYS

A tutorial how to use structs and user derived types as arrays if the PLC IDE/Compiler doesnt allow for arrays. Working with booleans, numbers and user data types is shown in respective POUs that can be run on any PLC that is iec61131-3 compliant. For other data types the process is the same. On top of the examples the project contains struct arrays of 32 elements for each elementary type so the users can start using the functions immediately. If the operator needs different data types the Python generator script can be used. THe python script is located in the same repository as this file. Originally written in CODESYS 3.5. These DTs and POUs can be used under the MIT license.

## USAGE

The repository consists out of a CODESYS 3.5 project file, its generated PlcOpenXml and the serialized data in the docs folder.

* The codesys file can be opened with CODESYS and ran there.

* On different platforms than CODESYS the PlcOpenXml file can be used to import the data as no CODSYS native functions have been used in the project.

* Finally the user can read the code in markdown format located in this repository under docs folder or from this [link](docs/index_st.md)

## LICENSE

This project is meant as a tutorial and as it it can be used under the MIT license.