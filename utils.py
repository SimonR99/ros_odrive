"""
Utility functions for ODrive calibration and test.
"""

import yaml
import odrive
from odrive.enums import *


def print_voltage_current(odrv) -> None:
    """
    Print voltage and current for debugging.
    """
    print(f'  voltage = {odrv.vbus_voltage:5.2f} V'
          f'  current = {odrv.ibus:5.2f} A')


def find_odrvs():
    """
    This function will find ODrive that serial numbers are list
    in the config.yml. Need to improve to async operation.
    """
    

    return odrive.find_any()


def check_error(odrv, name: str | None = None) -> None:
    """
    This function will print the error
    """
    if name is not None:
        print(f'{name} odrive checking...')
    print_voltage_current(odrv)
    print(f'  {"error code:":<12}axis0{" " * 27}| axis1')
    print(f'  {"controller":<10}  '
          f'{ControllerError(odrv.axis0.controller.error).name:31} | '
          f'{ControllerError(odrv.axis1.controller.error).name:15}')
    print(f'  {"encoder":<10}  '
          f'{EncoderError(odrv.axis0.encoder.error).name:31} | '
          f'{EncoderError(odrv.axis1.encoder.error).name:15}')
    print(f'  {"motor":<10}  '
          f'{MotorError(odrv.axis0.motor.error).name:31} | '
          f'{MotorError(odrv.axis1.motor.error).name:15}')
    print('--------------------------------------')


def check_version(odrv) -> None:
    """
    Print out hardware version and firmware version.
    """
    print(f'Firmware version is {odrv.fw_version_major}.'
          f'{odrv.fw_version_minor}.{odrv.fw_version_revision}'
          f'{" " * 3} Hardware version is {odrv.hw_version_major}.'
          f'{odrv.hw_version_minor}.{odrv.hw_version_variant}')