import re

def main():
    html = input("HTML: ")
    parsed_url = parse(html)
    if parsed_url:
        print(parsed_url)
    else:
        print("Invalid HTML or URL not found.")

def parse(s):
    match = re.search(r"<iframe(?:.|\n)*?src=\"(https?://(?:www\.)?youtube\.com/embed/([A-Za-z0-9_-]+))\"", s)
    if match:
        url = match.group(1)
        video_id = match.group(2)
        return f"https://youtu.be/{video_id}"

if __name__ == "__main__":
    main()