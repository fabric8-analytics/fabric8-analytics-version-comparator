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
# TODO: setup logging

class IntegerItem(Item):
    """Integer Item class for maven version comparator tasks."""

    def __init__(self, str_version):
        """Initializes integer from string value of version.
        :str_value: part of version supplied as string
        """
        self.value = int(str_version)

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

    def to_string(self):
        return str(self.value)

    @classmethod
    def is_none(self):
        """Check if none."""
        if self.value is None:
            return True
        return False


class StringItem(Item):
    """String Item class for maven version comparator tasks."""  

    def __init__(self, str_version, followed_by_digit):
        """Initializes string value of version.
        :str_value: part of version supplied as string
        """

        self.qualifiers = ["alpha", "beta", "milestone", "rc", "snapshot", "", "sp"]
    
        self.aliases = {
               "ga" : "",
               "final" : "empty",
               "cr" : "rc"
        }

        self.release_version_index = str(self.qualifiers.index(""))
        self._decode_char_versions(str_version, followed_by_digit)
        
   
    def _decode_char_versions(self, value, followed_by_digit):
        if followed_by_digit and len(str_version)==1:
            if value.startswith("a"):
                value = "alpha"
            elif value.startswith("b"):
                value = "beta"
            elif value.startswith("m"):
                value = "meta" 

        self.value = self.aliases.get(value, value)

    
    @staticmethod
    def comparable_qualifier(qualifier):
        q_index = self.qualifiers.get(qualifier, None)
        q_index_not_found = len(self.qualifiers) + "-" + qualifier

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

    def to_string(self):
        return str(self.value)

    @classmethod
    def is_none(self):
        """Check if none."""
        if self.value is release_version_index and self.value is 0:
            return True

        return False


class ListItem(Item):
    """String Item class for maven version comparator tasks."""

    def __init__(self):
        """Initializes string value of version.
        :str_value: part of version supplied as string
        """  
        self.array_list = list()

    def add_item(self, item):
        arr_list = self.array_list
        arr_list.append(item)

    def get_list(self):
        return self.array_list

    def normalize(self):
        i = len(self.arraylist)
        while(i>=0):
            lastItem = self.arraylist[i]
            if lastItem is None:
                self.arraylist.pop(i)
            elif( not isinstance(lastItem)):
                break
            i-=1


    def compare_to(self, item):
        """Compare two maven versions."""
        import pdb
        pdb.set_trace()
        if item is None:
            if len(self.array_list)==0:
                return 0
            first = self.array_list[0]
            return first.compareTo(None)

        if isinstance(item, IntegerItem):
            return -1
        if isinstance(item, StringItem):
            return 1
        if isinstance(item, ListItem):
            left_iter = iter(self.arraylist)
            right_iter = iter(item.get_list())

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
                    return result

            return 0 
        else:
            raise ValueError("invalid item" + type(item))

    def to_string():
        # To implement
        pass

    @classmethod
    def is_none(self):
        """Check if none."""
        if len(self.arraylist) is o:
            return True

        return False

