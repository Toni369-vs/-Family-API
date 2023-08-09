
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        self._members = [
             {
            "id": 1,
            "first_name": "John",
            "last_name": last_name,
            "age": 33 ,
            "lucky_numbers":[7, 13, 22],
            },
            {
            "id": 2,
            "first_name": "Jane",
            "last_name": last_name,
            "age": 35,
            "lucky_numbers":[10, 14, 3],
            },
            {
            "id": 3,
            "first_name": "Jimmy",
            "last_name": last_name,
            "age": 5 ,
            "lucky_numbers":[1],
            }
        ]

    def _generateId(self):
        return randint(0, 99999999)

#----------------método POST----------------------

    def add_member(self, member):
       
        for person in self._members:
            if(member["id"] == person["id"]):
               member["id"] = self._generateId() 
        
        
        member["last_name"] = self.last_name
        self._members.append(member)

        return True        
     
#----------------métodos GET----------------------

# método para devolver todos los miembros de la familia

    def get_all_members(self):
        return self._members

# método para devolver un miembro por id
    def get_member(self, id): 
        for member in self._members:
            if (member["id"] == id):
                return member
        return "No existe miembro"

#----------------método DELETE----------------------

    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return True