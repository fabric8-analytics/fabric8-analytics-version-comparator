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
from f8a_version_comparator.string_item import StringItem
from f8a_version_comparator.list_item import ListItem
# TODO: setup logging

class IntegerItem(Item):
    """Integer Item class for maven version comparator tasks."""

    def __init__(self, str_version):
        """Initializes integer from string value of version.
        :str_value: part of version supplied as string
        """
        self.value = int(str_value)

 	def int_cmp(self, cmp_value):
 		if self.value.__lt__(cmp_value):
 			return -1
 		if self.value.__gt__(cmp_value):
 			return 1
 		return 0

    def compare_to(self, item):
        """Compare two maven versions."""
        if item == None:
        	0 if self.value==0 else 1

        if isinstance(item, IntegerItem):
        	self.int_cmp(item.value)#check if this value thing works
        if isinstance(item, StringItem):
        	return 1
        if isinstance(item, ListItem):
        	return 1
        else:
        	raise ValueError("invalid item" + type(item))

     def to_string():
     	return str(self.value)

    @classmethod
    def is_none(self):
        """Check if none."""
        if self.value is None:
        	return True
         return False
