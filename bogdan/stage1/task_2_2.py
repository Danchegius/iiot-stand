def normalize(raw):
    number = raw.strip()
    if number == '':
        return None
    number = number.replace(',', '.')
    number = number.replace(' ', '')

    check = number
    check = check.replace('-', '')
    check = check.replace(".", "", 1)
    if check.isdigit():
        return number
    else:
        return None


if __name__ == '__main__':
    for k in ["12,5 ", "13.0", "-0,75", "####", "", "  7 ", "N/A", "1 250,3"]:
        print(normalize(k))


        