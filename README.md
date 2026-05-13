# Seed Sowing Robot using Raspberry Pi Pico

A smart agricultural robot developed using Raspberry Pi Pico for automatic and accurate seed sowing.

The robot is capable of:
- moving autonomously
- maintaining straighter movement using encoder feedback
- stopping at predefined distances
- dropping seeds automatically using a servo motor
- detecting obstacles using ultrasonic sensors
- displaying live system information on an OLED display

The system uses IR optocoupler sensors with encoder discs to measure wheel rotation, speed, and travel distance for accurate seed spacing.

---

# Features

- Encoder-based distance measurement
- IR optocoupler wheel feedback system
- Straight driving correction
- Automatic seed dropping
- Move → Stop → Drop → Continue workflow
- Ultrasonic obstacle detection
- OLED live status display
- Modular MicroPython architecture

---

# Hardware Components

## Microcontroller
- Raspberry Pi Pico

## Motor Driver
- L298N Dual H-Bridge Motor Driver

## Drive Motors
- 2x DC geared motors

## Encoder System
- IR optocoupler sensors
- Encoder discs

## Servo Motor
- SG90 / MG90S / MG996R

## Distance Sensor
- HC-SR04 Ultrasonic Sensor

## Display
- SSD1306 OLED Display (128x32)

## Power Supply
- External battery pack

---

# Project Structure

```text
config.py
encoder.py
motor.py
servo.py
ultrasonic.py
oled_display.py
main.py
```

---

# Pin Configuration

## Left Motor

| Function | GPIO |
| -------- | ---- |
| IN1      | GP10 |
| IN2      | GP11 |
| ENA      | GP12 |

## Right Motor

| Function | GPIO |
| -------- | ---- |
| IN3      | GP14 |
| IN4      | GP15 |
| ENB      | GP13 |

## Encoder System

| Function      | GPIO |
| ------------- | ---- |
| Left Encoder  | GP16 |
| Right Encoder | GP17 |

## Ultrasonic Sensor

| Function | GPIO |
| -------- | ---- |
| Trigger  | GP18 |
| Echo     | GP19 |

## Servo Motor

| Function     | GPIO |
| ------------ | ---- |
| Servo Signal | GP9  |

## OLED Display

| Function | GPIO |
| -------- | ---- |
| SDA      | GP0  |
| SCL      | GP1  |

---

# Working Principle

1. The robot moves forward automatically.
2. Encoder discs rotate with the wheels.
3. IR optocoupler sensors generate pulses.
4. Raspberry Pi Pico counts encoder pulses using interrupts.
5. Distance traveled is calculated.
6. The robot stops after reaching the seed spacing distance.
7. The servo motor opens the seed gate.
8. A seed is dropped.
9. The servo closes the gate.
10. The robot continues moving.
11. The ultrasonic sensor stops the robot if an obstacle is detected.

---

# Encoder-Based Speed and Distance Measurement

The robot uses:
- IR optocoupler sensors
- encoder discs attached to wheels

to measure:
- wheel rotation
- wheel speed
- travel distance

This improves:
- straight driving
- distance accuracy
- seed spacing precision

---

# Distance Calculation

Distance traveled is calculated using:

```text
distance = wheel_turns × wheel_circumference
```

Wheel turns are calculated from encoder pulses:

```text
wheel_turns = pulses / encoder_slots
```

---

# Straight Driving Logic

The robot continuously compares:
- left wheel encoder pulses
- right wheel encoder pulses

If one wheel rotates faster:
- motor speed is automatically corrected

This helps maintain straighter movement during sowing.

---

# Seed Dropping Logic

Seed sowing is based on:
- encoder-measured distance
- NOT time delay

This provides more accurate seed spacing even when:
- terrain changes
- battery voltage changes
- wheel speed changes

---

# How to Run

1. Install MicroPython on Raspberry Pi Pico.
2. Copy all project files into the Pico.
3. Connect all hardware components properly.
4. Run the main program:

```python
main.py
```

---

# Required Libraries

- machine
- time
- utime
- ssd1306

---

# Future Improvements

- PID motor control
- GPS navigation
- Line following
- Mobile application control
- Solar charging system
- Automatic row turning
- Multi-seed hopper system
- Soil moisture monitoring
- Wireless telemetry

---

# Author

Win Lwin

Robotics & Embedded Systems Enthusiast
