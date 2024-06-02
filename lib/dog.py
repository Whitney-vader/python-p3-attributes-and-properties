class Dog:
    APPROVED_BREEDS = ["Pug", "Husky", "Golden Retriever"]

    def __init__(self, name="Fido", breed=None):
        if not isinstance(name, str) or len(name) < 1 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            self.name = "Fido"
        else:
            self.name = name

        if breed is not None and breed not in Dog.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            self.breed = None
        elif breed is not None:
            self.breed = breed
        else:
            self.breed = "Mutt"
