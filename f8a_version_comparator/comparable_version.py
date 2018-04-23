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

from integer_item import IntegerItem
from string_item import StringItem
from list_item import ListItem

class ComparableVersion():

    def __init__(self, version):
        self.items = list()
        self.parse_version(version)
       

    def parse_version(self, version):

        parse_stack = list()
        version = version.lower()
        ref_list = list()

        parse_stack.append(ref_list)


        _is_digit = False

        _start_index = 0

        for _ch in range(0, len(version)):

            ver_char = version[_ch]

            if ver_char is ".":

                if _ch==_start_index:
                    ref_list.append(0)
                else:
                    ref_list.append(self.parse_item(_is_digit, version[_start_index : _ch]))

                _start_index = _ch + 1

            elif ver_char=="-":
                if _ch==_start_index:
                    ref_list.append(0)
                else:
                    ref_list.append(self.parse_item(_is_digit, version[_start_index : _ch]))

                _start_index = _ch + 1 
                self.items.append(ref_list)
                ref_list = list()
                parse_stack.append(ref_list)

            elif ver_char.isdigit():
                if not _is_digit and _ch > _start_index:
                    ref_list.add(StringItem(version[_start_index: i ], True))
                    _start_index = _ch

                    self.items.append(ref_list)
                    ref_list = list()
                    parse_stack.append(ref_list)
                _is_digit = True
            else:
                if _is_digit and _ch > _start_index:
                    ref_list.append(self.parse_item(True, version[_start_index:i]))
                    _start_index = i
                    self.items.append(ref_list)
                    ref_list = list()
                    parse_stack.append(ref_list)
                _is_digit = False

        if len(version) > _start_index:
            ref_list.append(self.parse_item(_is_digit, version[_start_index]))

        # implement list normalization
        while len(parse_stack)>0:
            break

        print(self.items)

    def parse_item(self, _is_digit, buf):
        if _is_digit:
            return IntegerItem(buf)

        return StringItem(buf, false)

    def compare_to(obj):

        # 
        pass

if __name__ == "__main__":

    c = ComparableVersion("1-11-1")
      