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
from f8a_version_comparator.integer_item import IntegerItem
from f8a_version_comparator.string_item import StringItem
# TODO: setup logging

class ListItem(Item):
    """String Item class for maven version comparator tasks."""


    def __init__(self):
        """Initializes string value of version.
        :str_value: part of version supplied as string
        """
        self.arraylist = list()
    
   
    def normalize():
        i = len(self.arraylist)
        while(i>=0):
            lastItem = self.arraylist[i]
            if lastItem is None:
                self.arraylist.pop(i)
            elif(!isinstance(lastItem)):
                break
            i-=1


    def compare_to(self, item):
        """Compare two maven versions."""
        if item is None:
            if len(self.arraylist)==0:
                return 0
            first = self,arraylist[0]
            return first.compareTo(None)

        if isinstance(item, IntegerItem):
            return -1
        if isinstance(item, StringItem):
            return 1
        if isinstance(item, ListItem):
            left_iter = iter(self.arraylist)
            right_iter = iter(item.arraylist)

            while(True):
                l = next(left_iter, None)
                r = next(right_iter, None)
                if l is None and r is None:
                    break
                result = 0 
                if l is None:
                    if r is None:
                        result = 0 
                    else:
                        -1 * r.compare_to(l)
                else:
                    l.compare_to(r)
                if result is not 0:
                    retirn result

            return 0 
        else:
            raise ValueError("invalid item" + type(item))

    def to_string():
        # To implement

    @classmethod
    def is_none(self):
        """Check if none."""
        if len(self.arraylist) is o:
            return True

        return False
