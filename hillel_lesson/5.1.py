import keyword
import string
test_data=["_","__", "___"," ", "import","x","get_value","get value","get!value","some_super_puper_value","Get_value","get_Value","getValue","3m","m3","assert","assert_exception"]
forbidden_punc = string.punctuation.replace("_", "") + " "
for variable in test_data:
    if variable in keyword.kwlist:
        print(f"Incorrect variable name for: {variable}")
        continue
    if '0' <= variable[0] <= '9' :
        print(f"Incorrect variable name for: {variable}")
        continue
    if variable!=variable.lower() :
        print(f"Incorrect variable name for: {variable}")
        continue
    if forbidden_punc in variable :
        print(f"Incorrect variable name for: {variable}")
        continue

    else:
        print(f"Correct variable name for: {variable}")





