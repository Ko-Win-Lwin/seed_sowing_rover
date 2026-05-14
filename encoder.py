from machine import Pin
import time

from config import SLOTS

# =========================
# COUNTERS
# =========================

left_count = 0
right_count = 0

# =========================
# DEBOUNCE
# =========================

last_left_time = 0
last_right_time = 0

DEBOUNCE_US = 5000

# =========================
# ENCODER PINS
# =========================

left_pin = Pin(16, Pin.IN, Pin.PULL_UP)
right_pin = Pin(17, Pin.IN, Pin.PULL_UP)

# =========================
# INTERRUPT FUNCTIONS
# =========================

def left_irq(pin):

    global left_count
    global last_left_time

    now = time.ticks_us()

    if time.ticks_diff(now, last_left_time) > DEBOUNCE_US:

        left_count += 1
        last_left_time = now


def right_irq(pin):

    global right_count
    global last_right_time

    now = time.ticks_us()

    if time.ticks_diff(now, last_right_time) > DEBOUNCE_US:

        right_count += 1
        last_right_time = now

# =========================
# INTERRUPT SETUP
# =========================

left_pin.irq(
    trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
    handler=left_irq
)

right_pin.irq(
    trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING,
    handler=right_irq
)

# =========================
# FUNCTIONS
# =========================

def get_pulses():

    return left_count, right_count


def get_average_pulses():

    return (
        left_count + right_count
    ) / 2


def get_turns():

    return (
        left_count / SLOTS,
        right_count / SLOTS
    )


def reset():

    global left_count
    global right_count

    left_count = 0
    right_count = 0
