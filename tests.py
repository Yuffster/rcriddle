import riddle

def test_get_grid():
	crossword = """

	                ┌───┐
	                │ W │
	┌───┬───┬───┬───├───┤
	│ H │ E │ L │ L │ O │
	└───┴───┴───┴───┼───┤
	                │ R │
	    ┌───┐       ├───┤
	    │   │       │ L │
	    └───┘       ├───┤
	                │ D │
	                └───┘
	"""
	expected = [
	    [' ', ' ', ' ', ' ', 'W'],
	    ['H', 'E', 'L', 'L', 'O'],
	    [' ', ' ', ' ', ' ', 'R'],
	    [' ', '?', ' ', ' ', 'L'],
	    [' ', ' ', ' ', ' ', 'D']
	]
	assert(riddle.get_grid(crossword) == expected)


def test_rotate_grid():
	start = [
	    [' ', ' ', ' ', ' ', 'W'],
	    ['H', 'E', 'L', 'L', 'O'],
	    [' ', ' ', ' ', ' ', 'R'],
	    [' ', '?', ' ', ' ', 'L'],
	    [' ', ' ', ' ', ' ', 'D']
	]
	expected = [
	    [' ', ' ', ' ', 'H', ' '],
	    [' ', '?', ' ', 'E', ' '],
	    [' ', ' ', ' ', 'L', ' '],
	    [' ', ' ', ' ', 'L', ' '],
	    ['D', 'L', 'R', 'O', 'W']
	]
	assert(riddle.rotate_grid(start) == expected)


def test_get_words():
	start = [
	    [' ', ' ', ' ', ' ', 'W'],
	    ['H', 'E', 'L', 'L', 'O'],
	    [' ', ' ', ' ', ' ', 'R'],
	    [' ', '?', ' ', ' ', 'L'],
	    [' ', ' ', ' ', ' ', 'D']
	]
	result = riddle.get_words(start)
	assert("HELLO" in result)
	assert("WORLD" in result)
