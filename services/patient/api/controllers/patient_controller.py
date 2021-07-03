from uuid import uuid4
from api.crud import CRUDPatient
from api.utils import logger
from api.exception import PatientException

logging = logger(__name__)

crud_patient = CRUDPatient()


class PatientController:
    @staticmethod
    def create_patient(request):
        request.update(dict(patient_id=str(uuid4())))
        logging.debug(f"create_patient request parameters: {request}")
        try:
            return crud_patient.create(request)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def update_patient(request: dict):
        logging.debug(f"update_patient request parameters: {request}")
        try:
            return crud_patient.update(request)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_patient(patient_id):
        logging.debug(f"get_patient request parameters: {patient_id}")
        try:
            return crud_patient.get(patient_id=patient_id)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_all_patients(request={}):
        logging.debug(f"get_all_patients")
        try:
            return crud_patient.get_all(**request)
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete(patient_id):
        logging.debug(f"delete request parameters: {patient_id}")
        try:
            status = crud_patient.delete(patient_id)
            response = dict(deletion_status=status, patient_id=patient_id)
            return response
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete_all_patients():
        logging.debug(f"delete_all_patients")
        try:
            status = crud_patient.delete_all()
            response = dict(deletion_status=status)
            return response
        except PatientException as exception:
            logging.error(exception.error_log_object)
            raise exception
