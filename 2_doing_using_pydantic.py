from pydantic import BaseModel,EmailStr, AnyUrl
from typing import List, Dict, Optional

class Patient(BaseModel):
    name: str
    email: EmailStr
    linkedin_url: AnyUrl
    age: int
    weight: float
    married: bool = False
    allergies: Optional[List[str]] = None
    contact_details: Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('inserted to datbase')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('updated to datbase')

patient_info = {'name':'Alex','email':'abc@gmail.com','linkedin_url':'https://linkedin.com/1234','age':18, 'weight': 78.9, 'contact_details':{'email':'123@gmail.com','phone':'01845674568'}}
patient1 = Patient(**patient_info)


insert_patient_data(patient1)