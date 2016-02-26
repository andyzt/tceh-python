# -*- coding: utf-8 -*-

import random

EMPTY_MARK = 'empty'
MOVES = {
    'w': (lambda e: e // 4 == 0, -4),
    's': (lambda e: e // 4 == 3, 4),
    'a': (lambda e: e % 4 == 0, -1),
    'd': (lambda e: e % 4 == 3, 1),
}


def shuffle_field():
    """
    This method is used to create a field at the very start of the game.
    :return: list with 16 randomly shuffled tiles,
    one of which is a empty space.
    """
    numbers = list(range(16))
    random.shuffle(numbers)

    empty_index = random.randint(0, 16)
    numbers[empty_index] = EMPTY_MARK
    return numbers


def print_field(field):
    """
    This method prints field to user.
    :param field: current field state to be printed.
    :return: None
    """
    for i in range(0, 16, 4):
        print(field[i:i+4])
    print('\n')


def is_game_finished(field):
    """
    This method checks if the game is finished.
    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    try:
        for i in range(len(field) - 2):
            if int(field[i]) > int((field[i + 1])):
                return False
        return field[-1] == EMPTY_MARK
    except ValueError:
        return False


def perform_move(field, key):
    """
    Moves empty-tile inside the field.
    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move).
    :raises: IndexError if the move can't me done.
    """
    key = key.lower()
    empty_spot = field.index(EMPTY_MARK)

    validation, vector = MOVES[key]

    if validation(empty_spot):
        raise IndexError("can't move %s" % key)

    to_change = empty_spot + vector
    field[empty_spot], field[to_change] = field[to_change], field[empty_spot]
    return field


def handle_user_input():
    """
    Handles user input. List of accepted moves:
    'w' - up, 's' - down,
    'a' - left, 'd' - right
    :return: <str> current move.
    """
    try:
        input_f = raw_input
    except NameError:
        input_f = input

    allowed_moves = list(MOVES.keys())
    message = 'Move %s: ' % ', '.join(allowed_moves)
    move = None

    while move not in allowed_moves:
        move = input_f(message).lower()
    return move


def main():
    """
    The main method.
    :return: None
    """
    # field = shuffle_field()
    field = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'empty', 11, 12, 13, 11]

    steps = 0
    while not is_game_finished(field):
        try:
            print_field(field)
            move = handle_user_input()
            field = perform_move(field, move)
            steps += 1
        except IndexError as ex:
            print(ex)
        except KeyboardInterrupt:
            print('Shutting down.')
            quit()
    print('You have completed the game in {} steps.'.format(steps))


if __name__ == '__main__':
    main()
