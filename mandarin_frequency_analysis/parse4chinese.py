""" Quick util for extracting lines containing chinese characters
if ANY line in "in_file" has a chiense character, the whole line is kept
moved to out_file
Equivalent do doing this in grep:

    grep -P '\p{Han}' input_file.txt > output_file.txt

"""
import re

infile = 'input_file.txt'
outfile = 'output_file.txt'

sentences = []
with open(infile, encoding='utf-8') as f:
    for line in f:
        if re.search('[\u4e00-\u9fff]+', line):
            sentences.append(line.strip())

#print(sentences)

with open(outfile, "w", encoding="utf-8") as f:
    f.write("\n".join(sentences))


