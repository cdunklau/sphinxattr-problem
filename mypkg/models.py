

class SomeClass:
    """
    Some class that does a thing

    Attributes:
        id (str):
            The identifier
        workflow_state (int):
            The workflow state
        age (int):
            Age in milliseconds
        name (str):
            The name of the thing
        host (str):
            The hostname or IP address

    """
    def __init__(self, config):
        self.id = config.id
        self.workflow_state = config.workflow_state
        self.age = config.age
        self.name = config.name
        self.host = config.host
