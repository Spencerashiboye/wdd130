""" Purpose: Water flow test 
Arthur: Spencer Ashiboye
"""
from pytest import approx
import pytest
from water_flow import (water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe,  
pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction)

def test_water_column_height():
    # Test cases
    assert water_column_height(0.0, 0.0) == 0.0 
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9


def test_pressure_gain_from_water_height():
    # Test cases
    assert pytest.approx(pressure_gain_from_water_height(0.0), abs=0.001) == 0.000  
    assert pytest.approx(pressure_gain_from_water_height(30.2), abs=0.001) == 295.628    
    assert pytest.approx(pressure_gain_from_water_height(50.0), abs=0.001) == 489.450

def test_pressure_loss_from_pipe():
    # test pressure loss from pipe seven times 
    assert pressure_loss_from_pipe (0.048692, 0.00, 0.018, 1.75,) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.000, 1.75,) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.018, 0.00,) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.018, 1.75,) == pytest.approx(-113.008, abs=0.001)
    assert pressure_loss_from_pipe (0.048692, 200.00, 0.018, 1.65,) == pytest.approx(-100.462, abs=0.001)
    assert pressure_loss_from_pipe (0.286870, 1000.00, 0.013, 1.65,) == pytest.approx(-61.576, abs=0.001)
    assert pressure_loss_from_pipe (0.286870, 1800.75, 0.013, 1.65,) == pytest.approx(-110.884, abs=0.001)

def test_pressure_loss_from_fittings():
    # Test cases
    assert pressure_loss_from_fittings(0.00, 3) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 0) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_fittings(1.65, 2) == pytest.approx(-0.109, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 2) == pytest.approx(-0.122, abs=0.001)
    assert pressure_loss_from_fittings(1.75, 5) == pytest.approx(-0.306, abs=0.001)

def test_reynolds_number():
    # Test cases
    assert reynolds_number(0.048692, 0.00) == pytest.approx(0, abs=1.0)
    assert reynolds_number(0.048692, 1.65) == pytest.approx(80069, abs=1.0)
    assert reynolds_number(0.048692, 1.75) == pytest.approx(84922, abs=1.0)
    assert reynolds_number(0.286870, 1.65) == pytest.approx(471729, abs=1.0)
    assert reynolds_number(0.286870, 1.75) == pytest.approx(500318, abs=1.0)

def test_pressure_loss_from_pipe_reduction():
    # Test cases
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == pytest.approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == pytest.approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == pytest.approx(-184.182, abs=0.001)


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])