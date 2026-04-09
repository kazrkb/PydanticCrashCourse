from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zipcode: int

class Patient(BaseModel):
    name: str
    gender: str = 'Male'
    age: int
    address: Address


address_dict = {
    'city': 'Lakshmipur',
    'state': 'Chottogram',
    'zipcode': 1200
}
address1 = Address(**address_dict)

patient_dict = {
    'name': 'Rakib',
    'age': 25,
    'address': address1
}

patient1 = Patient(**patient_dict)

# temp = patient1.model_dump(include=['name','age'])
# temp = patient1.model_dump(exclude={'address':['state']})
temp = patient1.model_dump(exclude_unset=True)
print(temp)
print(type(temp))

