
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

        # example list of members
        self._members = [
            {
                "id": 1,
                "first_name": "John",
                "last_name": self.last_name,
                "age": 33,
                "lucky_number": [7, 13, 22],
            },
            {
                "id": 2,
                "first_name": "Jane",
                "last_name": self.last_name,
                "age": 34,
                "lucky_numbers": [10, 14, 3],
            },
            {
                "id": 3,
                "first_name": "Jimmy",
                "last_name": self.last_name,
                "age": 5,
                "lucky_numbers": [1],
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        self._members.append(member)
        
        pass

    def delete_member(self, id):
        # fill this method and update the return
        member = next((m for m in self._members if m['id'] == id), None)
        if member:
            self._members.remove(member)
            return {'done': True}
        else:
            return {'done': False, 'message': 'Member not found'}, 404
        pass

    def get_member(self, id):
        # fill this method and update the return
        for m in self._members:
            if m['id'] == int(id):
                return m
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
