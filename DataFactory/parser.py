class Parser:
    def __init__(self):
        self.data_per_line = []
        self.data_template = []
        self.data_filename = ""
        self.split_element = ""
        self.abbreviations = {"INT": "integer", "STR": "string", "[]": "list", "{}": "dictonary"}

    def get_data(self, data_file):
        # gets the filename and reads each line of the file
        self.data_filename = data_file
        try:
            self.data_per_line = open(self.data_filename).read().split("\n")
            # strip data
            self.data_per_line = [x for x in self.data_per_line if x.strip() != ""]

        except FileNotFoundError:
            print("\033[91mI didn't found your file!\033[0m")
            exit(1)

    def get_data_template(self):
        # gets the split element and the data template
        self.split_element = self.data_per_line[0]
        self.data_template = self.data_per_line[1]
        self.data_template = self.data_template.split(self.split_element)

        self.clean_data_template = []
        self.element_types = []
        # make the data template clean
        for element in self.data_template:
            self.element_types.append(element.split("|")[1])
            self.clean_data_template.append(element.split("|")[0])

    def split_actuall_data(self):
        # clean data
        actuall_data = self.data_per_line.copy()
        del actuall_data[0:2]
        self.clean_data = []

        for item in actuall_data:
            splitted_item = item.split(self.split_element)
            splitted_item = self.edit_splitted_item(splitted_item=splitted_item)
            self.clean_data.append(splitted_item)

    def edit_splitted_item(self, splitted_item):
        # saves as int list or string
        new_splitted_items = []

        for i, elm in enumerate(splitted_item):
            if self.element_types[i].lower() == "[]":
                new_splitted_items.append(elm.split(","))
            elif self.element_types[i].lower() == "int":
                new_splitted_items.append(int(elm))
            else:
                new_splitted_items.append(elm)

        return new_splitted_items


if __name__ == "__main__":
    parser = Parser()
    parser.get_data(data_file="../Tests/example_data.txt")
    parser.get_data_template()
    parser.split_actuall_data()
