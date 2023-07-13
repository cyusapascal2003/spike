from hub import port
import color
import color_sensor
import motor
import runloop


async def main():
    # Move straight at default velocity
    motor.run(port.A, -500)
    motor.run(port.B, 500)
    motor.run(port.C, 500)
    motor.run(port.D, -500)

    while color_sensor.color(port.E) != color.GREEN or color_sensor.color(port.E) != color.BLACK:
        # When front sensor detects green or black, stop and move backward
        if color_sensor.color(port.E) == color.GREEN or color_sensor.color(port.E) == color.BLACK:
            motor.stop(port.A)
            motor.stop(port.B)
            motor.stop(port.C)
            motor.stop(port.D)
            # Wait for 1 second
            await runloop.sleep_ms(1000)
            motor.run(port.A, 500)
            motor.run(port.B, -500)
            motor.run(port.C, -500)
            motor.run(port.D, 500)
        # Whwn back sensor detects green or black, stop and move forward
        if color_sensor.color(port.F) == color.GREEN or color_sensor.color(port.F) == color.BLACK:
            motor.stop(port.A)
            motor.stop(port.B)
            motor.stop(port.C)
            motor.stop(port.D)
            # Wait for 1 second
            await runloop.sleep_ms(1000)
            # Move forward at default velocity
            motor.run(port.A, -500)
            motor.run(port.B, 500)
            motor.run(port.C, 500)
            motor.run(port.D, -500)

runloop.run(main())
