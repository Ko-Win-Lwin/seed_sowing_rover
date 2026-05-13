import time

import motor
import encoder
import ultrasonic
import servo
import oled_display

from config import (
    BASE_SPEED,
    KP,
    LEFT_OFFSET,
    RIGHT_OFFSET,
    WHEEL_CIRCUMFERENCE,
    SLOTS,
    SEED_DISTANCE_CM,
    WALL_DISTANCE,
)

encoder.reset()

last_seed_distance = 0

while True:

    # ======================
    # READ ENCODERS
    # ======================

    left_pulses, right_pulses = encoder.get_pulses()

    # ======================
    # STRAIGHT CORRECTION
    # ======================

    error = left_pulses - right_pulses

    correction = error * KP

    left_speed = (
        BASE_SPEED
        - correction
        + LEFT_OFFSET
    )

    right_speed = (
        BASE_SPEED
        + correction
        + RIGHT_OFFSET
    )

    # ======================
    # DRIVE
    # ======================

    motor.drive(
        left_speed,
        right_speed
    )

    # ======================
    # DISTANCE
    # ======================

    average_pulses = (
        left_pulses
        + right_pulses
    ) / 2

    turns = average_pulses / SLOTS

    distance_cm = (
        turns
        * WHEEL_CIRCUMFERENCE
    )

    # ======================
    # SEED DROPPING
    # ======================

    if (
        distance_cm
        - last_seed_distance
        >= SEED_DISTANCE_CM
    ):

        print("STOP")

        motor.stop()

        time.sleep(0.3)

        print("DROP SEED")

        servo.drop_seed()

        last_seed_distance = distance_cm

        time.sleep(0.3)

    # ======================
    # ULTRASONIC
    # ======================

    dist = ultrasonic.get_distance()

    if (
        dist != -1
        and dist < WALL_DISTANCE
    ):

        print("OBSTACLE")

        motor.stop()

        oled_display.show(
            "STOP",
            dist,
            left_pulses,
            right_pulses
        )

        break

    # ======================
    # OLED
    # ======================

    oled_display.show(
        "RUN",
        dist,
        left_pulses,
        right_pulses
    )

    # ======================
    # DEBUG
    # ======================

    print(
        "L:", left_pulses,
        "R:", right_pulses,
        "DIST:", distance_cm
    )

    time.sleep(0.05)