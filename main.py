from utils.table import Table;
from utils.openspace import Openspace;
from utils.file_utils import arrange_new_tables,display_openspace_info
import os
import pandas as pd;
import time;
from random import shuffle;


def get_file_path():
        while True:
            file_path = input('Please provide a file path: ')
            if os.path.exists(file_path):
                return file_path
            print("File does not exist. Please enter a valid file path.")

def load_names(file_path):
    while True:
        sheet = pd.read_excel(file_path)
        column_name = input("Please specify the column name names extraction: ")
        if column_name not in sheet.columns:
            print(f"Column '{column_name}' does not exist in the provided file.")
        else:
            break
    return list(pd.DataFrame(sheet)['Students'])

def get_table_configuration():
    nb_tables = int(input('Please specify number of tables: '))
    tb_capacity = int(input('Please specify the table capacity: '))
    return nb_tables, tb_capacity

def create_tables(nb_tables, tb_capacity):
    return [Table(tb_capacity) for _ in range(nb_tables)]

def display_remaining_people(open_space):
    remaining = open_space.people_standing
    print(f"There is a total of: {len(remaining)} left unseated")
    return remaining

def handle_arrangement(open_space, remaining):
    continue_arrangement = input("Would you like to add more tables to find them a seat? type: Yes / No ")
    
    if continue_arrangement.lower() == 'no':
        print("Final disposition: ")
        return None

    max_c_input = int(input("Please specify a maximum capacity for the new tables: "))
    
    min_c_input = get_minimum_capacity()
    
    print("I am trying to find the optimal seating arrangement, please be aware that the capacity values might be overridden to avoid having people sitting alone.")
    time.sleep(4)
    
    extra_tables = arrange_new_tables(len(remaining), max_c_input, min_c_input)
    open_space.organize(remaining, extra_tables)
    print("New tables added:")
    open_space.display()
    return continue_arrangement

def get_minimum_capacity():
    while True:
        min_c_input = int(input("Please specify a minimum capacity for the new tables: "))
        if min_c_input >= 2:
            return min_c_input
        print("We cannot have one person table")

def export_configuration(open_space, continue_arrangement):
    if continue_arrangement.lower() == 'yes':
        export_file_name = input("Please provide a file name: ")
        open_space.store(export_file_name)

def main():
    file_path = get_file_path()
    names = load_names(file_path)
    print(f'There is a total of {len(names)} people to be seated')
    
    nb_tables, tb_capacity = get_table_configuration()
    tables = create_tables(nb_tables, tb_capacity)
    
    open_space = Openspace(nb_tables, tables, names)
    remaining = open_space.people_standing
    print("People have been seated")
    
    open_space.display()
    display_remaining_people(open_space)
    
    continue_arrangement = handle_arrangement(open_space, remaining)
    display_openspace_info(open_space)
    
    export_configuration(open_space, continue_arrangement)

    print("Bye!")

if __name__ == "__main__":
    main()




