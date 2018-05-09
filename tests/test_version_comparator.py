# Copyright © 2018 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
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
    assert(res == -1), "{} is greater than {}".format(v1, v2)


def check_version_equal(v1, v2):
    """Check if versions are equal."""
    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)
    res = c.compare_to(c1)
    assert(res == 0), "{} is not equal to  {}".format(v1, v2)


def test_comparisons():
    """Test function covering all the cases."""
    check_version_order("1-alpha-1", "1.0")
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
