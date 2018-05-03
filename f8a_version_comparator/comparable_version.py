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

from .item_object import IntegerItem
from .item_object import StringItem
from .item_object import ListItem


class ComparableVersion():

    def __init__(self, version):

        self.parse_version(version)

    def parse_version(self, version):
        parse_stack = list()
        version = version.lower()
        ref_list = ListItem()
        self.items = ref_list
        _is_digit = False

        _start_index = 0

        for _ch in range(0, len(version)):

            ver_char = version[_ch]

            if ver_char is ".":

                if _ch == _start_index:
                    ref_list.add_item(0)
                else:
                    ref_list.add_item(self.parse_item(_is_digit, version[_start_index: _ch]))

                _start_index = _ch + 1

            elif ver_char == "-":
                if _ch == _start_index:
                    ref_list.add_item(0)
                else:
                    ref_list.add_item(self.parse_item(_is_digit, version[_start_index: _ch]))
                _start_index = _ch + 1

                temp = ListItem()
                ref_list.add_item(temp)
                ref_list = temp
            elif ver_char.isdigit():
                if not _is_digit and _ch > _start_index:
                    ref_list.add_item(StringItem(version[_start_index: i], True))
                    _start_index = _ch

                    temp = ListItem()
                    ref_list.add_item(temp)
                    ref_list = temp
                _is_digit = True
            else:
                if _is_digit and _ch > _start_index:
                    ref_list.add_item(self.parse_item(True, version[_start_index:i]))
                    _start_index = i
                    stemp = ListItem()
                    ref_list.add_item(temp)
                    ref_list = temp
                _is_digit = False

        if len(version) > _start_index:
            ref_list.add_item(self.parse_item(_is_digit, version[_start_index]))

        return self.items.get_list()

    def parse_item(self, _is_digit, buf):
        if _is_digit:
            return IntegerItem(buf)

        return StringItem(buf, False)

    def compare_to(self, obj):

        return self.items.compare_to(obj.items)

# if __name__ == "__main__":
#     c = ComparableVersion("1-alpha-1")
#     c1 = ComparableVersion("1.0")

#     print(c.compare_to(c1))
#
