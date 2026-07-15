from pathlib import Path
import json

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
        pick = int(input(f"Choose entry(#1 - {len(self.__list)}): "))
        view = self.__list[pick - 1]
        print(view)

    def add_more_entries(self):
        user_input = int(input("Enter the number of additional entries: "))
        for entry in range(1, user_input + 1):
            print(f"Write for entry #{len(self.__list) + 1}")
            text = input("")
            self.__list.append(text)
        return self.__list
    
    def store_entries(self):
        path = Path("entries.json")
        contents = json.dumps(self.__list)
        path.write_text(contents)

def main():
    user_input = int(input("Enter the number of entries: "))
    notes = Notebook(user_input)
    notes.create_entries()

    opt_user = input("Add more entries?(y/n): ")
    notes.add_more_entries()

    opt_user = input("View entries?(y/n): ")
    notes.view_entries()

    opt_user = input("Store entries?(y/n): ")
    notes.store_entries()



main()