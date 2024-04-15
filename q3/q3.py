# Author: P. Khanzadi
# Python: 3.9.7

# Library
import re

# Variables: Global
## Conditions' values
password_length_min       = 8
password_length_max       = 12
password_valid_characters = '[^a-zA-Z0-9@#]' # regular expression
special_characters        = '[@#]+' # regular expression


'''
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
'''

# Functions
def is_string(x):
    try:
        if isinstance(x, str) == True:
            return True
        else:
            return False
    except:
        return False


def is_password_length_valid(x,length_min,length_max):
    try:

        if len(x) >= length_min and len(x) <= length_max:
            return True
        else:
            return False
    except:
        return False


def is_password_characters_valid(x):
    try:
        if not(bool(re.search(password_valid_characters,x))) == True: 
            return True
        else:
            return False
    except:
        return False
    

def is_there_uppercase(x):
    try: 
        if bool(re.search('[A-Z]+',x)) == True: 
            return True
        else:
            return False
    except:
        return False


def is_there_lowercase(x):
    try: 
        if bool(re.search('[a-z]+',x)) == True: 
            return True
        else:
            return False
    except:
        return False

def is_there_special_character(x):
    try: 
        if bool(re.search(special_characters,x)) == True: 
            return True
        else:
            return False
    except:
        return False

def is_there_number(x):
    try: 
        if bool(re.search('[0-9+]',x)) == True: 
            return True
        else:
            return False
    except:
        return False


def is_password_valid(password):
    try:
        # Conditions: C_*
        C_is_password_string               = is_string(password)
        C_is_password_length               = is_password_length_valid(password,password_length_min,password_length_max)
        C_is_password_characters_valid     = is_password_characters_valid(password)
        C_is_password_characters_lowercase = is_there_lowercase(password) # at least one lowercase character, for example: 11a234
        C_is_password_characters_uppercase = is_there_uppercase(password) # at least one uppercase character, for example: 11A234
        C_is_password_characters_special   = is_there_special_character(password) # at least one special character, for example: 11@34
        C_is_password_number               = is_there_number(password) # at least one special character, for example: 11@34

        # Print Conditions:
        Text_C_1 = "Password is string: "+ str(C_is_password_string)
        Text_C_2 = "Password Length is Valid: "+ str(C_is_password_length)
        Text_C_3 = "Paswword Characters are Valid: "+ str(C_is_password_characters_valid)
        Text_C_4 = "At least one lowercase character: "+ str(C_is_password_characters_lowercase)
        Text_C_5 = "At least one uppercase character: "+ str(C_is_password_characters_uppercase)
        Text_C_6 = "At least one special character: "+ str(C_is_password_characters_special)
        Text_C_7 = "At least one number: "+ str(C_is_password_number)
        
        Text     = [Text_C_1, Text_C_2, Text_C_3, Text_C_4, Text_C_5, Text_C_6, Text_C_7]

        return Text

    except:
        return False, ['Error in the following function: is_password_valid ()']

'''
-----------------------------------------------------------------
-----------------------------------------------------------------
-----------------------------------------------------------------
'''


# Main 
password     = '*aa1aBCd@'
print('Password (input): '+ str(password))
output_text       = is_password_valid(password)
for t in output_text:
    print(t)

### Finish
