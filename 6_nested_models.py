from pydantic import BaseModel

class Address(BaseModel):
    city: str
    state: str
    zipcode: int

class Patient(BaseModel):
    name: str
    gender: str
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
    'gender': 'Male',
    'age': 25,
    'address': address1
}

patient1 = Patient(**patient_dict)
print(patient1.address.city)