class Notebook():
    def __init__(self, entries=0):
        self.entries = entries
        self.__list = []

    def create_entries(self):
        """Creates entries for a notebook"""
        for entry in range(1, self.entries + 1):
            print(f"Write for entry #{entry}")
            text = input("")
            self.__list.append(text)
        return self.__list
    
    def view_entries(self):
        pick = int(input(f"Choose entry(#1 - {len(self.__list)})"))
        view = self.__list[pick - 1]
        print(view)

def main():
    user_input = int(input("Enter the number of entries: "))
    notes = Notebook(user_input)
    notes.create_entries()
    opt_user = input("View entries?(y/n): ")
    notes.view_entries()


main()