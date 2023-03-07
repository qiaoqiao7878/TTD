"""
from unittest import TestCase

from assertpy import assert_that

from src.word_wrap import Wrapper


class TestWrapper(TestCase):
    def test_empty_string_with_0_column(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("", 0)).is_equal_to("")

    def test_string_with_0_column(
        self,
    ):
        wrapper = Wrapper()
        try:
            result = wrapper.wrap("asd", 0)
            assert False
        except ValueError:
            pass

    def test_string_with_1_column(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("asd", 1)).is_equal_to("a\ns\nd")

    def test_word_is_longer_than_column_allowed(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("asd", 2)).is_equal_to("as\nd")
        assert_that(wrapper.wrap("asdf", 2)).is_equal_to("as\ndf")

    def test_(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("as asdf", 2)).is_equal_to("as\nas\ndf")
        assert_that(wrapper.wrap("as asdf", 3)).is_equal_to("as\nasd\nf")
        assert_that(wrapper.wrap("as asdf", 4)).is_equal_to("as\nasdf")

    def test_only_spaces(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("     ", 1)).is_equal_to("")

    def test_words_with_line_break(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("as\nasdf", 2)).is_equal_to("as\nas\ndf")

    def test_words_with_multuple_spaces(
        self,
    ):
        wrapper = Wrapper()
        assert_that(wrapper.wrap("as   as", 3)).is_equal_to("as\nas")
"""