#!/usr/bin/python3
import sys

def markdown2html(markdown_file, output_file):
    try:
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()
    except FileNotFoundError:
        print(f"Missing {markdown_file}", file=sys.stderr)
        return 1

    # Convert markdown to HTML here

    with open(output_file, 'w') as f:
        f.write(html_content)

    return 0

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    sys.exit(markdown2html(markdown_file, output_file))
