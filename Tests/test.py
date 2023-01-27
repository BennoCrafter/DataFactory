from DataFactoryOld import return_output

filename = "example_data.txt"
# create object
df = return_output.Return(filename=filename)
# print a specific line
print(df.get_line(2))
# print a specific colum
print(df.get_colum("name"))
# print specific colum of line
print(df.get_colum_from_line("name", 1))
# add new line
