from collections import defaultdict
import sys

words = defaultdict(int)

with open(sys.argv[1], "r", encoding="latin-1") as input_file:
    for line in input_file:
        line_words = (w for w in line.strip().split(' ') if len(w) == 5 and "\'" not in w)
        for word in line_words:
            words[word] += 1


print(sorted(words.items(), key=lambda x: x[1], reverse=True)[:100])
