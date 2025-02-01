import re

def preprocess_code(input_string):
    return re.sub(r'^[^\n]*```(python|sql)[^\n]*\n|[^\n]*```[^\n]*\n|```$', '', input_string, flags=re.MULTILINE)