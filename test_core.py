import core


def test_gear_price():
    assert core.gear_price('1', 1) == 80 * 1.07
    assert core.gear_price('2', 1) == 120 * 1.07
    assert core.gear_price('3', 1) == 135 * 1.07
    assert core.gear_price('4', 1) == 125 * 1.07


def test_get_gear_type():
    assert core.get_gear_type('1') == 'djspeakers'
    assert core.get_gear_type('one') == 'djspeakers'
    assert core.get_gear_type('2') == 'stagespeakers'
    assert core.get_gear_type('two') == 'stagespeakers'
    assert core.get_gear_type('3') == 'subspeakers'
    assert core.get_gear_type('three') == 'subspeakers'
    assert core.get_gear_type('4') == 'djcontroller'
    assert core.get_gear_type('four') == 'djcontroller'


def test_actual_price():
    assert core.actual_price('1') == 350
    assert core.actual_price('2') == 750
    assert core.actual_price('3') == 750
    assert core.actual_price('4') == 600


def test_deposit():
    assert core.deposit(350.0) == 35.0
    assert core.deposit(750.0) == 75.0
    assert core.deposit(750.0) == 75.0
    assert core.deposit(600.0) == 60.0
