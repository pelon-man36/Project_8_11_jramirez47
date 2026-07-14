class Notebook():
    def __init__(self, entries=0):
        self.entries = entries

    def ask_user(self):
        user_input = int(input("Enter the number of entries: "))
        self.entries = user_input
        return self.entries

ask = Notebook(0)
print(ask.ask_user())