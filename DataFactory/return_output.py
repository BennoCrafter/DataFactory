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
                exit(1)
        else:
            print("\033[91mPlease use an str as colum!\033[0m")
            exit(1)

    def get_line_per_index(self, line):
        if isinstance(line, int):
            try:
                return self.parser.clean_data[line]
            except IndexError:
                print("\033[91mYou're using a to high or to low number!\033[0m")
                exit(1)
        else:
            print("\033[91mPlease use an int as line!\033[0m")
            exit(1)

    def get_line(self, colum_where_line_is, line):
        if isinstance(line, str):
            try:
                colum_list = self.get_colum(colum=colum_where_line_is)[1]
                return self.parser.clean_data[colum_list.index(line)]
            except:
                print("This linne doesn't exists!")
                exit(1)
        else:
            print("\033[91mPlease use an str as line!\033[0m")
            exit(1)

    def get_colum_from_line_per_index(self, colum, line):
        colum_output = self.get_colum(colum=colum)
        line_output = self.get_line_per_index(line=line)
        return line_output[colum_output[0]]

    def get_colum_from_line(self, colum_where_line_is, colum, line):
        colum_output = self.get_colum(colum=colum)
        line_output = self.get_line(colum_where_line_is=colum_where_line_is, line=line)
        return line_output[colum_output[0]]

    def get_best_match(self, user, users_colum, selection_colum):
        selection = self.get_colum(colum=users_colum)[1]
        decision_colum = self.get_colum(colum=selection_colum)[1]
        decision_colum = [set(hobby) for hobby in decision_colum]

        users_dict = dict(zip(selection, [{selection_colum: h} for h in decision_colum]))
        decision_colum = users_dict[user][selection_colum]

        best_match = None
        best_score = 0
        for other_user, other_user_data in users_dict.items():
            if other_user == user:
                continue
            other_user_decision_colum = other_user_data[selection_colum]
            intersection = decision_colum.intersection(other_user_decision_colum)
            union = decision_colum.union(other_user_decision_colum)
            score = len(intersection) / len(union)
            if score > best_score:
                best_score = score
                best_match = other_user
        return best_match


if __name__ == "__main__":
    get_output = Return(filename="../Tests/example_data.txt")
    print(get_output.get_colum(colum="name"))
    print(get_output.get_line_per_index(line=1))
    get_output.get_colum_from_line_per_index(colum="name", line=1)
    print(get_output.get_best_match(user="Benno", users_colum="name", selection_colum="hobbies"))