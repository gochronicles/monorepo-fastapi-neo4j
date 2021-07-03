from pydantic import BaseModel


class Patient(BaseModel):
    name: str
    status: bool = False
    classified: bool = False


class PatientUpdate(BaseModel):
    patient_id: str
    name: str
    status: bool = False
    classified: bool = False
