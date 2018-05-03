"""Tests for the class Comparable Version."""
from f8a_version_comparator.comparable_version import ComparableVersion

def check_version_order(v1, v2):

    c = ComparableVersion(v1)
    c1 = ComparableVersion(v2)
    res = c.compare_to(c1)
    assert(res==-1)

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

if __name__ == '__main__':
    test_comparisons()