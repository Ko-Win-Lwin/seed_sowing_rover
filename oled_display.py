from machine import Pin, I2C
import ssd1306

try:

    i2c = I2C(
        0,
        scl=Pin(1),
        sda=Pin(0),
        freq=400000
    )

    oled = ssd1306.SSD1306_I2C(
        128,
        32,
        i2c
    )

    oled_found = True

except:

    oled_found = False


def show(state, dist, left_pulses, right_pulses):

    if not oled_found:
        return

    try:

        oled.fill(0)

        oled.text(state, 0, 0)

        if dist == -1:
            oled.text("NoDist", 0, 10)

        else:
            oled.text(f"{dist:.1f}cm", 0, 10)

        oled.text(
            f"L{left_pulses}",
            0,
            20
        )

        oled.text(
            f"R{right_pulses}",
            64,
            20
        )

        oled.show()

    except:
        pass