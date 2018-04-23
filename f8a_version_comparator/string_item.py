#!/usr/bin/env python

# Copyright © 2018 Red Hat Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Class to implement methods for integer type items"""

from base import Item
from list_item import ListItem
# TODO: setup logging

class StringItem(Item):
    """String Item class for maven version comparator tasks."""
    qualifiers = ["alpha", "beta", "milestone", "rc", "snapshot", "", "sp"]
    
    aliases = {
               "ga" : "",
               "final" : "empty",
               "cr" : "rc"
    }

    release_version_index = str(qualifiers.index(""))

    def __init__(self, str_version, followed_by_digit):
        """Initializes string value of version.
        :str_value: part of version supplied as string
        """
    
        if followed_by_digit and len(str_version)==1:
            _decode_char_versions(str_version)
    
   
    def _decode_char_versions(value):
        if value.startswith("a"):
            value = "alpha"
        elif value.startswith("b"):
            value = "beta"
        elif value.startswith("m"):
            value = "meta" 

        self.value = aliases.get(value, value)

    
    @staticmethod
    def comparable_qualifier(qualifier):
        q_index = qualifiers.get(qualifier, None)
        q_index_not_found = len(qualifiers) + "-" + qualifier

        return str(q_index) if q_index is not None else q_index_not_found

    def str_cmp(self, val1, val2):
        if val2.__lt__(val1):
            return -1
        if val2.__gt__(val1):
            return 1
        return 0

    def compare_to(self, item):
        """Compare two maven versions."""
        if item is None:
            return self.str_cmp(comparable_qualifier(item), release_version_index)# check if this works

        if isinstance(item, IntegerItem):
            return -1
        if isinstance(item, StringItem):
            return self.str_cmp(comparable_qualifier(self.value), comparable_qualifier(item.value) )#need to add get item value
        if isinstance(item, ListItem):
            return -1
        else:
            raise ValueError("invalid item" + type(item))

    @classmethod
    def is_none(self):
        """Check if none."""
        if self.value is release_version_index and self.value is 0:
            return True

        return False
