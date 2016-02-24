# -*- coding: utf-8 -*-

import random  # see https://docs.python.org/2/library/random.html

EMPTY_MARK = 'empty'


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    raise NotImplemented()


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    raise NotImplemented()


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    raise NotImplemented()


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    raise NotImplemented()


def handle_user_input():
    """
    Handles user input. List of accepted moves:
    'w' - up, 's' - down,
    'a' - left, 'd' - right
    :return: <str> current move.
    """
    raise NotImplemented()


def main():
    """
    The main method.
    :return: None
    """
    raise NotImplemented()

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()