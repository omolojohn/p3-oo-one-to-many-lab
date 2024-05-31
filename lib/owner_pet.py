class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
    
    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet argument must be of type Pet")
        pet.owner = self
        self._pets.append(pet)
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner is not None:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be of type Owner")
            owner.add_pet(self)
        Pet.all.append(self)
