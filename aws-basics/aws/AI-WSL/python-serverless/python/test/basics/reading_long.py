import pandas as pd
import numpy as np

# Read the file using open() function
# file_name = input("Enter the file name: ")
file_name = 'SMSSpamCollection.tsv'

# Read the file using open() function
data = open(file_name).read()

# Split the data using '\n' as delimiter 
data = data.replace('\t', '\n').split('\n')

# Split the data labellist and textlist 
label_list = data[0::2]
text_list = data[1::2]

print(len(label_list), len(text_list))

df = pd.DataFrame({
    'Person': label_list,
    'text': text_list
})

# Alternative way to read the file
# df = pd.read_csv(file_name, sep='\t', header=None)
# df.columns = ['Person', 'text']
