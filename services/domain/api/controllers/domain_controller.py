from uuid import uuid4
from api.crud import CRUDDomain
from api.utils import logger
from api.exception import DomainException

logging = logger(__name__)

crud_domain = CRUDDomain()


class DomainController:
    @staticmethod
    def create_domain(request):
        request.update(dict(domain_id=str(uuid4())))
        logging.debug(f"create_domain request parameters: {request}")
        try:
            return crud_domain.create(request)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def update_domain(request: dict):
        logging.debug(f"update_domain request parameters: {request}")
        try:
            return crud_domain.update(request)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_domain(domain_id):
        logging.debug(f"get_domain request parameters: {domain_id}")
        try:
            return crud_domain.get(domain_id=domain_id)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def get_all_domains(request={}):
        logging.debug(f"get_all_domains")
        try:
            return crud_domain.get_all(**request)
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete(domain_id):
        logging.debug(f"delete request parameters: {domain_id}")
        try:
            status = crud_domain.delete(domain_id)
            response = dict(deletion_status=status, domain_id=domain_id)
            return response
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception

    @staticmethod
    def delete_all_domains():
        logging.debug(f"delete_all_domains")
        try:
            status = crud_domain.delete_all()
            response = dict(deletion_status=status)
            return response
        except DomainException as exception:
            logging.error(exception.error_log_object)
            raise exception
