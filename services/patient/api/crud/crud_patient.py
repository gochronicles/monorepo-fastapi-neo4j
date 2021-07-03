from py2neo import NodeMatcher
from py2neo import Node
from api.schemas import PatientUpdate
from api.database import graph
from api.utils import logger


logging = logger(__name__)


class CRUDPatient:
    def __init__(self):
        self.node_matcher = NodeMatcher(graph)

    def get(self, **props):
        node = self.node_matcher.match("Patient", **props).first()
        if node is not None:
            return dict(node.items())
        else:
            return []

    def get_all(self, **props):
        nodes = self.node_matcher.match("Patient", **props).all()
        if nodes is not None:
            return [dict(node.items()) for node in nodes]
        else:
            return []

    def create(self, patient: PatientUpdate):
        props = PatientUpdate.validate(patient).dict()
        patient_id = props.get("patient_id")
        node = self.node_matcher.match("Patient", patient_id=patient_id).first()
        if not node:
            node = Node("Patient", **props)
            graph.create(node)
            logging.debug("Node created!")
        else:
            logging.debug("patient_id has to be unique!")
        return patient_id

    def update(self, patient: PatientUpdate):
        props = PatientUpdate.validate(patient).dict()
        patient_id = props.get("patient_id")
        node = self.node_matcher.match("Patient", patient_id=patient_id).first()
        if node:
            node.update(**props)
            graph.push(node)
        else:
            logging.debug("Node does not exist!")
        return patient_id

    def delete(self, patient_id: str):
        node = self.node_matcher.match("Patient", patient_id=patient_id).first()
        if node:
            graph.delete(node)
            return True
        else:
            logging.debug("Node does not exist!")
            return False

    def delete_all(self):
        graph.run("MATCH (p:Patient) DETACH DELETE p")
        logging.debug("All nodes for Patient type deleted!")
        return True
