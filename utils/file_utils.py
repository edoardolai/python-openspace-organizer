from .table import Table
from .openspace import Openspace
import math;


def distribute_evenly(unseated, max_c):
        tables = []
        nb_new_tables = math.floor(unseated / max_c)
        for table in range(nb_new_tables):
            tables.append(Table(max_c))
        return tables
        

def arrange_new_tables(unseated: int, max_capacity: int, min_capacity: int, iteration_count = 0):
    if unseated <= max_capacity or max_capacity == min_capacity:
        return distribute_evenly(unseated, max_capacity)
    else:
        _max = max_capacity
        while unseated % _max < min_capacity:
            _max -= 1
            if unseated % _max == 0:
                break
        extra_tables = []
        new_tables = distribute_evenly(unseated, _max)
        extra_tables.extend(new_tables)
        remaining_people = unseated % _max
        if remaining_people == 0:
            return extra_tables
        elif remaining_people > 1:
            extra_tables.append(Table(remaining_people))
            return extra_tables
        
def display_openspace_info(openspace: Openspace):
    while True:
        info_option = int(input("Select an option of the info you want to know about: \n"
                            "1 - Total People \n"
                            "2 - Number of Tables \n"
                            "3 - People Unseated \n"
                            "4 - Dispaly current room disposition \n"
                            "Or press any other key to continue: "))
        
        match info_option:
            case(1):
                total_people = sum(openspace.disposition_as_csv.count()) 
                print(f"Total People: {total_people}")
            case(2):
                number_of_tables = len(openspace.tables)  
                print(f"Number of Tables: {number_of_tables}")
            case(3):
                unseated_people = openspace.people_standing if openspace.people_standing is not (None or []) else "Everybody found a seat" 
                print(f"People Unseated: {unseated_people}")
            case(4):
               openspace.display()
            case _:
                print("Exiting information display.")
                break  