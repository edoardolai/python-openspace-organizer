from typing import List;

class Seat:
    def __init__(self, free: bool, occupant: str | None):
        self.free = free;
        self.occupant = occupant;

    def __str__(self) -> str:
        return "A Seat object, constr(free: bool, occupant: str"
    
    def set_occupant(self,name:str):
        if self.free:
            self.occupant = name
    
    def remove_occupant(self)->str:
        prev = self.occupant
        self.occupant = None
        return prev

class Table:
    object_counter = 0;
    def __init__(self, capacity: int, seats:List[Seat] = None):
        self.capacity = capacity;
        self.seats = seats if seats is not None else []
        self.id = f"Table_{Table.object_counter}"
        Table.object_counter+=1

    def __str__(self):
        return "A table object, constr(capacity: int seats: List[Seat])"
    
    def assign_seat(self, name:str):
        if self.has_free_spot():
            self.seats.append(Seat(False, name))
    
    def has_free_spot(self)->bool:
        return self.left_capacity() > 0;

    def left_capacity(self) -> int:
        return self.capacity - len(self.seats);
        


seat = Seat(False, "Bob")
table = Table(2, [seat])

print(table)