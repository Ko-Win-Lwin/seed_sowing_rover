# Seed Sowing Robot using Raspberry Pi Pico

A smart agricultural robot car built using Raspberry Pi Pico for automatic seed sowing.

The robot:
- moves forward automatically
- maintains straighter movement using encoder correction
- stops at fixed distances
- drops seeds using a servo motor
- detects obstacles using ultrasonic sensor
- displays information on OLED display

---

# Features

- Encoder-based distance measurement
- Straight driving correction
- Automatic seed dropping
- Move → Stop → Drop → Continue workflow
- Ultrasonic obstacle detection
- OLED live status display
- Modular MicroPython project structure

---

# Hardware Components

## Microcontroller
- Raspberry Pi Pico

## Motor Driver
- L298N

## Motors
- 2x DC geared motors

## Encoders
- Wheel encoder sensors

## Servo Motor
- SG90 / MG90S / MG996R

## Sensors
- HC-SR04 Ultrasonic Sensor

## Display
- SSD1306 OLED Display (128x32)

## Power
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

## Encoder

| Function      | GPIO |
| ------------- | ---- |
| Left Encoder  | GP16 |
| Right Encoder | GP17 |

## Ultrasonic Sensor

| Function | GPIO |
| -------- | ---- |
| Trigger  | GP18 |
| Echo     | GP19 |

## Servo

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

1. Robot moves forward.
2. Encoders measure wheel rotation.
3. Distance traveled is calculated.
4. Robot stops after reaching seed spacing distance.
5. Servo opens seed gate.
6. Seed is dropped.
7. Servo closes gate.
8. Robot continues moving.
9. Ultrasonic sensor stops robot if obstacle detected.

---

# Straight Driving Logic

The robot compares:
- left wheel encoder pulses
- right wheel encoder pulses

If one wheel moves faster:
- motor speed is automatically corrected.

This improves:
- straight movement
- sowing accuracy

---

# Seed Dropping Logic

Seed dropping is based on:
- wheel encoder distance
- NOT time delay

This gives better accuracy even if:
- battery voltage changes
- terrain changes

---

# How to Run

1. Install MicroPython on Raspberry Pi Pico.
2. Copy all project files into the Pico.
3. Connect all hardware properly.
4. Run:

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

- PID control
- GPS navigation
- Line following
- Mobile app control
- Solar charging
- Automatic turning at row end
- Multi-seed hopper
- Soil moisture sensing

---

# Author

Win Lwin

Computer Science Student  
Robotics & Embedded Systems Enthusiast