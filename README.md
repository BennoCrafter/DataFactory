# DataFactory
A little Pandas clone

# How to use it?
###create DataFactory object
<code>df = return_output.Return(filename=filename)</code>

# Features

### print a specific line
<code>print(df.get_line(2))</code>
### print a specific colum
<code>print(df.get_colum("name"))</code>
### print specific colum of line
<code>print(df.get_colum_from_line("name", 1))</code>
### find best match for user John with the selctions of hobbies and names
<code>print(df.get_best_match(user="John", users_colum="name", selection_colum="hobbies"))</code>