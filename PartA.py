class Pet:
    # This  it sets up the pet's info when you make one
    def __init__(my, pet_name, pet_age, pet_gender, pet_id, owner):
        my.pet_name = pet_name  # Mty pets anme 
        my.pet_age = pet_age  # How old my pet is
        my.pet_gender = pet_gender  # The gender of the pet 
        my.pet_id = pet_id  # Pet with a ID
        my.owner = owner  # The person who owns the pet
    
    # This shows all the pet's information like name, age gender and the id 
    def show_info(my):
        print(f"Name: {my.pet_name}, Age: {my.pet_age}, Gender: {my.pet_gender}, ID: {my.pet_id}, Owner: {my.owner}")
    
    # This changes the pet's name to something new 
    def change_name(my, new_name):
        if isinstance(new_name, str):  # This is going to check if the new name is a string 
            my.pet_name = new_name
        else:
            print("Invalid name")  # If it's not text, how an error will show up
    
    # This changes how old the pet is
    def change_age(my, new_age):
        if isinstance(new_age, int):  # Check if the new age is a number
            my.pet_age = new_age
        else:
            print("Invalid age")  # If it's not a number, show an error will show up 
    
    # This changes the pet's gender
    def change_gender(my, new_gender):
        if isinstance(new_gender, str):  # Check if the new gender is text
            my.pet_gender = new_gender
        else:
            print("Invalid gender")  # If it's not text, how an error will show up
    
    # This changes the pet's ID
    def change_id(my, new_id):
        if isinstance(new_id, str):  # Check if the new ID is text
            my.pet_id = new_id
        else:
            print("Invalid  pet ID")  # If it's not text, how an error will show up
    
    # This changes the owner's name
    def change_owner(my, new_owner):
        if isinstance(new_owner, str):  # Check if the new owner name is text 
            my.owner = new_owner
        else:
            print("Invalid  owner name")  # If it's not text, how an error will show up

      # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #       

# This is a class for dogs
class Dog(Pet):
    # This is the init thingy for dogs, it adds breed and trained stuff
    def __init__(my, pet_name, pet_age, pet_gender, pet_id, owner, dog_breed, is_trained):
        super().__init__(pet_name, pet_age, pet_gender, pet_id, owner) 
        my.dog_breed = dog_breed  # whatis the dogs breed
        my.is_trained = is_trained  # True if the dog is trained, False if it's not
    
    # This shows all the dog's info, including breed and trained status
    def show_info(my):
        super().show_info()  # Show the pet infomation
        print(f"Breed: {my.dog_breed}, Trained: {my.is_trained}")
    
    # This changes the dog's breed
    def change_breed(my, new_breed):
        if isinstance(new_breed, str):  
            my.dog_breed = new_breed
        else:
            print("Invalid the breed")  
    
    # This changes if the dog is trained or not
    def change_training_status(my, new_status):
        if isinstance(new_status, bool): 
            my.is_trained = new_status
        else:
            print("Invalid for training")  

# Making a pet object 
pet1 = Pet("Milly", 6, "Female", "P1984", "Dhavish")  
# Making a dog object
dog1 = Dog("Max", 7, "Male", "D2004", "Destiny", "Labrador", True)  

# Showing their information
pet1.show_info()  # Show Milly infomation
dog1.show_info()  # Show Max's information 

# Changing  the age 
pet1.change_age(4)  # Milly is now 4 years old
dog1.change_training_status(False)  # Max is not trained anymore :(

# Showing the updated info
print("\nAfter updates:")
pet1.show_info()  # Show Millys updated infomation
dog1.show_info()  # Show Max's updated infomation
