import can

def send_velocity_command(bus, node_id, velocity):
    # Velocity command ID for ODrive: 0x00 is for AXIS0, 0x01 is for AXIS1
    velocity_command_id = 0x00
    arbitration_id = (node_id << 5) | velocity_command_id

    # Convert velocity to integer representation
    velocity_int = int(velocity * 10000)  # Scale factor based on ODrive documentation

    # Create a CAN message
    data = velocity_int.to_bytes(4, byteorder='little', signed=True) + bytes(4)  # 8-byte message
    msg = can.Message(arbitration_id=arbitration_id, data=data, is_extended_id=False)

    # Send the message on the CAN bus
    bus.send(msg)
    print(f'Sent velocity command {velocity} to node {node_id}.')

def main():
    # Initialize CAN bus (can0)
    bus = can.interface.Bus(channel='can0', bustype='socketcan')

    # Node ID for ODrive (change as needed) (node 12)
    node_id = 0x18

    # Desired velocity (in turns per second)
    desired_velocity = 20.0

    # Send velocity command
    send_velocity_command(bus, node_id, desired_velocity)

if __name__ == '__main__':
    main()
