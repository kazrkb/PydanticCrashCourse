from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, model_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_address: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight/(self.height**2),2)
        return bmi




def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.contact_address)
    print(patient.bmi)

patient_info = {
    'name': 'Alex',
    'email': '123@gmail.com',
    'age': '90',
    'weight': 78.9,
    'height': 1.5,
    'married': False,
    'allergies': ['dust', 'pollen'],
    'contact_address': {'emergency': '01845674568'}
}
patient1 = Patient(**patient_info)
update_patient_data(patient1)


