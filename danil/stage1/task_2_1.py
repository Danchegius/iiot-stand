def parse_packet(line):
    out = {}
    value = float
    for s in line.strip().split(";")[:-1]:
        key, value = s.split("=")
        out.update({key.lower(): float(value.replace(",", "."))})
    for s in line.strip().split(";")[-1:]:
        key, value = s.split("=")
        out.update({key.lower(): value})
    return out


if __name__ == "__main__":
    print(parse_packet("T = 0.140 ; PITCH = 12,61 ; ROLL=-3.30;Q=OK"))
