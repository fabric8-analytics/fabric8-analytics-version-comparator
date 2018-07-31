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
# Author: Geetika Batra <gbatra@redhat.com>, Pavel Tisnovsky <ptisnovs@redhat.com>
#

"""Tests for the class Comparable Version."""


import pytest

from f8a_version_comparator.comparable_version import ComparableVersion


def check_version_order(v1, v2):
    """Check order of versions."""
    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)

    # check using `compare_to` method
    res = c.compare_to(c1)
    assert res == -1, "{} is greater than {}".format(v1, v2)

    # check using `compare_to` method and version string
    res = c.compare_to(v2)
    assert res == -1, "{} is greater than {}".format(v1, v2)

    # check using rich comparison
    assert c < c1, "rich comparison: {} is not lower than {}".format(v1, v2)


def check_version_different_order(v1, v2):
    """Check order of versions, the first version must be greater that the second."""
    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)

    # check using `compare_to` method
    res = c.compare_to(c1)
    assert res == 1, "{} is less than {}".format(v1, v2)

    # check using `compare_to` method and version string
    res = c.compare_to(v2)
    assert res == 1, "{} is less than {}".format(v1, v2)

    # check using rich comparison
    assert c > c1, "rich comparison: {} is not greater than {}".format(v1, v2)


def check_version_equal(v1, v2):
    """Check if versions are equal."""
    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)

    # check using `compare_to` method
    res = c.compare_to(c1)
    assert res == 0, "{} is not equal to {}".format(v1, v2)

    # check using `compare_to` method and version string
    res = c.compare_to(v2)
    assert res == 0, "{} is not equal to {}".format(v1, v2)

    # check using rich comparison
    assert c == c1, "rich comparison: {} is not equal to {}".format(v1, v2)


def test_init():
    """Test ComparableVersion objects `__init__` method."""
    # should work
    version = '1.0.0'
    _ = ComparableVersion(version)

    # both should raise
    with pytest.raises(TypeError):
        _ = ComparableVersion(None)
        assert _ is not None
        _ = ComparableVersion(1.0)
        assert _ is not None


def test_repr():
    """Test ComparableVersion objects `__repr__` method."""
    version = '1.0.0'
    expected_repr = "ComparableVersion(version={!r})".format(version)

    assert repr(ComparableVersion(version)) == expected_repr, "Invalid representation."


def test_str():
    """Test ComparableVersion objects `__str__` method."""
    version = '1.0.0'
    assert str(ComparableVersion(version)) == version, "Invalid string conversion."


def test_eq_operator():
    """Test the == operator."""
    version = '1.0.0'
    c1 = ComparableVersion(version)
    c2 = ComparableVersion(version)
    assert c1 == c2

    # ComparableVersion == None
    assert not c1 == None  # noqa - because we really want to use == here

    version = '2.5.3-alpha'
    c3 = ComparableVersion(version)
    c4 = ComparableVersion(version)
    assert c3 == c4

    # ComparableVersion == None
    assert not c3 == None  # noqa - because we really want to use == here


def test_lt_operator():
    """Test the < operator."""
    version = '1.0.0'
    c1 = ComparableVersion(version)
    version = '2.0.0'
    c2 = ComparableVersion(version)
    assert c1 < c2

    # ComparableVersion < None
    assert not c1 < None
    assert not c2 < None

    version = '2.1.1'
    c3 = ComparableVersion(version)
    assert c2 < c3
    # transitivity check
    assert c1 < c3

    # ComparableVersion < None
    assert not c3 < None


def test_gt_operator():
    """Test the > operator."""
    version = '2.0.0'
    c1 = ComparableVersion(version)
    version = '1.0.0'
    c2 = ComparableVersion(version)
    assert c1 > c2

    # ComparableVersion < None
    assert c1 > None
    assert c2 > None

    version = '2.1.1'
    c3 = ComparableVersion(version)
    assert c3 > c2
    # transitivity check
    assert c3 > c1

    # ComparableVersion > None
    assert c3 > None


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

    check_version_different_order("8.0.0", "1.0.0")
    check_version_different_order("6.1.0", "6.1.0rc3")
    check_version_different_order("6.1H.5-beta", "6.1.0rc3")
    check_version_different_order("6.1H.5-beta", "6.1.0")

    check_version_different_order("6.1-alpha", "beta")
    check_version_different_order("6.1-beta", "6.1-alpha")


def test_comparisons_wrong_type():
    """Test function compare_to."""
    v1 = "1.0.0"
    c = ComparableVersion(v1)
    # check the TypeError
    with pytest.raises(TypeError):
        c.compare_to(None)
        c.compare_to(True)
        c.compare_to(False)
        c.compare_to([])
        c.compare_to({})
        c.compare_to(42)
        c.compare_to(3.14)
        c.compare_to(1 + 2j)


def test_parse_version():
    """Test the method to parse version."""
    c = ComparableVersion("1")
    itemlist = c.items.get_list()
    assert len(itemlist) == 1
    assert str(itemlist[0]) == "1"

    c = ComparableVersion("1.2")
    itemlist = c.items.get_list()
    assert len(itemlist) == 2
    assert str(itemlist[0]) == "1"
    assert str(itemlist[1]) == "2"

    c = ComparableVersion("1-2")
    itemlist = c.items.get_list()
    assert len(itemlist) == 2

    c = ComparableVersion(".2")
    itemlist = c.items.get_list()
    assert len(itemlist) == 2

    c = ComparableVersion("-2")
    itemlist = c.items.get_list()
    assert len(itemlist) == 1


def test_parse_item():
    """Test the method to parse item."""
    c = ComparableVersion("2")

    p1 = c.parse_item(False, "StringItem")
    assert p1 is not None
    assert str(p1) == "StringItem"

    p2 = c.parse_item(True, "0")
    assert p2 is not None
    assert str(p2) == "0"

    # try to parse empty string (which is definitely not a number)
    with pytest.raises(ValueError):
        p3 = c.parse_item(True, "")
        assert p3 is not None

    # try to parse string that does not contain a number
    with pytest.raises(ValueError):
        p3 = c.parse_item(True, "foobar")
        assert p3 is not None


if __name__ == '__main__':
    test_init()
    test_comparisons()
    test_comparisons_wrong_type()
    test_parse_version()
    test_parse_item()
    test_repr()
    test_str()
    test_eq_operator()
    test_lt_operator()
    test_gt_operator()
