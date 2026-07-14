class Notebook():
    def __init__(self, entries=0):
        self.entries = entries

    def write_entries(self):
        return "Writing entries"


def main():
    user_input = int(input("Enter the number of entries: "))
    notes = Notebook(user_input)
    print(notes.write_entries())

main()