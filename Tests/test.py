from DataFactory import return_output

filename = "example_data.txt"
# create object
df = return_output.Return(filename=filename)
# print a specific line
print(df.get_line(2))
# print a specific colum
print(df.get_colum("name"))
# print specific colum of line
print(df.get_colum_from_line("name", 1))
# find best match for user A with the selctions of hobbies
print(df.get_best_match(user="John", users_colum="name", selection_colum="hobbies"))