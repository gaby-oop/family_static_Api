
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
#self=esto
#init es inicialiar ls datos del obj
class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id":self._generateId() , 
            "first_name": "John",
            "last_name": self.last_name,
            "age": 33,
            "lucky_numbers":[7, 13, 22]},
            {"id": self._generateId(),
            "first_name": "Jane Jackson",
            "last_name": self.last_name,
            "age": 35,
            "lucky_numbers": [10, 14, 3]},
            {"id": self._generateId(),
            "first_name": "Jimmy Jackson",
            "last_name": self.last_name,
            "age": 5,
            "lucky_numbers": 1}
        ]  

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    
    def add_member(self,first_name, age, lucky_numbers):
        add = {
           "id": self._generateId(), 
            "first_name": first_name,
            "last_name": self.last_name,
            "age": age,
            "lucky_numbers":lucky_numbers
        }
        self._members.append(add)
        return add

    def delete_member(self, id):
        for x in self._members:
           if x["id"] == id:
                self._members.remove(x)
        return self._members

    def get_member(self, id):
       for x in self._members:
           if x["id"] == id:
                return x
        
# this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
