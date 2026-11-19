from calculator import add, subtract, multiply, divide, circleArea

def test_circleArea():
	assert circleArea(-4) == "Error"

def test_add():
	assert add(2, 3) == 5

def test_divide():
	assert divide(6, 2) == 3

def test_multiply():
	assert multiply(3, 2) == 6

def test_subtract():
	assert subtract(10, 6) == 4

def test_divide_uneven():
	#arrange
	a, b = 5, 2
	#act
	result = divide(a, b)
	#assert
	assert result == 2.5
