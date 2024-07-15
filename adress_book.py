from collections import UserDict
from record import Record
from prettytable import PrettyTable




class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.data = {}

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return next((record for record in self.data.values() if record.name.value == name), None)

    def delete(self, name: str):
        if name in self.data.keys():
            del self.data[name]

    def __str__(self):
        result = ''
        result += f'AddressBook with {len(self.data)} records \n'

        return result
