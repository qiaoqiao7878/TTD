from src.directions import Directions


class Rover:
    def __init__(self):
        self.direction: str = Directions.NORTH
        # TODO: Maybe this should be in a separated class?
        self.parsedCommands = {}
        self.y: int = 0
        self.x: int = 0

    def parse_commands(self, commands):
        return commands

    def execute(self, commands):
        self.parsedCommands = self.parse_commands(commands)

        self.y = self.parsedCommands.starting_position.y
        self.x = self.parsedCommands.starting_position.x
        self.direction = self.parsedCommands.starting_position.d

        for movement in self.parsedCommands.moving_command:
            self.move(movement)

        return self.x + ' ' + self.y + ' ' + self.direction

    def move(self, movement: str):
        """
        Args:
          movement
        """
        if movement == "L":
            self.turn_left()
        elif movement == "R":
            self.turn_right()
        elif movement == "M":
            self.move_forward()

    def turn_left(self):
        if self.direction == Directions.NORTH:
            self.direction = Directions.WEST
        elif self.direction == Directions.WEST:
            self.direction = Directions.SOUTH
        elif self.direction == Directions.SOUTH:
            self.direction = Directions.EAST
        elif self.direction == Directions.EAST:
            self.direction = Directions.NORTH

    def turn_right(self):
        if self.direction == Directions.NORTH:
            self.direction = Directions.EAST
        elif self.direction == Directions.EAST:
            self.direction = Directions.SOUTH
        elif self.direction == Directions.SOUTH:
            self.direction = Directions.WEST
        elif self.direction == Directions.WEST:
            self.direction = Directions.NORTH

    def move_forward(self):
        if self.direction == Directions.NORTH:
            self.y = self.y + 1
        elif self.direction == Directions.EAST:
            self.x = self.x + 1
        elif self.direction == Directions.SOUTH:
            self.y = self.y - 1
        elif self.direction == Directions.WEST:
            self.x = self.x - 1
