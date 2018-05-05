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
#
# Author: Geetika Batra <gbatra@redhat.com>
#

"""Tests for the class Comparable Version."""

from f8a_version_comparator.comparable_version import ComparableVersion


def check_version_order(v1, v2):
    """Check order of versions."""
    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)
    res = c.compare_to(c1)
    assert(res == -1)


def check_version_equal(v1, v2):
    """Check if versions are equal."""
    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)
    res = c.compare_to(c1)
    assert(res == 0)


def test_comparisons():
    """Test function covering all the cases."""
    check_version_order("1-alpha-1", "1.0")
    check_version_order("1", "2")
    check_version_order("1.5", "2")
    check_version_order("1", "2.5")
    check_version_order("1", "2")
    check_version_order("1.5", "2")
    check_version_order("1", "2.5")
    check_version_order("1.0", "1.1")
    check_version_order("1.1", "1.2")
    check_version_order("1.0.0", "1.1")
    check_version_order("1.0.1", "1.1")
    check_version_order("1.1", "1.2.0")

    check_version_equal("1", "1")
    check_version_equal("1", "1.0")
    check_version_equal("1", "1.0.0")
    check_version_equal("1.0", "1.0.0")
    check_version_equal("1", "1-0")
    check_version_equal("1", "1.0-0")
    check_version_equal("1.0", "1.0-0")

    # no separator between number and character
    check_version_equal("1a", "1-a")
    check_version_equal("1a", "1.0-a")
    check_version_equal("1a", "1.0.0-a")
    check_version_equal("1.0a", "1-a")
    check_version_equal("1.0.0a", "1-a")
    check_version_equal("1x", "1-x")
    check_version_equal("1x", "1.0-x")
    check_version_equal("1x", "1.0.0-x")
    check_version_equal("1.0x", "1-x")
    check_version_equal("1.0.0x", "1-x")

    # aliases
    check_version_equal("1ga", "1")
    check_version_equal("1final", "1")
    check_version_equal("1cr", "1rc")

    # special "aliases" a, b and m for alpha, beta and milestone
    check_version_equal("1a1", "1-alpha-1")
    check_version_equal("1b2", "1-beta-2")
    check_version_equal("1m3", "1-milestone-3")

    # case insensitive
    check_version_equal("1X", "1x")
    check_version_equal("1A", "1a")
    check_version_equal("1B", "1b")
    check_version_equal("1M", "1m")
    check_version_equal("1Ga", "1")
    check_version_equal("1GA", "1")
    check_version_equal("1Final", "1")
    check_version_equal("1FinaL", "1")
    check_version_equal("1FINAL", "1")
    check_version_equal("1Cr", "1Rc")
    check_version_equal("1cR", "1rC")
    check_version_equal("1m3", "1Milestone3")
    check_version_equal("1m3", "1MileStone3")
    check_version_equal("1m3", "1MILESTONE3")

    check_version_order("6.1.0rc3", "6.1.0")
    check_version_order("6.1.0rc3", "6.1H.5-beta")
    check_version_order("6.1.0", "6.1H.5-beta")


if __name__ == '__main__':
    test_comparisons()
