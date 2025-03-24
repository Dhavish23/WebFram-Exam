import unittest
from PartA import Pet, Dog  

class TestPetMethods(unittest.TestCase):
    
    # This will test if something is a Pet
    def test_is_instance_of_pet(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        self.assertIsInstance(my_pet, Pet)  # Check if it's a Pet
    
    # This will test if it is not a Dog
    def test_is_not_instance_of_dog(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        self.assertNotIsInstance(my_pet, Dog)  # Make sure it's not a Dog

    # This wil test if the two objects are the same
    def test_objects_are_identical(self):
        my_pet1 = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        my_pet2 = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        self.assertEqual(my_pet1.pet_name, my_pet2.pet_name) 
        self.assertEqual(my_pet1.pet_age, my_pet2.pet_age)    
    
    # Test when we are changing the name
    def test_change_name(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        my_pet.change_name("Bella")
        self.assertEqual(my_pet.pet_name, "Bella")  

    # Test when we are changing the age
    def test_change_age(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        my_pet.change_age(4)
        self.assertEqual(my_pet.pet_age, 4)  # Age updated?
    
    # Test when we are changing the gender
    def test_change_gender(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        my_pet.change_gender("Male")
        self.assertEqual(my_pet.pet_gender, "Male")  # Gender updated?
    
    # Test when we are changing the ID
    def test_change_id(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        my_pet.change_id("P1234")
        self.assertEqual(my_pet.pet_id, "P1234")  # ID updated?
    
    # Test when we are changing the owner
    def test_change_owner(self):
        my_pet = Pet("Milly", 6, "Female", "P1984", "Dhavish")
        my_pet.change_owner("Luke")
        self.assertEqual(my_pet.owner, "Luke")  # Owner updated?
    
    # Test when we are changing the dogs breed
    def test_change_breed(self):
        my_dog = Dog("Max", 7, "Male", "D2004", "Destiny", "Labrador", True)
        my_dog.change_breed("Beagle")
        self.assertEqual(my_dog.dog_breed, "Beagle")  

    # Test when changing the dogs training status
    def test_change_training_status(self):
        my_dog = Dog("Max", 7, "Male", "D2004", "Destiny", "Labrador", True)
        my_dog.change_training_status(False)
        self.assertEqual(my_dog.is_trained, False)  

# Run the tests
if __name__ == '__main__':
    unittest.main()
