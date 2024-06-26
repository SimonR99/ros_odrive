import odrive
import time
import math
from odrive.enums import *
from odrive.utils import start_liveplotter



def run_state(axis, requested_state, wait):
    """
    Sets the requested state on the given axis. If wait is True, the method
    will block until the state goes back to idle.

    Returns whether the odrive went back to idle in the given timeout period,
    which is 10s by default.
    """
    axis.requested_state = requested_state
    timeout_ctr = 100; # 20s timeout for encoder calibration to finish
    if wait:
        while(timeout_ctr > 0): # waits until state goes back to idle to continue
            time.sleep(0.2)
            timeout_ctr -= 1
            if axis.current_state == AXIS_STATE_IDLE:
                break
    return timeout_ctr > 0

odrv0 = odrive.find_any()
odrv = odrv0




odrv.axis0.controller.config.spinout_electrical_power_threshold = 10
odrv.axis0.controller.config.spinout_mechanical_power_threshold = -10

odrv.axis0.controller.config.pos_gain = 20.0
odrv.axis0.controller.config.vel_gain = 0.08
odrv.axis0.controller.config.vel_integrator_gain = 0.2

odrv.axis0.controller.config.control_mode = ControlMode.TORQUE_CONTROL

odrv.axis0.requested_state = AXIS_STATE_CLOSED_LOOP_CONTROL

# Wait for calibration to take place

start_liveplotter(lambda:[odrv0.axis0.vel_estimate, odrv0.axis0.controller.vel_setpoint])
#start_liveplotter(lambda:[odrv0.axis0.pos_estimate, odrv0.axis0.controller.pos_setpoint])


time.sleep(2)

total_time = 10
max_vel = 20.0

ramping_time = total_time/3

n_segments = 3

for i in range(n_segments):
    odrv.axis0.controller.input_torque = max_vel/n_segments * i
    print(max_vel/n_segments * i)
    time.sleep(ramping_time/n_segments)

odrv.axis0.controller.input_torque = max_vel
time.sleep(ramping_time)

for i in range(n_segments, 0, -1):
    odrv.axis0.controller.input_torque = max_vel/n_segments * i
    print(max_vel/n_segments * i)
    time.sleep(ramping_time/n_segments)

odrv.axis0.controller.input_torque = 0

time.sleep(5)




odrv.save_configuration()