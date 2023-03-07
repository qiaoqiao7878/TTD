"""
from unittest import TestCase

from assertpy import assert_that

from src.add import add_numbers


class TestRover(TestCase):
    def test_empty_string(self):
        assert_that(add_numbers("")).is_equal_to(0)

    def test_one_number(self):
        assert_that(add_numbers("1")).is_equal_to(1)
        assert_that(add_numbers("10")).is_equal_to(10)

    def test_two_numbers(self):
        assert_that(add_numbers("1,2")).is_equal_to(3)
        assert_that(add_numbers("10,1")).is_equal_to(11)

    def test_more_numbers(self):
        assert_that(add_numbers("1,2,3")).is_equal_to(6)
        assert_that(add_numbers("1000,100,10,1")).is_equal_to(1111)

    def test_new_line_break(self):
        assert_that(add_numbers("1\n2,3")).is_equal_to(6)

    def test_different_delimiters(self):
        assert_that(add_numbers("//;\n1;2")).is_equal_to(3)
        assert_that(add_numbers("//.\n1.2")).is_equal_to(3)
"""