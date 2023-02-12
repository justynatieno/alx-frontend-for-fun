 Script markdown2html.py that takes an argument 2 strings:
    a) First argument is the name of the Markdown file
    b) Second argument is the output file name
Requirements:
    a) If the number of arguments is less than 2: print in STDERR Usage: ./markdown2html.py README.md README.html and exit 1
    b) If the Markdown file doesn’t exist: print in STDER Missing <filename> and exit 1
    c) Otherwise, print nothing and exit 0