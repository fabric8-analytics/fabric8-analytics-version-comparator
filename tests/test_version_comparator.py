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
    check_version_order( "1.0-alpha-1", "1.0" )
    check_version_order( "1.0-alpha-1", "1.0-alpha-2" )
    check_version_order( "1.0-alpha-1", "1.0-beta-1" )

    check_version_order( "1.0-beta-1", "1.0-SNAPSHOT" )
    check_version_order( "1.0-SNAPSHOT", "1.0" )
    check_version_order( "1.0-alpha-1-SNAPSHOT", "1.0-alpha-1" )

    check_version_order( "1.0", "1.0-1" )
    check_version_order( "1.0-1", "1.0-2" )
    check_version_order( "1.0.0", "1.0-1" )

    check_version_order( "2.0-1", "2.0.1" )
    check_version_order( "2.0.1-klm", "2.0.1-lmn" )
    check_version_order( "2.0.1", "2.0.1-xyz" )

    check_version_order( "2.0.1", "2.0.1-123" )
    check_version_order( "2.0.1-xyz", "2.0.1-123" )


if __name__ == '__main__':
    test_comparisons()