from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_address: Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['iub.edu.bd','du.edu.bd']
        #123@iub.edu.bd [-1] = iub.edu.bd 
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('not a valid domain')
        return value 
    
    @field_validator('name')
    @classmethod
    def name_uppercase(cls,value):
        return value.upper()


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.contact_address)

patient_info = {
    'name': 'Alex',
    'email': 'abc@iub.edu.bd',
    'age': 18,
    'weight': 78.9,
    'married': False,  # or True
    'allergies': None,
    'contact_address': {'phone': '01845674568'}
}
patient1 = Patient(**patient_info)
update_patient_data(patient1)