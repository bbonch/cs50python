import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    src = re.search(r"\"https?:\/\/(?:www\.)?youtube\.com\/embed\/(.*?)\"", s)
    if src:
        video_id = src.group(1)
        new_src = f"https://youtu.be/{video_id}"
    else:
        return None

    return new_src


if __name__ == "__main__":
    main()
