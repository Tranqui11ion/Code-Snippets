"""
Compares two csv files and confirms if they contain the same data. 
Make sure both CSVs have the same column names before reformatting them using test_subset_data.
Modify col_names to match with data being tested
"""


import pandas as pd
import filecmp

col_names = ['LDG_NAME', 'ACCNBRI', 'PERIOD', 'SEQNBR', 'LDG_TRANS_RID', 'DOC_TYPE' ]

"""
This method takes in a csv file(filename) sets the columns using the col_names variable(modify as needed), 
and outputs the result as a .txt file. Put full path name if filename and output_path are not within the same folder.

"""
def test_subset_data( filename, output_path, col_names):
    output_txt = open(output_path, 'w+')
    df = pd.read_csv(filename, header=0, usecols= col_names)
    newdf = df.sort_values(by=['LDG_TRANS_RID'])
    newdf.to_csv(output_txt, index=False)

"""
Compares two files and checks for matching data
"""
def compare_data_subsets(file1, file2):
    result = filecmp.cmp(file1, file2, shallow=False)
    return result

#-----------------TEST---------------------------
test_subset_data("csv1.csv", "txtfile1.txt", col_names)
test_subset_data("csv2.csv", "txtfile2.txt", col_names)

set1 = "txtfile1.txt"
set2 = "txtfile2.txt"
print(compare_data_subsets(set1, set2))
