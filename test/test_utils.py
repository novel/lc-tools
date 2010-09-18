"""Tests for test util module"""

from nose.tools import *

from lctools.utils import int_sequence, is_int_sequence

class TestIntSequence(object):
    """Test Class for lctools.utils.int_sequence
    function."""

    def test_that_int_sequence_processes_single_int(self):
        ints = int_sequence("3")

        assert_true(isinstance(ints, list))
        assert_equal(len(ints), 1)
        assert_equal(ints[0], 3)

    def test_that_int_sequence_processes_several_ints(self):
        ints = int_sequence("3, 4, 6, 123, 345")

        assert_true(isinstance(ints, list))
        assert_equal(len(ints), 5)
        assert_equal(set(ints), set([3, 4, 6, 123, 345]))

    def test_that_int_sequence_proccesses_simple_ranges(self):
        ints = int_sequence("0-5")

        assert_true(isinstance(ints, list))
        assert_equal(len(ints), 6)
        assert_equal(set(ints), set(range(0, 6)))

    def test_that_int_sequence_processes_mixed_ranges_and_ints(self):
        ints = int_sequence("1-3,5,7-9,12")

        assert_true(isinstance(ints, list))
        assert_equal(len(ints), 8)
        assert_equal(set(ints), set([1, 2, 3, 5, 7, 8, 9, 12]))

    @raises(ValueError)
    def test_that_int_sequence_fails_on_malformed_sequence(self):
        ints = int_sequence("-23")

    @raises(ValueError)
    def test_that_int_sequence_fails_on_illegal_values(self):
        ints = int_sequence("4-2")

class TestIsIntSequence(object):
    """Test Class for lctools.utils.is_int_sequence function."""

    def test_that_is_int_sequence_returns_true_for_int_sequence(self):
        assert_true(is_int_sequence("1-3,7,10"))

    def test_that_is_int_sequence_returns_true_for_digit(self):
        assert_true(is_int_sequence("143"))

    def test_that_is_int_sequence_returns_false_for_some_alfanum_str(self):
        assert_false(is_int_sequence("h345aha"))

    def test_that_is_int_sequence_returns_false_for_alnum_str(self):
        assert_false(is_int_sequence("hehe"))
