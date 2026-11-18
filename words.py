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

           
