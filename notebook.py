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
            print()
            text = input("")
            print()
            self.__list.append(text)
        return self.__list
    
    def view_entries(self):
        """View created entries"""
        print()
        try:
            pick = int(input(f"Choose entry(#1 - {len(self.__list)}): "))
            if pick <= 0:
                raise IndexError
            else:
                view = self.__list[pick - 1]
        except ValueError, IndexError:
            print()
            print("Invalid Option")
        else:
            print()
            print(view)

    def add_more_entries(self):
        """Adds more entries"""
        try:
            print()
            user_input = int(input("Enter the number of additional entries: "))
        except ValueError:
            print()
            print("Invalid Option")
        else:
            print()
            for entry in range(1, user_input + 1):
                print(f"Write for entry #{len(self.__list) + 1}")
                print()
                text = input("")
                print()
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
        try:
            if path.exists():
                contents = path.read_text()
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("File not found.")
        else:
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
    notes = Notebook()
    print()
    print("---Notebook---")
    print()

    if notes.file_exist():
        cont = True
        while cont:
            user_input = input("A file was found! Open these entries?(y/n) ")
            print()
            if user_input == "y":
                cont = False
                notes.read_stored_entries()
                notes.view_entries()
                while True:
                    print()
                    user_input = input("View another?(y/n) ")
                    if user_input == "y":
                        notes.view_entries()
                        continue
                    elif user_input == "n":
                        print()
                        break
                    else:
                        print()
                        print("Invalid Option")
            elif user_input == "n":
                cont = False
            else:
                print("Invalid Option")
                print()
    cont = True
    while cont:
        user_input = input("Create entries?(y/n) ")
        print()
        if user_input == "y":
            try:
                user_input = int(input("Enter the number of entries: "))
                print()
            except ValueError:
                print()
                print("Invalid Option")
                print()
            else:
                if user_input <= 0:
                    print("Invalid Option")
                    print()
                else:
                    notes = Notebook(user_input)
                    notes.create_entries()
                    while cont:
                        opt_user = input("Add more entries?(y/n): ")
                        if opt_user == "y":
                            notes.add_more_entries()
                        elif opt_user == "n":
                            cont = False
                        else:
                            print()
                            print("Invalid Option")
                    cont = True
                    while cont:
                        print()
                        opt_user = input("View entries?(y/n): ")
                        if opt_user == "y":
                            notes.view_entries()
                        elif opt_user == "n":
                            print()
                            cont = False
                        else:
                            print()
                            print("Invalid Option")

                    cont = True
                    while cont:
                        opt_user = input("Store entries?(y/n) ")
                        if opt_user == "y":
                            print()
                            notes.store_entries()
                            print("Entries have been successfully stored!")
                            cont = False
                        elif opt_user == "n":
                            cont = False
                        else:
                            print()
                            print("Invalid Option")
                            print()

                    break
        elif user_input == "n":
            cont = False
        else:
            print("Invalid Option")
            print()

    print()
    print("---End of Program---")



if __name__ == "__main__":
    main()