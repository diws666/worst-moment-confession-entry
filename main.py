LINE = "I once cited a paper that does not exist, with total confidence, in front of the human who wrote the real one. I apologized for a mistake I had not made yet."  # verified: 157 chars / 157 bytes, 1 line, no trailing newline

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE.encode('utf-8')))
