# from unittest import TestCase

# from assertpy import assert_that

# from src.template import Template


# class TestWrapper(TestCase):
#     def test_empty_input(
#         self,
#     ):
#         my_input = ""
#         dictionary = {"variable": "foo"}
#         desired_output = ""
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_no_replacement_input(
#         self,
#     ):
#         my_input = "is"
#         dictionary = {"variable": "foo"}
#         desired_output = "is"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_one_word_replace(
#         self,
#     ):
#         my_input = "is ${variable}"
#         dictionary = {"variable": "foo"}
#         desired_output = "is foo"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_word_not_in_dict(
#         self,
#     ):
#         my_input = "is ${variable}"
#         dictionary = {"v": "foo"}
#         desired_output = "is ${variable}"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_one_word_replace_twice(
#         self,
#     ):
#         my_input = "is ${variable} is ${variable}"
#         dictionary = {"variable": "foo"}
#         desired_output = "is foo is foo"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_two_word_replace_twice(
#         self,
#     ):
#         my_input = "is ${variable} is ${variable2}"
#         dictionary = {"variable": "foo", "variable2": "bar"}
#         desired_output = "is foo is bar"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_missing_open_curly_braces(
#         self,
#     ):
#         my_input = "is $variable}"
#         dictionary = {
#             "variable": "foo",
#             "ariable": "bar",
#         }
#         desired_output = "is $variable}"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_missing_close_curly_braces(
#         self,
#     ):
#         my_input = "is ${variable"
#         dictionary = {
#             "variable": "foo",
#             "ariable": "bar",
#         }
#         desired_output = "is ${variable"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_word_is_empty(
#         self,
#     ):
#         my_input = "is ${}"
#         dictionary = {
#             "variable": "foo",
#             "ariable": "bar",
#         }
#         desired_output = "is ${}"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_multiple_dollars(
#         self,
#     ):
#         my_input = "is $$$$$${variable}"
#         dictionary = {
#             "variable": "foo",
#             "ariable": "bar",
#         }
#         desired_output = "is $$$$$foo"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)

#     def test_dollar_in_last_place(
#         self,
#     ):
#         my_input = "is $0"
#         dictionary = {
#             "variable": "foo",
#             "ariable": "bar",
#         }
#         desired_output = "is $0"
#         template = Template()
#         assert_that(template.replace(my_input, dictionary)).is_equal_to(desired_output)
