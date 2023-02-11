from DataFactory import return_output

filename = "example_data.txt"
# create object
df = return_output.Return(filename=filename)
# print a specific line per index
print(df.get_line_per_index(line=2))
# print a specific colum
print(df.get_colum(colum="name"))
# print specific colum of line per index
print(df.get_colum_from_line_per_index("name", 1))
# find best match for user A with the selctions of hobbies
print(df.get_best_match(user="John", users_colum="name", selection_colum="hobbies"))
# print specific colum of a line
print(df.get_colum_from_line(colum_where_line_is="name", line="Jim", colum="hobbies"))
# print specific line
print(df.get_line(colum_where_line_is="name", line="Jim"))