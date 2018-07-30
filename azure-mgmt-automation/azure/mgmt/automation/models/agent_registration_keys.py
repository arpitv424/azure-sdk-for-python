# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AgentRegistrationKeys(Model):
    """Definition of the agent registration keys.

    :param primary: Gets or sets the primary key.
    :type primary: str
    :param secondary: Gets or sets the secondary key.
    :type secondary: str
    """

    _attribute_map = {
        'primary': {'key': 'primary', 'type': 'str'},
        'secondary': {'key': 'secondary', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(AgentRegistrationKeys, self).__init__(**kwargs)
        self.primary = kwargs.get('primary', None)
        self.secondary = kwargs.get('secondary', None)
