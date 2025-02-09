class Product:
    def __init__(self,id,name,category,breed,price,nutrition):
        self.id = (id)
        self.name = str(name)
        self.category = str(category)
        self.breed = breed
        self.price = price
        self.nutrition = nutrition
pet_1 =Product("68737", "Cat","pet","Siamese","3000p","carnivorous")
pet_2 = Product("68738", "Dog","pet","Dachshund","3500p","carnivorous")
pet_3 =Product("68739", "fish","pet","Gold","500p","herbivorus")
pet_4 = Product("68740", "hamster","pet","Jungarik","700p","herbivorus")
a= [pet_1.id,pet_1.name,pet_1.category,pet_1.breed,pet_1.price,pet_1.nutrition,
pet_2.id,pet_2.name,pet_2.category,pet_2.breed,pet_2.price,pet_2.nutrition,
pet_3.id,pet_3.name,pet_3.category,pet_3.breed,pet_3.price,pet_3.nutrition,
pet_4.id,pet_4.name,pet_4.category,pet_4.breed,pet_4.price,pet_4.nutrition]

print(a)