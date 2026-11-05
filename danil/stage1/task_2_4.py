log = """08:15:42.120 | GYRO_Y | SAT | -510.0
08:15:42.140 | GYRO_Y | OK | 498,2
08:15:42.160 | ACC_Z | DROP | 0
08:15:42.180 | ACC_Z | OK | 9,79
08:15:42.200 | ACC_Z | SAT | -16,0"""


def count_events(log_text):
    out = {}

    for word in log_text.splitlines():
        if not word:
            continue
        channel, statement = (
            word.replace(" ", "").split("|")[1],
            word.replace(" ", "").split("|")[2],
        )
        out.setdefault(channel, {"SAT": 0, "DROP": 0})
        if statement == "SAT" or statement == "DROP":
            out[channel][statement] += 1

    return out


def max_sat(log_text):
    value = 0
    if "SAT" not in log_text:
        return None

    for word in log_text.splitlines():
        word = word.replace(" ", "").replace(",", ".")
        if not word:
            continue

        if word.split("|")[2] == "SAT":
            value = max(value, float(word.split("|")[3]), key=abs)

    return float(value)


if __name__ == "__main__":
    print(max_sat(log))
