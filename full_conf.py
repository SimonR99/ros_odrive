import odrive
import time
import math
from odrive.enums import *



odrv0 = odrive.find_any()


odrv = odrv0
odrv.config.dc_bus_overvoltage_trip_level = 52
odrv.config.dc_max_negative_current = -1
odrv.axis0.config.motor.motor_type = MotorType.HIGH_CURRENT
odrv.axis0.config.motor.torque_constant = 0.09963855421686746
odrv.axis0.config.motor.pole_pairs = 3
odrv.axis0.config.motor.current_soft_max = 10
odrv.axis0.config.motor.current_hard_max = 23
odrv.axis0.config.motor.calibration_current = 1
odrv.axis0.config.motor.resistance_calib_max_voltage = 5
odrv.axis0.controller.config.input_mode = InputMode.PASSTHROUGH
odrv.axis0.controller.config.control_mode = ControlMode.TORQUE_CONTROL
odrv.axis0.controller.config.vel_limit = 58
odrv.axis0.controller.config.vel_limit_tolerance = 1
odrv.axis0.config.torque_soft_min = -0.9
odrv.axis0.config.torque_soft_max = 0.9
odrv.can.config.baud_rate = 1000000
odrv.axis0.config.can.node_id = 11
odrv.axis0.config.can.encoder_msg_rate_ms = 0
odrv.axis0.config.can.iq_msg_rate_ms = 0
odrv.axis0.config.can.torques_msg_rate_ms = 0
odrv.axis0.config.can.error_msg_rate_ms = 0
odrv.axis0.config.can.temperature_msg_rate_ms = 0
odrv.axis0.config.can.bus_voltage_msg_rate_ms = 0
odrv.can.config.protocol = Protocol.SIMPLE
odrv.config.enable_uart_a = False
odrv.rs485_encoder_group0.config.mode = Rs485EncoderMode.AMT21_EVENT_DRIVEN
odrv.axis0.config.load_encoder = EncoderId.RS485_ENCODER0
odrv.axis0.config.commutation_encoder = EncoderId.RS485_ENCODER0

odrv0.axis0.controller.config.pos_gain = 10.0
odrv.axis0.controller.config.vel_integrator_gain = 0.0
odrv0.axis0.controller.config.vel_gain = 0.01


odrv.axis0.controller.config.spinout_electrical_power_threshold = 1000
odrv.axis0.controller.config.spinout_mechanical_power_threshold = -1000



odrv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# Wait for calibration to take place

time.sleep(1)

odrv.axis0.controller.input_torque = 2.0

time.sleep(2)

odrv.axis0.controller.input_torque = 0

