import math


def to_degrees(raw):

    raw = raw.lower().replace(",", ".").strip()

    if (
        raw.endswith("deg")
        and raw[: raw.find("deg")].rstrip().replace(".", "", 1).lstrip("+-").isdigit()
    ):
        return float(raw[: raw.find("deg")].strip())

    elif (
        raw.endswith("rad")
        and raw[: raw.find("rad")].rstrip().replace(".", "", 1).lstrip("+-").isdigit()
    ):
        return math.degrees(float(raw[: raw.find("rad")]))
    # elif


if __name__ == "__main__":
    print(to_degrees("32.55 deg"))
