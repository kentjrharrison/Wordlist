def num_letters(num_rows,num_cols):
    w_row=num_rows-2
    w_col=num_cols-2
    whitespace=w_row*w_col
    return (num_rows*num_cols)-whitespace
assert num_letters(3,4) == 10  #3 is the num_rows and 4 is the num_columns
print("Checking assertions.")
assert num_letters(13,4) == 30
print("1 works")
assert num_letters(4,4) == 12
print("2 works")
assert num_letters(6,4) == 16
print("3 works")
assert num_letters(6,7)==22
print("4 works")
import numpy as np
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file
print(rows)
print(columns)
words.extend(data[0,:].tolist())
words.extend(data[1:-1,0].tolist())
words.extend(data[-1,:].tolist())
words.extend(data[1:-1,-1].tolist())
   
print(words) #check that you collected all the letters in your data file
assert len(words) == num_letters(rows, columns) 

#this should not throw an error. If it does, most likely your main code is not getting the correct number of letters

  #this should not throw an error. If it does, most likely your main code is not getting the correct number of letters
