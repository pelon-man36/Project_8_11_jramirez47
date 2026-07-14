class Notebook():
    def __init__(self, entries=0):
        self.entries = entries

    def create_entries(self):
        """Writes entries for notebook"""
        empty_list = []
        for entry in range(1, self.entries + 1):
            print(f"Write for entry #{entry}")
            text = input("")
            empty_list.append(text)
            print(entry)
        return empty_list

def main():
    user_input = int(input("Enter the number of entries: "))
    notes = Notebook(user_input)
    print(notes.create_entries())


main()