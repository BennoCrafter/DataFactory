from DataFactory.parser import Parser


class Return:
    def __init__(self, filename):
        self.parser = Parser()
        self.parser.get_data(data_file=filename)
        self.parser.get_data_template()
        self.parser.split_actuall_data()

    def get_colum(self, colum):
        if isinstance(colum, str):
            if colum in self.parser.clean_data_template:
                index = self.parser.clean_data_template.index(colum)
                output_list = []
                for element in self.parser.clean_data:
                    output_list.append(element[index])
                return index, output_list
            else:
                print(f"\033[91mPlease enter a valid cloum like {self.parser.clean_data_template}!\033[0m")
                exit()
        else:
            print("\033[91mPlease use an Str as colum!\033[0m")
            exit()

    def get_line(self, line):
        if isinstance(line, int):
            try:
                return self.parser.clean_data[line]
            except IndexError:
                print("\033[91mYou're using a to high or to low number!\033[0m")
                exit()
        else:
            print("\033[91mPlease use an Int as line!\033[0m")
            exit()

    def get_colum_from_line(self, colum, line):
        colum_output = self.get_colum(colum=colum)
        line_output = self.get_line(line=line)
        return line_output[colum_output[0]]


if __name__ == "__main__":
    get_output = Return(filename="../Tests/example_data.txt")
    print(get_output.get_colum(colum="name"))
    print(get_output.get_line(line=1))
    get_output.get_colum_from_line(colum="name", line=1)
