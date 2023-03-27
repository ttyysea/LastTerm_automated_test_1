from function import validate_number


def test_people_1_van_0_car_0():
    input = 1
    expected_result = (1, 0, 0)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_0_van_1_car_0():
    input = 11
    expected_result = (0, 1, 0)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_0_van_0_car_1():
    input = 4
    expected_result = (0, 0, 1)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_1_van_1_car_1():
    input = 16
    expected_result = (1, 1, 1)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_people_0_van_0_car_0():
    input = 0
    expected_result = (0, 0, 0)
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_number_not_integer_input_abc():
    input = "abc"
    expected_result = "number is not integer."
    actual_result = validate_number(input)
    assert expected_result == actual_result

def test_number_less_than_0_input_minus_1():
    input = -1
    expected_result = "The number must be greater than 0."
    actual_result = validate_number(input)
    assert expected_result == actual_result



