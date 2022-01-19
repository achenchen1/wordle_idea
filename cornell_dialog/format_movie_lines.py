import re

with open("movie_lines.txt", "r", encoding="latin-1") as cornell:
    with open("modified.txt", "w+") as modified:
        for number, line in enumerate(cornell):
            trimmed = re.sub(r'.*(\+\+\+\$\+\+\+ )', '', line).lower()
            alphabet_regex = re.compile('[^a-z \']')
            space_regex = re.compile('( )+')
            formatted_line = space_regex.sub(' ', alphabet_regex.sub(' ', trimmed))

            modified.write(formatted_line)
            modified.write("\n")

