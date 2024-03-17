import random

def add_chip(chip_number):
  """Adds a chip to the specified position on the board.

  Args:
    chip_number: The number of the chip to add (0-7).
  """

  # Check if the chip number is valid.
  if chip_number < 0 or chip_number > 7:
    raise ValueError("Invalid chip number.")

  # Add the chip to the board.
  board[chip_number] = 1

# Get a random chip number.
chip_number = random.randint(0, 7)

# Add the chip to the board.
add_chip(chip_number)
