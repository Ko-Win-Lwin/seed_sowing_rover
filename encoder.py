from machine import Pin
from config import SLOTS

left_count = 0
right_count = 0

left_pin = Pin(16, Pin.IN, Pin.PULL_UP)
right_pin = Pin(17, Pin.IN, Pin.PULL_UP)


def left_irq(pin):
    global left_count
    left_count += 1


def right_irq(pin):
    global right_count
    right_count += 1


left_pin.irq(trigger=Pin.IRQ_FALLING, handler=left_irq)
right_pin.irq(trigger=Pin.IRQ_FALLING, handler=right_irq)


def get_pulses():
    return left_count, right_count


def get_average_pulses():
    return (left_count + right_count) / 2


def get_turns():
    return left_count / SLOTS, right_count / SLOTS


def reset():
    global left_count, right_count
    left_count = 0
    right_count = 0