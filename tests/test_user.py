# from unittest import TestCase
# import pytest
# import re
# from assertpy import assert_that


# class User:
#     @classmethod
#     def create_valid_user(cls, name: str, email: str):
#         if not re.match("^[a-zA-Z]+$", name):
#             raise ValueError("Invalid name")
#         if not re.match("^\S+@\S+\.\S+$", email):
#             raise ValueError("Invalid email")
#         user = cls()
#         user.name = name
#         user.email = email
#         return user


# class MockDatabase:
#     def __init__(self) -> None:
#         self.database = {}

#     def save(self, user: User):
#         self.database[user.email] = user.name

#     def has_user(self, name: str, email: str) -> bool:
#         if email not in self.database.keys():
#             return False
#         if name != self.database[email]:
#             return False
#         return True


# class UserService:
#     def __init__(self, database: MockDatabase) -> None:
#         self.database = database

#     def create_user(self, name: str, email: str):
#         user = User.create_valid_user(name, email)
#         self.database.save(user)


# # @pytest.fixture(scope="function")
# # def user_service(database):
# #     return UserService(database)


# # @pytest.fixture(scope="function")
# # def database():
# #     return MockDatabase()


# class TestUserService(TestCase):
#     def test_create_user_should_fail_when_user_name_is_invalid(self):
#         database = MockDatabase()
#         user_service = UserService(database)
#         assert_that(user_service.create_user).raises(ValueError).when_called_with(
#             "1 invalid name", "irrelavant@email.test"
#         ).is_equal_to("Invalid name")

#     def test_create_user_should_fail_when_user_email_is_invalid(self):
#         database = MockDatabase()
#         user_service = UserService(database)
#         assert_that(user_service.create_user).raises(ValueError).when_called_with(
#             "validname", ""
#         ).is_equal_to("Invalid email")
#         assert_that(user_service.create_user).raises(ValueError).when_called_with(
#             "validname", "irrelavantemail.test"
#         ).is_equal_to("Invalid email")
#         assert_that(user_service.create_user).raises(ValueError).when_called_with(
#             "validname", "irrelavant@emailtest"
#         ).is_equal_to("Invalid email")
#         assert_that(user_service.create_user).raises(ValueError).when_called_with(
#             "validname", "irrelavantemailtest"
#         ).is_equal_to("Invalid email")

#     def test_create_user_should_not_fail_when_user_is_valid(self):
#         database = MockDatabase()
#         user_service = UserService(database)
#         user_service.create_user("validname", "valid@email.test")

#     def test_create_user_saved_in_database_when_user_is_valid(self):
#         database = MockDatabase()
#         user_service = UserService(database)
#         email = "valid@email.test"
#         name = "validname"
#         user_service.create_user(name, email)
#         assert database.has_user(name, email)

#     def test_create_user_saved_in_database_when_multiple_users_are_valid(self):
#         database = MockDatabase()
#         user_service = UserService(database)
#         email1 = "valid@email.test"
#         name1 = "validname"
#         user_service.create_user(name1, email1)

#         email2 = "valid2@email.test"
#         name2 = "validnamex"
#         user_service.create_user(name1, email1)
#         user_service.create_user(name2, email2)
#         assert database.has_user(name1, email1)
#         assert database.has_user(name2, email2)
