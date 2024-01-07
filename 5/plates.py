def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str):
    s_len = len(s)
    if s_len < 2 or s_len > 6:
        return False

    if not s.isalnum():
        return False

    exit = False
    i = 0
    while not exit and i < s_len:
        if s[i].isdigit():
            exit = True
        else:
            i += 1

    if not exit:
        return True

    if s[i] == "0":
        return False

    if i < 2:
        return False

    digits_slice = s[i:]
    if not digits_slice.isdigit():
        return False

    return True


if __name__ == "__main__":
    main()
