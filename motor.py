from machine import Pin, PWM
from config import MAX_SPEED, MIN_SPEED

# LEFT MOTOR
IN1 = Pin(10, Pin.OUT)
IN2 = Pin(11, Pin.OUT)
ENA = PWM(Pin(12))
ENA.freq(1000)

# RIGHT MOTOR
IN3 = Pin(14, Pin.OUT)
IN4 = Pin(15, Pin.OUT)
ENB = PWM(Pin(13))
ENB.freq(1000)


def constrain(value, minimum, maximum):
    return max(minimum, min(maximum, value))


def drive(left_speed, right_speed):

    left_speed = constrain(left_speed, MIN_SPEED, MAX_SPEED)
    right_speed = constrain(right_speed, MIN_SPEED, MAX_SPEED)

    IN1.value(1)
    IN2.value(0)

    IN3.value(1)
    IN4.value(0)

    ENA.duty_u16(int(left_speed))
    ENB.duty_u16(int(right_speed))


def stop():

    ENA.duty_u16(0)
    ENB.duty_u16(0)

    IN1.value(0)
    IN2.value(0)

    IN3.value(0)
    IN4.value(0)


def turn_left(speed=25000):

    IN1.value(0)
    IN2.value(1)

    IN3.value(1)
    IN4.value(0)

    ENA.duty_u16(speed)
    ENB.duty_u16(speed)


def turn_right(speed=25000):

    IN1.value(1)
    IN2.value(0)

    IN3.value(0)
    IN4.value(1)

    ENA.duty_u16(speed)
    ENB.duty_u16(speed)
