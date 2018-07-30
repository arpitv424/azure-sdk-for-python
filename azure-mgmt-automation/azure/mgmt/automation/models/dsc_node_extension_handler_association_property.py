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


class DscNodeExtensionHandlerAssociationProperty(Model):
    """The dsc extensionHandler property associated with the node.

    :param name: Gets or sets the name of the extension handler.
    :type name: str
    :param version: Gets or sets the version of the extension handler.
    :type version: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(DscNodeExtensionHandlerAssociationProperty, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.version = kwargs.get('version', None)
