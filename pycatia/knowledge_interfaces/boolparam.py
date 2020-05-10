#! /usr/bin/python3.7
from pycatia.knowledge_interfaces.parameter import Parameter


class BoolParam(Parameter):
    def __init__(self, name=None, value=None, parameter=None, parent=None):
        if value and not isinstance(value, bool):
            raise ValueError(f'Parameter value [{value}] has to be bool()')

        self.parameters = self.set_parameters(parent)

        if parameter:
            self.parameter = parameter
        else:
            self.parameter = Parameter(self.parameters.CreateBoolean(name, value))

    def set_parameters(self, parent):
        try:
            # if parent is <class "Parameters">S
            return parent.parameters
        except AttributeError:
            # if parent is something like Catia.ActiveDocument.Part.ParametersS
            return parent