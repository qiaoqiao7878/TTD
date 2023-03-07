"""
from unittest import TestCase

from assertpy import assert_that

from src.rover import Rover


class TestRover(TestCase):
    def test_should_be_instantiated(
        self,
    ):
        rover = Rover()
        assert_that(rover).is_not_none()

    def test_not_moving(self):
        rover = Rover()
        command = "5 5\n1 2 N\n \n"
        desired_output = "1 2 N"
        result = rover.execute(command)
        assert_that(result).is_equal_to(desired_output)

    def test_moving_forward(self):
        rover = Rover()
        command = "5 5\n1 2 N\nM\n"
        desired_output = "1 3 N"
        result = rover.execute(command)
        assert_that(result).is_equal_to(desired_output)

    def test_turning_left(self):
        rover = Rover()
        command = "5 5\n1 2 N\nL\n"
        desired_output = "1 2 W"
        result = rover.execute(command)
        assert_that(result).is_equal_to(desired_output)

    def test_turning_right(self):
        rover = Rover()
        command = "5 5\n1 2 N\nR\n"
        desired_output = "1 2 E"
        result = rover.execute(command)
        assert_that(result).is_equal_to(desired_output)

    def test_command1(self):
        rover = Rover()
        command = "5 5\n1 2 N\nLMLMLMLMM\n3 3 E\nMMRMMRMRRM"
        desired_output = "1 3 N\n5 1 E"
        result = rover.execute(command)
        assert_that(result).is_equal_to(desired_output)

    def test_starting_position_out_of_bound(self):
        rover = Rover()
        command = "5 5\n5 5 N\nLMLML"
        try:
            result = rover.execute(command)
            assert False
        except ValueError:
            pass

    def test_starting_position_out_of_bound_smaller_than_zero(self):
        rover = Rover()
        command = "5 5\n-1 -1 N\nLMLML"
        try:
            result = rover.execute(command)
            assert False
        except ValueError:
            pass

    def test_after_moving_out_of_bound(self):
        rover = Rover()
        command = "5 5\n4 4 N\nMMMMM"
        try:
            result = rover.execute(command)
            assert False
        except ValueError:
            pass

    def test_invalid_initial_grid_definition(self):
        rover = Rover()
        command = "-1 -1\n-1 -1 N\nLMLML"
        try:
            result = rover.execute(command)
            assert False
        except ValueError:
            pass

    def test_invalid_direction(self):
        rover = Rover()
        command = "5 5\n4 4 P\nLMLML"
        try:
            result = rover.execute(command)
            assert False
        except ValueError:
            pass

    def test_invalid_moving_command(self):
        rover = Rover()
        command = "5 5\n4 4 N\nO"
        try:
            result = rover.execute(command)
            assert False
        except ValueError:
            pass
"""
