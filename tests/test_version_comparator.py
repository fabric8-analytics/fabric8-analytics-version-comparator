"""Tests for the class Comparable Version."""
from f8a_version_comparator.comparable_version import ComparableVersion

def check_version_order(v1, v2):

    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)
    res = c.compare_to(c1)
    assert(res==-1)

def check_version_equal(v1, v2):

    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)
    res = c.compare_to(c1)
    assert(res==0)

def test_comparisons():

    check_version_order("1-alpha-1", "1.0")
    check_version_order("1", "2")
    check_version_order("1.5", "2")
    check_version_order("1", "2.5")
    check_version_order( "1", "2" )
    check_version_order( "1.5", "2" )
    check_version_order( "1", "2.5" )
    check_version_order( "1.0", "1.1" )
    check_version_order( "1.1", "1.2" )
    check_version_order( "1.0.0", "1.1" )
    check_version_order( "1.0.1", "1.1" )
    check_version_order( "1.1", "1.2.0" )

    check_version_equal( "1", "1" )
    check_version_equal( "1", "1.0" )
    check_version_equal( "1", "1.0.0" )
    check_version_equal( "1.0", "1.0.0" )
    check_version_equal( "1", "1-0" )
    check_version_equal( "1", "1.0-0" )
    check_version_equal( "1.0", "1.0-0" )
       #no separator between number and character
    check_version_equal( "1a", "1-a" )
    check_version_equal( "1a", "1.0-a" )
    check_version_equal( "1a", "1.0.0-a" )
    check_version_equal( "1.0a", "1-a" )
    check_version_equal( "1.0.0a", "1-a" )
    check_version_equal( "1x", "1-x" )
    check_version_equal( "1x", "1.0-x" )
    check_version_equal( "1x", "1.0.0-x" )
    check_version_equal( "1.0x", "1-x" )
    check_version_equal( "1.0.0x", "1-x" )

if __name__ == '__main__':
    test_comparisons()