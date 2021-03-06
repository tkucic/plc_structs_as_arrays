# PLC Using structs as arrays | [MAIN] | [NAMESPACES] | [METRICS] | [BACK]  

## Documentation for Function block getUDT_Status32  

```pascal
INTERFACE
    VAR_INPUT 
        data : UDT_Status32; (*Data to work on*)
        ix : USINT; (*Index to retrieve*)
    END_VAR
    VAR_OUTPUT 
        Out : UDT_Status; (*Returned data*)
    END_VAR
END_INTERFACE
FUNCTION_BLOCK getUDT_Status32:
    CASE ix OF
    	0: Out := data.udt00; (*Return index 0 for the data struct*)
    	1: Out := data.udt01; (*Return index 1 for the data struct*)
    	2: Out := data.udt02; (*Return index 2 for the data struct*)
    	3: Out := data.udt03; (*Return index 3 for the data struct*)
    	4: Out := data.udt04; (*Return index 4 for the data struct*)
    	5: Out := data.udt05; (*Return index 5 for the data struct*)
    	6: Out := data.udt06; (*Return index 6 for the data struct*)
    	7: Out := data.udt07; (*Return index 7 for the data struct*)
    	8: Out := data.udt08; (*Return index 8 for the data struct*)
    	9: Out := data.udt09; (*Return index 9 for the data struct*)
    	10: Out := data.udt10; (*Return index 10 for the data struct*)
    	11: Out := data.udt11; (*Return index 11 for the data struct*)
    	12: Out := data.udt12; (*Return index 12 for the data struct*)
    	13: Out := data.udt13; (*Return index 13 for the data struct*)
    	14: Out := data.udt14; (*Return index 14 for the data struct*)
    	15: Out := data.udt15; (*Return index 15 for the data struct*)
    	16: Out := data.udt16; (*Return index 16 for the data struct*)
    	17: Out := data.udt17; (*Return index 17 for the data struct*)
    	18: Out := data.udt18; (*Return index 18 for the data struct*)
    	19: Out := data.udt19; (*Return index 19 for the data struct*)
    	20: Out := data.udt20; (*Return index 20 for the data struct*)
    	21: Out := data.udt21; (*Return index 21 for the data struct*)
    	22: Out := data.udt22; (*Return index 22 for the data struct*)
    	23: Out := data.udt23; (*Return index 23 for the data struct*)
    	24: Out := data.udt24; (*Return index 24 for the data struct*)
    	25: Out := data.udt25; (*Return index 25 for the data struct*)
    	26: Out := data.udt26; (*Return index 26 for the data struct*)
    	27: Out := data.udt27; (*Return index 27 for the data struct*)
    	28: Out := data.udt28; (*Return index 28 for the data struct*)
    	29: Out := data.udt29; (*Return index 29 for the data struct*)
    	30: Out := data.udt30; (*Return index 30 for the data struct*)
    	31: Out := data.udt31; (*Return index 31 for the data struct*)
    ELSE
    	(*Index is invalid, return initial function value*)
    	Out := Out;
    END_CASE

END_FUNCTION_BLOCK
```

## Metrics  

- VAR_INPUT : 2
- VAR_OUTPUT : 1

| Actions | Lines of code | Maintainable size |
| ------- | ------------- | ----------------- |
| 0 | 37 | 43 |

---
Autogenerated with [ia_tools](https://github.com/tkucic/ia_tools)  

[MAIN]: ../../../../index_st.md
[NAMESPACES]: ../../nsList_st.md
[METRICS]: ../../../metrics_st.md
[BACK]: ../nsMain_st.md
