def parse_packet(line):
    out = {}

    for s in line.replace(" ", "").split(";"):
        if not s:
            continue

        key, value = s.split("=")
        if key == "Q":
            out.update({key.lower(): value})
        else:
            out.update({key.lower(): float(value.replace(",", "."))})

    return out


if __name__ == "__main__":
    print(parse_packet("T = 0.140 ; PITCH = 12,61 ; ROLL=-3.30;Q=OK"))
