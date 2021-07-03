from py2neo import NodeMatcher
from py2neo import Node
from api.schemas import DomainUpdate
from api.database import graph
from api.utils import logger


logging = logger(__name__)


class CRUDDomain:
    def __init__(self):
        self.node_matcher = NodeMatcher(graph)

    def get(self, **props):
        node = self.node_matcher.match("Domain", **props).first()
        if node is not None:
            return dict(node.items())
        else:
            return []

    def get_all(self, **props):
        nodes = self.node_matcher.match("Domain", **props).all()
        if nodes is not None:
            return [dict(node.items()) for node in nodes]
        else:
            return []

    def create(self, domain: DomainUpdate):
        props = DomainUpdate.validate(domain).dict()
        domain_id = props.get("domain_id")
        node = self.node_matcher.match("Domain", domain_id=domain_id).first()
        if not node:
            node = Node("Domain", **props)
            graph.create(node)
            logging.debug("Node created!")
        else:
            logging.debug("domain_id has to be unique!")
        return domain_id

    def update(self, domain: DomainUpdate):
        props = DomainUpdate.validate(domain).dict()
        domain_id = props.get("domain_id")
        node = self.node_matcher.match("Domain", domain_id=domain_id).first()
        if node:
            node.update(**props)
            graph.push(node)
        else:
            logging.debug("Node does not exist!")
        return domain_id

    def delete(self, domain_id: str):
        node = self.node_matcher.match("Domain", domain_id=domain_id).first()
        if node:
            graph.delete(node)
            return True
        else:
            logging.debug("Node does not exist!")
            return False

    def delete_all(self):
        graph.run("MATCH (p:Domain) DETACH DELETE p")
        logging.debug("All nodes for Domain type deleted!")
        return True
