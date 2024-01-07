import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
        parts = [int(x) for x in ip.split(".")]
        i = 0
        while i < len(parts):
            if parts[i] < 0 or parts[i] > 255:
                return False
            else:
                i += 1
        
        return True
    else:
        return False


if __name__ == "__main__":
    main()
