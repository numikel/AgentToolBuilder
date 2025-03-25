import json

class AgentToolBuilder():
    def __init__(self, tool_name: str, tool_type: str, tool_description: str, parameters: object = None, properties_list: list[object] = None):
        self.name = tool_name
        self.type = tool_type
        self.description = tool_description
        self.parameters = None if parameters is None else parameters
        self.properties_list = [] if properties_list is None else properties_list

    def __repr__(self):
        return f"<AgentToolBuilder name={self.name} type={self.type}>"

    def build(self, return_json: bool = False):
        configuration = {
            "type": self.type,
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters or self.get_tool_parameters()
        }
        if return_json:
            configuration = json.dumps(configuration, indent=2)
        return configuration
    
    def get_tool_parameters(self, return_json: bool = False):
        parameters = {
            "type": "object",
            "properties": {k: v for d in self.properties_list for k, v in d.items()},
            "required": [k for d in self.properties_list for k in d]
        }
        if return_json:
            parameters = json.dumps(parameters, indent=2)
        return parameters
    
    def add_new_property(self, prop_name: str, prop_type: str, prop_description: str, prop_enum: list[str]=None, prop_default=None, prop_example=None):
        if prop_type not in ["string", "integer", "number", "boolean", "array", "object"]:
            raise ValueError(f"Invalid prop_type: {prop_type}")

        prop = {
            "type": prop_type,
            "description": prop_description
        }
        if prop_enum is not None:
            prop["enum"] = prop_enum
        if prop_default is not None:
            prop["default"] = prop_default
        if prop_example is not None:
            prop["example"] = prop_example
        self.properties_list.append({prop_name: prop})
        return self

