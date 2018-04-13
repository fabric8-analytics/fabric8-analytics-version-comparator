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

from f8a_version_comparator.item import Item
# TODO: setup logging

class StringItem(Item):
    """String Item class for maven version comparator tasks."""
    qualifiers = ["alpha", "beta", "milestone", "rc", "snapshot", "", "sp"]
    release_version_index = str(qualifiers.index(""))
    aliases = {
               "ga" : "",
               "final" : "empty",
               "cr" : "rc"
    }

    def __init__(self, str_version, followed_by_digit):
        """Initializes string value of version.
        :str_value: part of version supplied as string
        """
        if followed_by_digit and len(str_version)==1:
            _decode_char_versions(str_version)
        
    _decode_char_versions(value):
        if value.startswith("a"):
            value = "alpha"
        elif value.startswith("b"):
            value = "beta"
        elif value.startswith("m"):
            value = "meta" 

        self.value = aliases.get(value, value)

    @staticmethod
    def comparableQualifier(qualifier):
        q_index = qualifiers.index(qualifier)
        q_index_not_found = len(qualifiers) + "-" + qualifier

        return str(q_index) if q_index is not -1 else q_index_not_found

    @classmethod
    def compare_to(cls, self, ):
        """Compare two maven versions."""
        raise NotImplementedError()

    @classmethod
    def is_none(self):
        """Check if none."""
        if self.value is 0:
            return True

        return False
