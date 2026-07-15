from pathlib import Path
import json

class Notebook():
    """
    Creates a notebook with the number of entries chosen by user

        Arg:
        entries (default is 0)
    """
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
        """View created entries"""
        pick = int(input(f"Choose entry(#1 - {len(self.__list)}): "))
        view = self.__list[pick - 1]
        print(view)

    def add_more_entries(self):
        """Adds more entries"""
        user_input = int(input("Enter the number of additional entries: "))
        for entry in range(1, user_input + 1):
            print(f"Write for entry #{len(self.__list) + 1}")
            text = input("")
            self.__list.append(text)
        return self.__list
    
    def store_entries(self):
        """Stores created entries in a json file (entries.json)"""
        path = Path("entries.json")
        contents = json.dumps(self.__list)
        path.write_text(contents)

    def read_stored_entries(self):
        """Reads the stroed file"""
        path = Path("entries.json")
        contents = path.read_text()
        self.__list = json.loads(contents)
        return self.__list

    def file_exist(self):
        """Checks to see if stored file exists"""
        path = Path("entries.json")
        if path.exists() == True:
            return True
        else:
            return False

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

    opt_user = input("View stored entries?(y/n): ")
    notes.read_stored_entries()



main()