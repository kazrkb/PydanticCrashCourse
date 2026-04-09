from pydantic import BaseModel,EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str,Field(max_length=50, title='Name of the patient', description='Give patient name under 50 chars', examples=['Rakib','Nayeem'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0,strict=True)]
    married: Annotated[bool, Field(default=None)]
    allergies: Optional[List[str]] = Field(default=None,max_length=5)
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