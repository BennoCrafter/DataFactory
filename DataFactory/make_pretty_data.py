from DataFactory.parser import Parser


class PrettyData:
    def __init__(self, filename):
        self.parser = Parser()
        self.parser.get_data(data_file=filename)
        self.parser.get_data_template()
        self.parser.split_actuall_data()
        self.filename = "example_data"
        self.abbreviations = {"INT": "integer", "STR": "string", "[]": "list", "{}": "dictonary"}

    def write_data_in_string(self):
        self.filename = self.filename.upper()
        element_types = []
        template_data_attrs = f""
        i = 0
        data = ""

        for element in self.parser.clean_data:
            for item in element:
                data += f"__{self.parser.clean_data_template[i]}:__ <u>{item}</u>\n\n"
                i += 1
            i = 0

        i = 0
        for item in self.parser.element_types:
            new_item = self.abbreviations.get(item)
            element_types.append(new_item)

        for item in self.parser.clean_data_template:
            template_data_attrs += f"{item.upper()} as __{element_types[i]}__\n\n"
            i += 1
        self.pretty_data = f"# {self.filename}\n### DATA TEMPLATE:\n{template_data_attrs}\n### SPLIT OBJECT: {self.parser.split_element}\n## DATA:\n{data}"

    def write(self):
        with open(f"{self.filename}_pretty.md", "w") as file:
            file.write(self.pretty_data)
            file.close()


if __name__ == "__main__":
    pretty_data = PrettyData(filename="../Tests/example_data.txt")
    pretty_data.write_data_in_string()
    pretty_data.write()
