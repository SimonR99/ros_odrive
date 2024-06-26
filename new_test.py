"""
This code is for testing odrive functionality.
** Need to implement using async **
"""
import time
import utils
from odrive.enums import *
import odrive

def run_seconds(odrv, running_time: int, running_speed: int = 3,
                delay_time: int = 3, debug_interval: int = 1) -> None:
    """
    Run odrive for running_time seconds.
    Delay for delay seconds both before and after running.
    Print out voltage and current every second.
    """

    odrv.axis0.requested_state = AxisState.CLOSED_LOOP_CONTROL
    for _ in range(delay_time):
        utils.print_voltage_current(odrv)
        time.sleep(debug_interval)

    odrv.axis0.controller.input_vel = running_speed
    for _ in range(running_time):
        utils.print_voltage_current(odrv)
        time.sleep(debug_interval)

    odrv.axis0.controller.input_vel = 10
    for _ in range(delay_time):
        utils.print_voltage_current(odrv)
        time.sleep(debug_interval)

    odrv.axis0.controller.input_vel = -running_speed
    for _ in range(running_time):
        utils.print_voltage_current(odrv)
        time.sleep(debug_interval)

    odrv.axis0.controller.input_vel = 20
    for _ in range(delay_time):
        utils.print_voltage_current(odrv)
        time.sleep(debug_interval)


def test_run(running_time=5, running_speed=3) -> None:
    """
    Take a dictionary of section:odrive and perform test run.
    """
    odrv = odrive.find_any()
    #utils.check_error(odrv, section)  # Checking errors
    #rint(f'Test run {section}...')
    run_seconds(odrv, running_time, running_speed)  # Test run


if __name__ == '__main__':
    test_run(running_time=5, running_speed=3)  # Call test run function