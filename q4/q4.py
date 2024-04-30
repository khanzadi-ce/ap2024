# Author: P. Khanzadi
# Python: 3.9.7

# Library
import re
from tabulate import tabulate
from collections import Counter
import pandas as pd


# Functions

## Read text file 
def read_text_file(input_text_file):
    with open(input_text_file) as f:
        text = f.read()
        return text


## Calculate (cal) word frequency (freq) from a string
def cal_word_freq_method_1(text):
  words_freq = Counter(re.findall(r'\b\w+\b', text))
  return words_freq

def cal_word_freq_method_2(text):
  words_freq = pd.Series(text.split()).value_counts()
  return words_freq

# Main 

## Read text file 
text = read_text_file('D:\\AdvancedProgramming\\ap2024\\q2\\input.txt')

## Change all alphabets to lowercase (LC) (for example: A -> a)
text_LC = text.lower()


## Calculate frequency of each word 
words_freq_method_1 = cal_word_freq_method_1(text_LC)
words_freq_method_2 = cal_word_freq_method_2(text_LC)





print('==================== Method 1 ===============================')

## Create table for output 
table = [ ['Word','Frequency'] ]
table.extend( [ list(item) for item in words_freq_method_1.items() ] )
## Print table: Method 1
print(tabulate(table, headers="firstrow", tablefmt="grid"))

print('=============================================================')
print('=============================================================')
print('==================== Method 2 ===============================')

## Create table for output 
table = [ ['Word','Frequency'] ]
table.extend( [ list(item) for item in words_freq_method_2.items() ] )
## Print table: Method 2
print(tabulate(table, headers="firstrow", tablefmt="grid"))

print('=============================================================')

### Finish

######################################################################
# Read more about regular expressions

