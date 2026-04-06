def insert_patient_data(name: str,age: int):
    if type(name)==str and type(age)==int:
        if age < 0:
            raise ValueError('Age can not be negative')
        else:
            print(name)
            print(age)
            print('Inserted into database')
    else:
        raise TypeError('Incorrect Data Type')
    


insert_patient_data('alex',10)