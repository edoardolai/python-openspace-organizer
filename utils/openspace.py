from .table import Table;
from typing import List;
import pandas as pd;

class Openspace:
    def  __init__(self, number_of_tables: int, tables: List[Table], people : List[str] = None):
        self.people = people if people is not None else [];
        self.tables = tables;
        self.number_of_tables = number_of_tables;
        self.initial_setup = not len(tables[0].seats)
        self.disposition_as_csv = None
        self.people_standing = None
        
        if self.initial_setup:
            self.organize(people)

    
    def __str__(self):
        return "An Openspace constr(number_of_people: int , tables: List[Table], people: List[Str])" 

    def organize(self, names: List[str], new_tables : List[Table] = None):
        if new_tables == None:
            tables_df = self.assign_seats(names, self.tables)
            self.disposition_as_csv = tables_df
        else:
            tables_df = self.assign_seats(names, new_tables)
            self.disposition_as_csv = pd.concat([self.disposition_as_csv, tables_df], axis=1)
            self.tables.extend(new_tables)

    def assign_seats(self, names: List[str], tables: List[Table]):
        count = 0;
        for table in tables:
            while table.has_free_spot():
                table.assign_seat(names[count])
                count+=1
        room_setup = [[student.occupant for student in table.seats] for table in tables]
        table_names = [table.id for table in tables]
        tables_df = pd.DataFrame(room_setup).T
        tables_df.columns = table_names
        self.people_standing = names[(count) : len(names)] if len(names) else None;
        return tables_df

                        
    
    def display(self):
        print(self.disposition_as_csv)

    def store(self, file_name: str):
        self.disposition_as_csv.to_csv(file_name)